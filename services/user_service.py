"""
User Service — Handles registration, login, profile CRUD.
Data is persisted to data/users/users.json
"""
import json
import hashlib
import uuid
from pathlib import Path
from datetime import datetime

USERS_FILE = Path("data/users/users.json")


def _load_users() -> dict:
    if USERS_FILE.exists():
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}


def _save_users(users: dict):
    USERS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2, ensure_ascii=False)


def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


class UserService:
    AVATARS = [
        {"id": "a1", "name": "Khalid", "emoji": "🧒", "color": "#4ECDC4"},
        {"id": "a2", "name": "Maryam", "emoji": "👧", "color": "#FFB347"},
        {"id": "a3", "name": "Yusuf",  "emoji": "👦", "color": "#87CEEB"},
        {"id": "a4", "name": "Fatima", "emoji": "🧕", "color": "#DDA0DD"},
    ]

    @staticmethod
    def register(name: str, age_group: str, avatar_id: str,
                 username: str, password: str) -> tuple[bool, str]:
        """Register new user. Returns (success, message)."""
        users = _load_users()
        if username in users:
            return False, "Username already taken. Try another one!"
        if len(password) < 4:
            return False, "Password must be at least 4 characters."

        avatar = next((a for a in UserService.AVATARS if a["id"] == avatar_id),
                      UserService.AVATARS[0])
        users[username] = {
            "id": str(uuid.uuid4()),
            "username": username,
            "password_hash": _hash_password(password),
            "name": name,
            "age_group": age_group,
            "avatar": avatar,
            "xp": 0,
            "completed_missions": [],
            "badges": [],
            "created_at": datetime.utcnow().isoformat(),
            "last_login": datetime.utcnow().isoformat(),
        }
        _save_users(users)
        return True, "Welcome to the Adventure Universe!"

    @staticmethod
    def login(username: str, password: str) -> tuple[bool, dict | str]:
        """Login user. Returns (success, user_dict or error_msg)."""
        users = _load_users()
        user = users.get(username)
        if not user:
            return False, "Username not found."
        if user["password_hash"] != _hash_password(password):
            return False, "Incorrect password."
        user["last_login"] = datetime.utcnow().isoformat()
        _save_users(users)
        return True, user

    @staticmethod
    def update_progress(username: str, mission_id: str, xp_gained: int,
                        new_badges: list[str]) -> dict:
        """Update user XP, completed missions, badges. Returns updated user."""
        users = _load_users()
        user = users.get(username)
        if not user:
            return {}
        if mission_id not in user["completed_missions"]:
            user["completed_missions"].append(mission_id)
        user["xp"] += xp_gained
        for badge in new_badges:
            if badge not in user["badges"]:
                user["badges"].append(badge)
        users[username] = user
        _save_users(users)
        return user

    @staticmethod
    def get_all_avatars() -> list:
        return UserService.AVATARS
