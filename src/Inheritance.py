class User:
    def sign_in(self):
        print('logged in')


class Wizard(User):

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attack with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attack with arrows: arrows left - '
              f' {self.num_arrows}')


wizard1 = Wizard('Merlin', 50)
print(isinstance(wizard1, object))
archer1 = Archer('Robin', 100)
wizard1.attack()
archer1.attack()
