import datetime

from services.data_service import insert_user, get_all_users
from src.services.data_service import insert_operation, get_all_operations, create_operations, get_users_operations

if __name__ == "__main__":
    # user_id = insert_user("roma", "120")
    # print(f"new user id: {user_id}")
    #
    # users = get_all_users()
    # for user in users:
    #     print(user)
    # op_user_id = insert_operation(2, 200, "payment", "21.06.2025")
    # print(f"new operation_id: {op_user_id}")

    print(get_users_operations([2]))