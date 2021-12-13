class User:
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('Do Nothing')


class Wizard(User):

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'Attack with power of {self.power}')
        return ""


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attack with arrows: arrows left - '
              f' {self.num_arrows}')


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 30)


def player_atack(char):
    char.attack()


print(wizard1.attack())
