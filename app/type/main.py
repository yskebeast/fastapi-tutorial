#
# * typing is a standard module in python used for type hints
from typing import List, Tuple, Dict, Optional
from pydantic import BaseModel


def get_list(items: List[str]):
    for item in items:
        print(item.title())


# get_list(["apple", "bannana", "orange"])


def get_tuple(items: Tuple[str, str, int]):
    for i, item in enumerate(items):
        print(i, item)
        if i == 2:
            print(item)
        else:
            print(item.title())


# get_tuple(("apple", "bannana", 3))


def get_dict(items: Dict[str, str]):
    for key, value in items.items():
        print(key, value)


# get_dict({"name": "john", "age": "30"})


def get_optonal(name: Optional[str] = None):
    print(name)


# get_optonal("john")


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


# classをtypeに指定することで、Personクラスのインスタンスのみ受け付ける
def get_person_good(person: Person):
    return person.name.capitalize() + " " + str(person.age)


# print(get_person_good(Person("john", 50)))


# def get_person_bad(person: Person):
#     return person.middle_name.capitalize() + " " + str(person.age)


# print(get_person_bad(Person("alice", 18)))


class UsePydantic(BaseModel):
    name: str
    age: int


data = {"name": "john", "age": 100}
user = UsePydantic(**data)
print("user.model_dump()", user.model_dump())

print(UsePydantic(**data).model_dump())

# **data,model_dump()それぞれの役割
# * **data: 引数を辞書型に変換し、pydanticクラスに引数が別々に渡されるようにして、型に合わせてインスタンス化する
# * model_dump(): **dataで生成されたインスタンスを、辞書型に変換して返す
