from Functions import Command, Context, create_command
from InquirerTheme import SandWorldTheme
import inquirer


class Shop(Command):
    def __init__(self):
        super().__init__("Shop", "Buy items", self.callback)

    @staticmethod
    def callback(ctx: Context) -> None:
        theme = SandWorldTheme()
        items = ctx.database.get_shop_items()

        question = [
            inquirer.List("item",
                          message="Choice item",
                          choices=items
                          )
        ]
        answer = inquirer.prompt(question, theme=theme)  # getting answer

        if answer is None:  # check if user press ctrl + c
            return

        answer = answer["item"]

        for item in items:
            if item.get_name() == answer:
                answer = item
                break

        if answer.get_is_owned():
            print("You already have that item!")
            return

        if answer.get_price() > ctx.database.sand:
            print("not enough money.")
            return

        ctx.database.sand = ctx.database.sand - answer.get_price()

        ctx.database.change_item(answer.get_name(), "is_owned", True)

        print("thanks for buy!")


def on_load():
    create_command(Shop)
