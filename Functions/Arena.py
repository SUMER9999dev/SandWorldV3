from Functions import Command, Context, create_command
from random import randint
import inquirer
import InquirerTheme


class Humanoid(object):
    def __init__(self, health: int, damage: dict, armor: dict):
        self._health = health
        self._damage = damage
        self._armor = armor

    def health(self):
        return self._health

    def damage(self):
        return self._damage

    def armor(self):
        return self._armor

    def attack(self, obj) -> int:
        dmg = self._damage
        dmg = randint(dmg["min"], dmg["max"])
        self._health -= dmg
        return dmg


class Monster(Humanoid):
    def __init__(self, name: str, health: int, dmg_min: int, dmg_max: int, arm_min: int, arm_max: int):
        super().__init__(health, {"min": dmg_min, "max": dmg_max}, {"min": arm_min, "max": arm_max})
        self._name = name

    def get_name(self) -> str:
        return self._name

    def attack(self, obj) -> int:
        dmg = super().attack(obj)
        print(f"You got {dmg} damage. You're health - {obj.health()}.")
        return dmg


class Player(Humanoid):
    def __init__(self):
        super().__init__(100, {"min": 1, "max": 4}, {"min": 1, "max": 4})

    def attack(self, obj: Monster) -> int:
        dmg = super().attack(obj)
        print(f"{obj.get_name()} got {dmg} damage! Monster health - {obj.health()}.")
        return dmg


class Fight(object):
    def __init__(self, player: Player, enemy: Monster):
        self._player = player
        self._enemy = enemy
        self._finished = False
        self._winner = None
        self._theme = InquirerTheme.SandWorldTheme()

    def __bool__(self):
        return self._finished

    def get_winner(self) -> any:
        return self._winner

    def win(self, obj) -> None:
        self._finished = True
        self._winner = obj

    def step(self) -> None:
        # TODO : make block
        if self._enemy.health() <= 0:
            self.win(self._player)
            return
        elif self._player.health() <= 0:
            self.win(self._enemy)
            return

        question = [
            inquirer.List('action',
                          message="Choice action",
                          choices=["Attack"]
                          )
        ]

        answer = inquirer.prompt(question, theme=self._theme)  # getting answer

        if answer is None:  # check if user press ctrl + c
            self.win(self._enemy)
            return

        answer = answer["action"]

        if answer == "Attack":
            self._player.attack(self._enemy)

        self._enemy.attack(self._player)


class Arena(Command):
    def __init__(self):
        super().__init__("Arena", "Fight with monsters!", self.callback)

    @staticmethod
    def callback(ctx: Context):
        plr = Player()
        monster = Monster("Sand demon", 120, 5, 10, 0, 0)
        fight = Fight(plr, monster)
        while not bool(fight):
            fight.step()
        if fight.get_winner() == plr:
            print("You win!")
            ctx.database.sand = ctx.database.sand + 20
        else:
            print("You lose.")


def on_load():
    create_command(Arena)
