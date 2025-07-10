# app/crud/user_crud.py

from sqlalchemy.orm import Session
from app.models.user_model import User
from app.core.auth_core import verify_password, get_password_hash
# import app.crud.user_crud as user

# 🧠 Create new user in database
def create_user(db: Session, username: str, password: str):
    hashed_password = get_password_hash(password)
    new_user = User(username=username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# 🔐 Authenticate username + password
def authenticate_user(db: Session, username: str, password: str):
    print(f"Authenticating user: {username}")
    user = db.query(User).filter(User.username == username).first()
    if user and verify_password(password, user.hashed_password):
        return user
    return None