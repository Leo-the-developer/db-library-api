import requests

URL = "http://127.0.0.1:8000"

for i in range(20):
    requests.post(f"{URL}/books", json={
        "title": f"Book {i}",
        "author": "Unknown",
        "year": 2000 + i,
        "category": "fiction",
        "rating": i % 5 + 1
    })
