"""
DataBase model
TODO: make sqlite
"""

import json


class Item(object):
    def __init__(self, price: int, is_owned: bool, description: str, name: str):
        self._price = price
        self._is_owned = is_owned
        self._description = description
        self._name = name

    def get_name(self):
        return self._name

    def get_is_owned(self):
        return self._is_owned

    def get_price(self):
        return self._price

    def __dict__(self) -> dict:
        return {"name": self._name, "description": self._description, "price": self._price, "is_owned": self._is_owned}

    def __bool__(self) -> bool:
        return self._is_owned

    def __str__(self) -> str:
        return f"({self._name}) - {self._price}, {self._description}"


class DB(object):
    def __init__(self, name: str) -> None:
        """
        :param name: str
        """

        # value init
        self._name = name
        self.__data = {}

        # loading startup

        with open(self._name, 'r') as reader:
            self.__data = json.loads(reader.read())

    # io

    def write_data(self):
        with open(self._name, 'w') as writer:
            writer.write(json.dumps(self.__data))

    # shop

    def get_shop_items(self) -> any:
        temp = []
        for item in self.__data["Shop"]:
            temp.append(Item(item["price"], item["is_owned"], item["description"], item["name"]))
        return temp

    def add_shop_item(self, item: Item) -> None:
        self.__data["Shop"].append(item.__dict__())
        self.write_data()

    def change_item(self, name: str, key: str, new_value: any) -> None:
        for item in self.__data["Shop"]:
            if item["name"] == name:
                item[key] = new_value
                break
        self.write_data()

    def get_shop_item(self, name: str) -> Item:
        for item in self.__data["Shop"]:
            if item["name"] == name:
                return Item(item["price"], item["is_owned"], item["description"], item["name"])

    # sand property

    def get_sand(self) -> int:
        return self.__data["Sand"]

    def set_sand(self, value: int) -> None:
        self.__data["Sand"] = value
        self.write_data()

    sand = property(get_sand, set_sand)
