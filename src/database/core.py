import psycopg2
from contextlib import contextmanager
from config.database import DB_CONFIG


@contextmanager
def get_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    try:
        yield conn
    finally:
        conn.close()

@contextmanager
def getcursor():
    with get_connection() as conn:
        cursor = conn.cursor()
        try:
            yield cursor
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            cursor.close()

def execute_cuery(query:str, params=None):
    with getcursor() as cursor:
        cursor.execute(query,params or ())
        if cursor.description:
            return cursor.fetchall()