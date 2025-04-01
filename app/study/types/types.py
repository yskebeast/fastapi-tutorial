from typing import List, Dict, Optional, Union
from datetime import datetime

from pydantic import BaseModel


def get_full_name(first_name: str, last_name: str) -> str:
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))


def get_name_with_age(name: str, age: int) -> str:
    name_with_age = name + "is this old: " + str(age)
    return name_with_age


print(get_name_with_age("john", 25))


"""
TYPE: List
"""


def process_items(items: List[str]):
    for item in items:
        print(item.capitalize())


process_items(["apple", "bananna", "orange"])

"""
TYPE: Dict
"""


def process_dict(items: Dict[str, str]):
    for item_key, item_value in items.items():
        print(f"{item_key} : {item_value}")


process_dict({"name": "john", "age": "25"})


"""
TYPE: Optional
"""


def process_optional(value: Optional[str] = None):
    if value is not None:
        print(value)
    else:
        print("No value provided")


print(process_optional("Optional Value"))

"""
TYPE: Union
"""


def process_union1(value: str | None = None):
    if value is not None:
        print(value)
    else:
        print("No value provided")


process_union1()
process_union1("Union Value1")


def process_union2(value: Union[str, None] = None):
    if value is not None:
        print(value)
    else:
        print("No value provided")


process_union2()
process_union2("Union Value2")


"""
TYPE: Class
"""


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = 0


def get_person(one_person: Person) -> str:
    return one_person.name + " is " + str(one_person.age) + " years old"


person = Person("John", 25)
print(get_person(person))


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: Union[datetime, None] = None
    friends: List[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
print(user.id)
