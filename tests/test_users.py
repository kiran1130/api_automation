import pytest
import pip._vendor.requests

BASE_URL = "https://gorest.co/public/v2"

ACCESS_TOKEN = "1b5cbae0a94402635e4ce48da62910786054b44a37c22dd7aca58ee16cbd143b"

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# Test case 1: Get all users
def test_get_all_users():
    response = pip._vendor.requests.get(f"{BASE_URL}/users", headers=HEADERS)
    assert response.status_code == 200
    data = response.json()
    print(data)


# Test case 2: Get a specific user by ID
def test_get_user_by_id():
    user_id = 2498 
    response = pip._vendor.requests.get(f"{BASE_URL}/users/{user_id}", headers=HEADERS)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json()["id"] == user_id


# Test case 3: Create a new user (POST)
def test_create_user():
    new_user = {
        "name": "Test User",
        "email": "test1@test.vi",
        "status": "active"
    }
    response = pip._vendor.requests.post(f"{BASE_URL}/users", json=new_user, headers=HEADERS)
    assert response.status_code == 201  # Created
    assert isinstance(response.json(), dict)
    assert response.json()["name"] == new_user["name"]
    # You can also assert other fields and check if the 'id' is present (auto-generated)

    # Store the user ID for the next test (update)
    global created_user_id # Declare a global variable to store the created user's ID
    created_user_id = response.json()["id"]


# Test case 4: Update an existing user (PUT)
def test_update_user():
    updated_user = {
        "name": "Updated Test User",
        "email": "updated.test.user@example.com", # Use a unique email or modify other fields
        "gender": "female",
        "status": "inactive"
    }
    response = pip._vendor.requests.put(f"{BASE_URL}/users/{created_user_id}", json=updated_user, headers=HEADERS)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json()["name"] == updated_user["name"]



# Test case 5: Delete a user (DELETE)
def test_delete_user():
    response = pip._vendor.requests.delete(f"{BASE_URL}/users/{created_user_id}", headers=HEADERS)
    assert response.status_code == 204

    get_response = pip._vendor.requests.get(f"{BASE_URL}/users/{created_user_id}", headers=HEADERS)
    assert get_response.status_code == 404