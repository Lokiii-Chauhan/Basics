class PlayerCharacter:
    membership = True

    def __init__(self, name):
        self.name = name

    def run(self):
        print('run')

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2


# player1 = PlayerCharacter('Loki')

print(PlayerCharacter.adding_things(5, 6))
