# z = {1:'key1', 2:'key2', 3:'key3'}
# del(z[1]) # удаление элемента словаря
# z.pop(2) # удаление элемента словаря
"""print(z.keys())
print(1 in z)"""#для проверки ключа
# print(z)

# a=[('a', 1), ('b', 2)] #картеж переформатровать в словарь
# b={}
# for color, n in a:
#     b[color]=n
# print(b)

# a=dict(name='Turatbek', prof='prog') #картеж переформатровать в словарь
# print(a)




# z = {'c1': 'Red', 'c2': 'Green', 'c3': None}
# z.update({'c2':'Зеленый'})
# # for i in z:
# #     if z[i]!=None:
# #         b=[]
# #         b.append(z[i])
# #         print(b)

# # b = []
# # for v in z.values():
# #     b.append(v)
# # print(b)

# c = {key: value for key, value in z.items() if value is not None}
# print(c)
