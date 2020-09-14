"""
Dig command
"""

from Functions import Command, Context, create_command
from random import randint


class Dig(Command):
    def __init__(self) -> None:
        """
        :return: None
        """
        super().__init__("Dig", "You dig some sand!", self.callback)

    @staticmethod
    def callback(ctx: Context) -> None:
        """
        dig sand!
        :param ctx: context
        :return: None
        """
        min_sand = 1
        max_sand = 4

        if ctx.database.get_shop_item("shovel").get_is_owned():
            min_sand += 2
            max_sand += 2

        got_sand = randint(min_sand, max_sand)

        print(f"You got {got_sand} sand!")

        ctx.database.sand = ctx.database.sand + got_sand


def on_load():
    create_command(Dig)
