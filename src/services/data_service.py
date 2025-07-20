from src.database.core import execute_cuery
from src.database.models import User
from src.database.queries import GET_USERS, INSERT_USERS


def insert_user(name: str, password: str) -> int:
    result = execute_cuery(INSERT_USERS, (name, password))
    return result[0][0] if result else None


def get_all_users() -> list[User]:
    users = []
    result = execute_cuery(GET_USERS)
    for row in result:
        users.append(User(id=row[0], name=row[1], password=row[2]))
    return users