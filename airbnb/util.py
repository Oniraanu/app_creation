import bcrypt


def hash_password(password: str):
    password = password.encode()
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt).decode()


def validate_password(user_password, hash_password):
    user_password = user_password.encode()
    hash_password = hash_password.encode()
    return bcrypt.checkpw(user_password, hash_password)


if __name__ == '__main__':
    passw = hash_password("Hello007")
    print(validate_password("Hello07", passw))


