from pydantic import BaseModel

# Shared base model
class UserBase(BaseModel):
    name: str

# Model for creating a user (POST)
class CreateUser(UserBase):
    pass

# Model for updating a user (PUT)
class UpdateUser(UserBase):
    pass

# Full User model with ID
class User(UserBase):
    id: int
