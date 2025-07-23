from src.database.core import execute_cuery
from src.database.models import User, Operation
from src.database.queries import GET_USERS, INSERT_USERS, CREATE_TABLE_OPERATIONS, GET_OPERATIONS, INSERT_OPERATION, \
    GET_USER_OPERATIONS


def insert_user(name: str, password: str) -> int:
    result = execute_cuery(INSERT_USERS, (name, password))
    return result[0][0] if result else None

def create_operations():
    execute_cuery(CREATE_TABLE_OPERATIONS)
    return "operations table appeared"

def insert_operation(id: int, amount: int, type: str, date: str):
    result = execute_cuery(INSERT_OPERATION, (id, amount, type, date))
    return result[0][0] if result else None

def get_all_users() -> list[User]:
    users = []
    result = execute_cuery(GET_USERS)
    for row in result:
        users.append(User(id=row[0], name=row[1], password=row[2]))
    return users

def get_all_operations() -> list[Operation]:
    operations = []
    result = execute_cuery(GET_OPERATIONS)
    for row in result:
        operations.append(Operation(id=row[0], amount=row[1], type=row[2], date_of_operation=row[3]))
    return operations

def get_users_operations(users_id):
    operations = []
    result = execute_cuery(GET_USER_OPERATIONS, users_id)
    for row in result:
        operations.append(Operation(id=row[0], amount=row[1], type=row[2], date_of_operation=row[3]))
    return operations
