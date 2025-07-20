from services.data_service import insert_user, get_all_users

if __name__ == "__main__":
    user_id = insert_user("ilya", "123")
    print(f"new user id: {user_id}")

    users = get_all_users()
    for user in users:
        print(user)