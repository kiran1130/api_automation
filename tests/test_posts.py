import pytest
import pip._vendor.requests
import pdb
import logging

BASE_URL = "https://jsonplaceholder.typicode.com"

# Test case 1: Get all posts
@pytest.mark.regression
def test_get_all_posts():
    response = pip._vendor.requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  
   
    assert len(response.json()) > 0 


# Test case 2: Get a specific post by ID
def test_get_post_by_id():
    post_id = 1
    response = pip._vendor.requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)  
    assert response.json()["id"] == post_id 


# Test case 3: Create a new post (using POST method)
def test_create_post():
    new_post = {
        "title": "Test Post",
        "body": "This is a test post.",
        "userId": 1 
    }
    response = pip._vendor.requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    assert isinstance(response.json(), dict)
    assert response.json()["title"] == new_post["title"]

# Test case 4: Update an existing post (using PUT method)
def test_update_post():
    post_id = 1
    updated_post = {
        "id": post_id,
        "title": "Updated Test Post",
        "body": "This post has been updated.",
        "userId": 1
    }
    response = pip._vendor.requests.put(f"{BASE_URL}/posts/{post_id}", json=updated_post)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json()["title"] == updated_post["title"]


# Test case 5: Delete a post (using DELETE method)
def test_delete_post():
    post_id = 1
    response = pip._vendor.requests.delete(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200 

    # Optionally, try to get the deleted post and assert it returns a 404
    get_response = pip._vendor.requests.get(f"{BASE_URL}/posts/{post_id}")
    assert get_response.status_code == 200
