#1 def decorator(func): #(func) = say
#     # def obertka(b, c, d): #say(name, surname, age)
#     def obertka(*args, **kwargs): #все аргументы и значение, можно и без args, kwargs. можно просто буквы со звездочкой**
#         print('функция старт')
#         # func(b, c, d) #say(name, surname, age)
#         func(*args, **kwargs) #все аргументы и значение
#         print('функция стоп')
#     return obertka

# def say(name, surname, age):
#     print('Hello', name, surname, age)

# a = decorator(say)
# a('Turatbek', 'Torubai uulu', 30)

#2 def decorator(func): #(func) = say
#     # def obertka(b, c, d): #say(name, surname, age)
#     def obertka(*args, **kwargs): #все аргументы и значение, можно и без args, kwargs. можно просто буквы со звездочкой**
#         print('функция старт')
#         # func(b, c, d) #say(name, surname, age)
#         func(*args, **kwargs) #все аргументы и значение
#         print('функция стоп')
#     return obertka

# @decorator
# def say(name, surname, age):
#     print('Hello', name, surname, age)

# say('Turatbek', 'Torubai uulu', 30)

#3 def lowercase(func):
#     def wrapper():
#         func_ret = func()
#         change_to_lowercase = func_ret.lower()
#         return change_to_lowercase
#     return wrapper

# @lowercase
# def hello_function():
#     return 'HELLO WORLD'

# print(hello_function())
