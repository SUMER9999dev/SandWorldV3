from Functions.CommandModel import Command, Context


commands = []


class ErrorCommand(Command):
    def __init__(self):
        super().__init__("error", "error command", self.callback, False)

    @staticmethod
    def callback() -> None:
        print("Invalid command!")


def create_command(command: any) -> None:
    commands.append(command())


def get_command(name: str) -> any:
    for command in commands:
        if command.name == name:
            return command
    return ErrorCommand()


def load_command(filename: str) -> None:
    __import__(filename, fromlist=["object"]).on_load()
