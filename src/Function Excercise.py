def highest_even(numbers):
    evens = []
    for items in numbers:
        if items % 2 == 0:
            evens.append(items)

    return max(evens)


print(highest_even([10, 2, 3, 4, 8, 11]))
