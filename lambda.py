# # def say(a,b):
# #     print(a-b)
# sayhello = lambda a, b: a+b
# # say(30, 15)
# print(sayhello(34, 32))


# func = lambda x:eval(x) # calculater
# print(func('{0}{1}{2}'.format(input('Number 1: '),input('Operation: '),input('Number 2: '))))


# b=['aito', 'kirill', 'taalai', 'umut', 'daniar', 'turatbek']
# new = list(map(lambda string: string.upper(), b))
# print(new)


# g = ['google', 'yandex', 'mcrosoft', 'spaceX', 'neirolink', 'WHATSAPP']
# f = list(filter(lambda a: 's' in a.lower(), g))
# e = list(map(lambda lower: lower.lower(), f))# функция для перевести на нижную регстр с помощью lambda
# print(f)
# print(e)


# x = 'cat'
# y = 'dog'
# h = ['cat', 'dog']
# f = list(filter(lambda a: a in y, h))
# print(f)