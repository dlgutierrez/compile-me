
import requests
from typing import Optional


BASE_URL = "http://localhost:5000"

def test_root_endpoint():
    print("Testing root endpoint (GET /)...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    print("-" * 50) 


def test_items_endpoint(item_id: int, q: Optional[str] = None):
    print(f"Testing items endpoint (GET /items/{item_id})...")
    params = {}
    if q is not None:
        params["q"] = q
    response = requests.get(f"{BASE_URL}/items/{item_id}", params=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    print("-" * 50)


def main():
    print("🚀 Testing FastAPI endpoints...\n")
    test_root_endpoint()
    test_items_endpoint(42)
    test_items_endpoint(123, "test query")
    test_items_endpoint(999, "another test")


if __name__ == "__main__":
    main()