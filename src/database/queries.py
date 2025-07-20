CREATE_TABLE = """
CREATE TABLE if not EXISTS users(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);
"""

INSERT_USERS = """
INSERT INTO users(name, password) VALUES(%s, %s)
RETURNING id;
"""

GET_USERS = "SELECT * FROM USERS;"