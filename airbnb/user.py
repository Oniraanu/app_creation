import json
from pathlib import Path
from util import hash_password, validate_password


def get_file_path():
    path = Path("../data/users/user.json").resolve()

    if path.exists():
        return path

    path.parent.mkdir(exist_ok=True, parents=True)
    path.touch(exist_ok=True)
    return path


def get_users():
    file_path = get_file_path()

    with file_path.open(mode="r", encoding="utf-8") as file:
        try:
            users = json.load(file)
            return users
        except json.decoder.JSONDecodeError:
            return []


def save_user(user):
    user["password"] = hash_password(user["password"])

    file_path = get_file_path()
    users = get_users()

    if [u for u in users if u["username"] == user["username"]]:
        print(f"User with username {user['username']} already exists")
        return

    users.append(user)

    with file_path.open(mode="w", encoding="utf-8") as file:
        json.dump(users, file)


def get_user_by_username(username):
    users = get_users()
    user_list = [u for u in users if u["username"] == username]
    if user_list:
        return user_list[0]
    return f"User with username {username} not found"


users = {
    "first_name": "Olubunmi",
    "last_name": "Bakre",
    "email": "bakreolubunmi@yahoo.com",
    "phone": "09058209277",
    "username": "Oniraanu",
    "password": "confidential",
    "role": "OWNER"
}

if __name__ == '__main__':
    print("HELLO")
    save_user(users)
    print(get_user_by_username("Oniraanu"))
