CREATE_TABLE = """
CREATE TABLE if not EXISTS users(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);
"""
GET_USER_OPERATIONS = """
SELECT * FROM operations INNER JOIN USERS ON users.id = operations.id WHERE users.id = %s
"""

INSERT_USERS = """
INSERT INTO users(name, password) VALUES(%s, %s)
RETURNING id;
"""


CREATE_TABLE_OPERATIONS = """
CREATE TABLE if not EXISTS operations(
    id INTEGER REFERENCES users(id),
    type VARCHAR(100) NOT NULL,
    amount integer NOT NULL,
    date_of_operation varchar(10) NOT NULL 
);
"""

INSERT_OPERATION = """
INSERT INTO operations(id, amount, type, date_of_operation) VALUES(%s, %s, %s, %s)
RETURNING id;
"""

GET_USERS = "SELECT * FROM USERS;"

GET_OPERATIONS = "SELECT * FROM OPERATIONS"