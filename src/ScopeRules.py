# 1- Start with local Scope
# 2- Parent Local?
# 3- Global
# 4- Built in Python Functions

a = 1


def confusion():
    global a
    a = 5
    return a


print(confusion())
print(a)
print(confusion())

