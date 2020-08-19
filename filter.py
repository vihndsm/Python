# # def poisk(a):
# #     return 's' in a.lower()# так как мы не занем внутри списка
# # def lower(f):
# #     return f.lower() # функция для перевести на нижную регстр
# g = ['google', 'yandex', 'mcrosoft', 'spaceX', 'neirolink', 'WHATSAPP']
# # b = list(filter(poisk, g))
# # c = list(map(lower, b)) 
# # print(b)
# # print(c)

# f = list(filter(lambda a: 's' in a.lower(), g))
# e = list(map(lambda lower: lower.lower(), f))# функция для перевести на нижную регстр с помощью lambda
# print(f)
# print(e)
