# p = open('text.txt', 'r') # открыть в режиме чтение
# a = p.read()
# print(a)
# p.close()

# a = open('text1.txt', 'r') # чтение по строкам текста
# for line in a:
#     print(line)
# a.close()

# a = open('text1.txt', 'w') # написать новый текст
# a.write('alex')
# a = open('text1.txt', 'r')
# b = a.read()
# print(b)
# a.close()

# with open('text1.txt', 'r+') as a:
#     a.write('kirill')
#     for line in a:
#         print(line)
# a.close()

# p = open('text.txt', 'w') # открыть в режиме чтение
# print('имя файла: ', p.name)
# print('Возвращает True если файл был закрыт: ', p.closed)
# print('в каком режиме: ', p.mode)

# with open('text1.txt', 'r') as a: #построчно читать файл и сохранять его в виде списка
#     b = a.readlines()
#     print(b)

# s = ['Aito','Kirill','Taalai','Umut'] #перевести список по строкам
# s = [i + '\n' for i in s]
# with open('text1.txt','w') as f:
#     f.writelines(s)

# with open('text1.txt') as a: #подсчета количества строк в текстовом файле
#     print(len(a.readlines()))

# with open('text.txt') as f: #программа на python, чтобы найти самые длинные слова.
#   a = f.read().split()
#   print(max(a, key=len))
# with open('text.txt') as f:  #программа на python, чтобы найти самые длинные слова.
#     print(sorted(f.read().split('\n'),key = len)[::-1])