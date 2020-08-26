# def upper(string):
#     return string.upper()
# def lower(string):
#     return string.lower()

# a=['AITO', 'KIRILL', 'TAALAI', 'UMUT', 'DANIAR', 'TURATBEK']
# b=['aito', 'kirill', 'taalai', 'umut', 'daniar', 'turatbek']
# m1 = list(map(upper, b))
# m2 = list(map(lower, a))
# print(m1,'\n', m2)
# # upper('string')
# # print(upper('turatbek'))


# def spisok(int): #str to list
#     return int
# a = '12345'
# m1 = list(map(spisok, a))
# print(m1)


# def spisok(int): #проверка имеется ли в списке ноль
#     try:
#         if int == 0:
#             print('zero is excist')
#         else:
#             print('not excist')
#     except SyntaxError:
#         print('error')
#     return int
# a = [1, 2, 3, 4, 5, 0]
# m1 = list(map(spisok, a))
# print(m1)


# def spisok(*a, **k):
#     return *a == 0
# a = [2,3,4,5,0]
# b = [3,5,62,2,3]
# m1 = list(map(spisok,a, b))
# # m2 = list(map(spisok,b))
# print(m1)
# # print(m2)

# print(list(map(lambda x: x.capitalize(), ['cat', 'dog', 'cow'])))

# old_list = ['1', '2', '3', '4', '5', '6', '7']
# new_list = []
# for item in old_list:
#     new_list.append(int(item))
# print(new_list)

# print(list(map(lambda x: int(x), ['1', '2', '3', '4', '5', '6', '7'])))