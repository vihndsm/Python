# class Person:
#     name = 'default'
#     age = '18'
#     prof = 'IT'
#     def set(self, name, age, prof):
#         self.name = name
#         self.age = age
#         self.prof = prof

# class Student(Person):
#     vak = 'FIT'
#     course = 1
#     money = 1
#     def abc(self, vak, course, money):
#         self.vak = vak
#         self.course = course
#         self.money = money
# alex = Student()
# alex.set('Alex', 21, 'Python dev')
# alex.abc('IR', 3, 200)
# # alex.vak = 'IR'
# # alex.course = 4
# # alex.money = 100
# print(alex.name, alex.age, alex.prof, alex.vak, alex.course, alex.money)


# aito = Person()
# aito.set('Aito', 18, 'PY dev')
# print(aito.name, aito.age, aito.prof)

# taalai = Person()
# taalai.name = 'Taalai'
# taalai.age = 23
# taalai.prof = 'dev'
# print(taalai.name, taalai.age, taalai.prof)

# turat = Person()
# turat.name = 'Turatbek'
# turat.age = 30
# turat.prof = 'juni dev'
# print(turat.name, turat.age, turat.prof)

# umut = Person()
# umut.name = 'Umut'
# # umut.age = 29
# # umut.prof = 'mid dev'
# print(umut.name, umut.age, umut.prof)

# class Person: #проверка на проходе
#     name = 'default'
#     age = '18'
#     lastname = 'IT'
#     def _set(self, name, age, lastname):
#         self.name = input('name: ')
#         self.lastname = input('lastname:' )
#         self.age = int(input('age: '))

# class Blank(Person):
#     vak = 'FIT'
#     money = 1
#     def __abc(self, vak, course, money):
#         self.vak = input('faculty: ')
#         self.money = int(input('money: '))
# a = Blank()
# a._set(1, 2, 3) # _ = предупреждение
# a._Blank__abc(1, 2, 3) # __ = безопасное сокрытие данных
# print(a.name, a.lastname, a.age, a.vak, a.money)

# if a.money > 35000:
#     print('Pass')
# else:
#     print('Stop!')

# class Car:   #полиморфизм
#    def start(self, a, b=None):
#         if b is not None:
#             print (a + b)
#         else:
#             print (a)
# car_a = Car()  
# car_a.start(10)
# car_a.start(10, 20)

# class Win_Door: # Композиция
#      def __init__(self, x, y):
#           self.square = x * y 
# class Room:
#     def __init__(self, x, y, z):
#         self.square = 2 * z * (x + y)
#         self.wd = []
#     def addWD(self, w, h):
#         self.wd.append(Win_Door(w, h))
#     def workSurface(self):
#         new_square = self.square
#         for i in self.wd:
#             new_square -= i.square
#         return new_square
 
# r1 = Room(6, 5, 2) 
# print(r1.square) # выведет 48.6
# r1.addWD(1, 1) 
# r1.addWD(1, 1)
# r1.addWD(1, 2)
# print(r1.workSurface()) # выведет 44.6