from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    password:str

@dataclass
class Operation:
    id: int
    amount: int
    type: str
    date_of_operation: str

