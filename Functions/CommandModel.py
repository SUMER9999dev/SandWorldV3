"""
Function and context model
"""
from DataBase import DB


class Context(object):
    def __init__(self, database_singleton: DB):
        """
        :param database_singleton: DB
        """

        self._data = database_singleton

    @property
    def database(self):
        """
        :return: database
        """

        return self._data


class Command(object):
    def __init__(self, name: str, description: str, callback, ctx_required: bool = True) -> None:
        """
        :param name: str
        :param description: str
        :param callback: function(ctx_required[context]) -> None
        """

        self.__name = name.lower()
        self.__description = description
        self.__callback = callback
        self.__ctx_required = ctx_required

    @property
    def name(self) -> str:
        """
        :property: command name
        """

        return self.__name

    @property
    def description(self) -> str:
        """
        :property: command description
        """

        return self.__description

    def call(self, context: Context) -> None:
        """
        :call command: {
            :param: context
        }
        :param: Context
        :return: None
        """
        if self.__ctx_required:
            self.__callback(context)
        else:
            self.__callback()

    def __str__(self):
        return self.__name
