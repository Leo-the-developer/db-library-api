from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models
from fastapi.responses import JSONResponse
from sqlalchemy import func

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books")
def create_book(book: dict, db: Session = Depends(get_db)):
    obj = models.Book(**book)
    db.add(obj)
    db.commit()
    return obj

@app.get("/books")
def get_books(limit: int = 10, offset: int = 0, db: Session = Depends(get_db)):
    return db.query(models.Book).limit(limit).offset(offset).all()

@app.post("/users")
def create_user(user: dict, db: Session = Depends(get_db)):
    obj = models.User(**user)
    db.add(obj)
    db.commit()
    return obj

@app.post("/loans")
def create_loan(loan: dict, db: Session = Depends(get_db)):
    obj = models.Loan(**loan)
    db.add(obj)
    db.commit()
    return obj

@app.get("/loans/with-users")
def loans_with_users(db: Session = Depends(get_db)):
    results = db.query(
        models.Loan.id,
        models.User.name.label("user_name"),
        models.Book.title.label("book_title"),
        models.Loan.loan_date,
        models.Loan.return_date
    ).join(models.User, models.User.id == models.Loan.user_id
    ).join(models.Book, models.Book.id == models.Loan.book_id
    ).all()

    return JSONResponse(content=[dict(r._asdict()) for r in results])

@app.get("/books/category-count")
def books_group_by_category(db: Session = Depends(get_db)):
    results = db.query(
        models.Book.category,
        func.count(models.Book.id).label("count")
    ).group_by(models.Book.category).all()

    return JSONResponse(content=[{"category": r.category, "count": r.count} for r in results])

@app.put("/books/update-rating")
def update_books_rating(author: str, db: Session = Depends(get_db)):
    books = db.query(models.Book).filter(models.Book.author == author).all()
    for b in books:
        b.rating = (b.rating or 0) + 1
    db.commit()
    return {"updated": len(books)}
