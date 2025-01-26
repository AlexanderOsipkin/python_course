# print("Hello from Pycharm")
# print('alex', '10', True)
# print(dir(__builtins__))

name = input('Enter your name: ')
age = input('Enter your age: ')
city = input('Enter your city: ')
print(name, age, city)

print(name.capitalize())
# Возвращает в ответе имя с заглавной буквы
print(name.upper())
# Возвращает в ответе имя заглавными буквами
print(dir(name))


def my_name():
    print(name)
    my_name('Alex')


my_name('Alex')

