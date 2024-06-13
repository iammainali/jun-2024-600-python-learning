a.sort(key=get_second_element)
print(a)


def get_second_element(x):
    return x[-1]


data = [(1, 2, 12), (3, 1, 14), (1, 1), (5, 2, 6)]

# sort the above data based on last item of the each tuple.


def get_last_element(x):
    return x[-1]


a.sort(key=get_last_element)
print(a)
