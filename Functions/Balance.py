"""
Balance command
"""

from Functions import Command, Context, create_command


class Balance(Command):
    def __init__(self) -> None:
        """
        :return: None
        """
        super().__init__("Balance", "get balance", self.callback)

    @staticmethod
    def callback(ctx: Context) -> None:
        """
        :param ctx: Context
        :return: None
        """
        print(f"You're balance: {ctx.database.sand}")


def on_load():
    create_command(Balance)
