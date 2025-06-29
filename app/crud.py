from app.models import User

# Simulated in-memory database
users = [
    User(id=1, name="Alice"),
    User(id=2, name="Bob")
]

# Helper to find user by ID
def get_user_by_id(user_id: int):
    return next((user for user in users if user.id == user_id), None)
