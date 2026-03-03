
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    # Arrange: (No special setup needed)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert "participants" in data["Chess Club"]

def test_signup_activity():
    # Arrange
    test_email = "tester@mergington.edu"
    activity = "Chess Club"
    signup_url = f"/activities/{activity.replace(' ', '%20')}/signup?email={test_email}"

    # Act
    signup_response = client.post(signup_url)

    # Assert
    assert signup_response.status_code in (200, 400)  # 400 if already signed up

    # Act (get updated activities)
    get_response = client.get("/activities")
    data = get_response.json()

    # Assert
    assert test_email in data[activity]["participants"]
