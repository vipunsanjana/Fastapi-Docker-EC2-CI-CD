from fastapi import FastAPI, HTTPException
from app.models import User, CreateUser, UpdateUser
from app.crud import users, get_user_by_id

app = FastAPI()

# 🔍 READ all users
@app.get("/users", response_model=list[User])
def get_users():
    return users

# 📄 READ single user
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# ➕ CREATE new user
@app.post("/users", response_model=User)
def create_user(user: CreateUser):
    new_id = max([u.id for u in users], default=0) + 1
    new_user = User(id=new_id, name=user.name)
    users.append(new_user)
    return new_user

# ✏️ UPDATE user
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated: UpdateUser):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.name = updated.name
    return user

# ❌ DELETE user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Cannot delete, user not found")
    users.remove(user)
    return {"detail": f"User with ID {user_id} deleted"}
