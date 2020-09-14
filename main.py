"""
entry point
"""

import Functions
import DataBase
import os
import inquirer
import InquirerTheme

# classes init
data = DataBase.DB("data.json")
context = Functions.Context(data)
theme = InquirerTheme.SandWorldTheme()

# load cogs
for function in os.listdir("Functions"):
    if function.endswith(".py") and function != "__init__.py" and function != "CommandModel.py":
        Functions.load_command(f"Functions.{function[:-3]}")


# main
def main() -> None:
    while True:
        question = [
            inquirer.List('command',
                          message="Choice command",
                          choices=Functions.commands
                          )
        ]
        answer = inquirer.prompt(question, theme=theme)  # getting answer
        if answer is None:  # check if user press ctrl + c
            break
        answer = answer["command"]
        Functions.get_command(answer.lower()).call(context)  # getting command by name and calling with context


if __name__ == '__main__':
    main()
