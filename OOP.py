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


# class Win_Door: # Композиция
#     def __init__(self, x, y):
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
 
# r1 = Room(6, 10, 3) 
# print(r1.square)
# r1.addWD(2, 6) 
# r1.addWD(1, 2)
# r1.addWD(1, 2)
# print(r1.workSurface())

################################################
# class Car:   #полиморфизм
#    def start(self, a, b=None):
#         if b is not None:
#             print (a + b)
#         else:
#             print (a)
# car_a = Car()  
# car_a.start(10)
# car_a.start(10, 20)


# class Cat():
# #     breed = 'brid'
# #     def set_value(self, name, age=0):
# #         self.name = name
# #         self.age = age

# # bob = Cat()
# # bob.set_value('Bob')
# # print(bob.name, bob.age)
#      def __init__(self, name, breed ='brid', age=1, color='white'):
#         self.name=name
#         self.age=age
#         self.breed=breed
#         self.color=color

# walt = Cat('Walt')
# bobi = Cat('Abc')
# print(walt.name, walt.breed, walt.age, walt.color)
# print(bobi.name, bobi.breed, bobi.age, bobi.color)

# class Animal: #Полиморфизм
#     # legs = 4
#     # tail = 1
#     def voice(self):
#         print('Какой-то звук')
# class Cat():
#     def voice(self):
#         print('Мяу мяу')
# class Dog():
#     def voice(self):
#         print('Гав-гав')
# class Bull():
#     def voice(self):
#         print('муу')

# cat1, cat2 = Cat(), Cat()
# dog1, dog2 = Dog(), Dog()
# bull1, bull2  = Bull(), Bull()

# an = Animal()
# farm_band = [cat1, cat2, dog1, dog2, bull1, bull2, an]

# for i in farm_band:
#     if isinstance(i, Cat):
#         i.voice()
#     if isinstance(i, Dog):
#         i.voice()
#     if isinstance(i, Bull):
#         i.voice()
#     if isinstance(i, Animal):
#         i.voice()


# class Task2:
#     def get_String(self):
#         self.string = input('String:')
#     def print_String(self):
#         print(self.string.upper())
# newobj = Task2()
# newobj.get_String()
# newobj.print_String()