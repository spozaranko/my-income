from src.database.core import execute_cuery
from src.database.queries import CREATE_TABLE


def initialize_database():
    execute_cuery(CREATE_TABLE)
    print("init complete")

if __name__ == "__main__":
    initialize_database()