class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("Puchiii", 2)
cat2 = Cat("luciii", 1)
cat3 = Cat("oreo", 1)


def oldest_cat(*args):
    return max(args)

print(f'The oldest cat is {cat1.age} {cat2.age} {cat3.age} years old')