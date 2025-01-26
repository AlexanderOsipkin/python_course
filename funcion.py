def hello(name):
    print('Hello there,', name)
    print('Hi there,', name)


hello('Alex')
hello('Alice')


def sum_nums(a, b):
    sum = a + b
    return sum


first_sum = sum_nums(10, 5)
print(first_sum)
second_sum = sum_nums(10.5, 15)
print(second_sum)
print(sum_nums(sum_nums(20.5, 20),30))