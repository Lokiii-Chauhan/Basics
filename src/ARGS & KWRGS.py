def super_func(name, *args, i='hi', **kwargs):
    print(args)
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func('Lokiii', 1, 2, 3, 4, 5, num1=5, num2=10))

# Rule: params, *args, default parameters, **kwargs
