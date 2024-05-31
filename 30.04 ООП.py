# class Cat():
#     def __init__(self, breed, color, age):
#         self._breed = breed
#         self._color = color
#         self._age = age
#
#     @property
#     def breed(self):
#         return self._breed
#
#     @property
#     def color(self):
#         return self._color
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, new_age):
#         if new_age > self._age:
#             self._age = new_age
#         return self._age
#
#     def meow(self):
#         print('Мяу')
#
#     def purr(self):
#         print('Мрррр')
#
#     def sleep(self):
#         print('Свернулся в клубочек и спит')
#
#
# class HomeCat(Cat):
#     def __init__(self, breed, color, age, owner, name):
#         super().__init__(breed, color, age)
#         self._owner = owner
#         self._name = name
#
#     @property
#     def owner(self):
#         return self._owner
#
#     @property
#     def name(self):
#         return self._name
#
#     def getFood(self):
#         print('Мяу-Мяу')
#
#
# class Parrot():
#     def sleep(self):
#         print('Спит на жердочке')
#
#
# def homeSleep(animal):
#     animal.sleep()

#
# class Predator:
#     def hunt(self):
#         print('Oхотится')
#
#
# class CatH(Predator):
#     def __init__(self, name, color):
#         super().__init__()
#         self._name = name
#         self._color = color
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def color(self):
#         return self._color


# cat1 = CatH('Британская', 'Серая')
# print(cat1.hunt())
#
# my_cat = HomeCat('Персидская', 'Рыжая', 3, 'Давид', 'Рыжик')
# print(my_cat.owner)
# print(my_cat.breed)
# print(my_cat.getFood())
# print(my_cat.purr())
#
# cat1 = Cat('Британская', 'Серая', 5)
# cat2 = Cat('Египетская', 'Лысая', 2)
# #
# print(cat1.breed)
# print(cat1.color)
# print(cat1.age)
# #
# cat1.age = 10
# print(cat1.age)
# #
# # cat1 = Cat()
# # parrot = Parrot()
# # homeSleep(cat1)
# # homeSleep(parrot)



# class Drink:
#     volume = 300
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def drink_sth(self):
#         print(f"Я люблю пить {self.name}")
#
#     def info(self):
#         print(f'Название напиток: {self.name}, Цена:{self.price}, Объём:{self.volume}')
#
#     def drinking(self):
#         if self.volume > 0:
#             self.volume = self.volume - 100
#             print(f'Я сделал глоток, осталось {self.volume}', f'Было {Drink.volume}')
#         else:
#             print('Нечего пить')
#
#
# class With_gaz(Drink):
#     color = ['red', 'green', 'black']
#
#     def __init__(self, name, price):
#         super().__init__(name, price)

# coffe = Drink('Кофе', 2)
# Drink.volume = 5
# coffe.volume = 7
# print(coffe.volume, Drink.volume)
# coffe.drink_sth()
# coffe.info()
# coffe = Drink('Кофе', 2)
# coffe.volume = 7
# water = Drink('Вода', 1)
# soda = Drink('Газировка', 2)
# soda.volume = 1
# water.volume = 0.5
# water.info()
# coffe.info()

# limonade = With_gaz('Cola', 5)
# #print(limonade.name)
# limonade.color = With_gaz.color[-1]
# limonade.info()
# print(limonade.color)
# coffe.info()
# coffe.drinking()
# coffe.drinking()
# coffe.drinking()
# coffe.drinking()


'''Строки в Питоне сравниваются на основании значений символовю т.е если мы захотим выяснить, что больше Apple или
Яблоко, - то Яблоко  окажется больше. А все потому, что английская А имеет значение 65(берется из таблицы кодировки)
, а русская буква Я -1071 (c помощью функции ord()-это можно выяснить). Такое положение дел не устроило Анну. Она
считает, что строки нужно сравнивать по количеству входящих в них символов. Для этого девушка создала класс RealString
 и реализовала озвученный инструментарий. Сравнивать между собой можно как объекты класса, так и обычные строки с
 экземплярами классе RealString. К слову, Анне понадобилось только 3 метода внутри класса(включая __ init__()) для
 воплощения задуманного'''
#



'''Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник. 
для этого он решил создать класс TriangleChecker, принимающий только положительные числа. С помощью метода is_triangle
() возвращаются следующие значения(в зависимости от ситуации):
- ура, можно построить треугольник
-С отрицательными числами ничего не выйдет!
-Нужно вводить только числа!
- Жаль, но из этого треугольник не сделать.'''
#
# class TriangleChecker:
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#     def is_triangle(self):
#         if self.x != 0 and self.y != 0 and self.z != 0:
#             res = 'ура, можно построить треугольник'
#             if self.x < 0 or self.y < 0 or self.z < 0:
#                 res = 'С отрицательными числами ничего не выйдет!'
#         else:
#             res = 'Жаль, но из этого треугольник не сделать.'
#         return res
#
# try:
#     str = [int(input(f'Введите отрезок {x + 1} >>')) for x in range(3)]
#     triangle = TriangleChecker(str[0], str[1], str[2])
#     print(triangle.is_triangle())
# except ValueError:
#     print('Нужно вводить только числа!')



# class TriangleChecker:
#     min = -1000000
#     max = 10000000
#
#     @classmethod
#     def validate(cls, arg):
#       return cls.min <= arg <= cls.max
#
#     def __init__(self, x, y, z):
#         self.x = self.y = 0
#         if self.validate(x) and self.validate(y) and self.validate(z):
#             self.x = x
#             self.y = y
#             self.z = z
#     def is_triangle(self):
#         if self.x != 0 and self.y != 0 and self.z != 0:
#             res = 'ура, можно построить треугольник'
#             if self.x < 0 or self.y < 0 or self.z < 0:
#                 res = 'С отрицательными числами ничего не выйдет!'
#         elif self.x == 0 and self.y != 0 and self.z != 0 or self.x != 0 and self.y == 0 and self.z != 0 or self.x != 0 and self.y == 0 and self.z == 0:
#             res = 'Жаль, но из этого треугольник не сделать.'
#         return res
#
# str = [input(f'Введите отрезок {x+1} >>') for x in range(3)]
#
# for el in str:
#     if el.isdigit():
#         triangle = TriangleChecker(str[0], str[1], str[2])
#         print(triangle.is_triangle())
#     else:
#         print('Нужно вводить только числа!')


'''Write a Python program to create a class representing a shopping cart. Include methods for adding and 
removing items, and calculating the total price'''

#Good one

#
# class Shop_crt:
#     magasin = {'Яблоко': 10,
#                'Манго': 24,
#                'Апельсин': 12,
#                'Клубника': 18,
#                'Груша': 15
#                }
#     total = 0
#
#     def __init__(self, x):
#         self.x = x
#     def add(self):
#         self.total += self.x
#         return self.total
#     def rmv(self):
#         self.total -= self.x
#         return self.total
#
# addition = Shop_crt(4)
# Magasin = addition.magasin
# for el, price in Magasin.items():
#     print(el, ':', price, 'Рублей', ' ', end=' ')
# lst = []
# summa = 0
# product = 0
# print('')
# Shopping = input('Совершать покупку, нажмите клавиша (1) или нажмите любую клавишу для выхода из магазина >>__ ')
# if Shopping == '1':
#     while Shopping == '1':
#         item = input('Напишите наименование товара из корзины --> нажмите Enter / нажмите любую клавишу для выхода из магазина >>__')
#         if item in Magasin:
#             a = Magasin[item]
#             addition = Shop_crt(a)
#             str = input('добавить (1) или убрать (2) >>')
#             if str == '1':
#                 lst.append(item)
#                 summa += addition.add()
#                 product = len(lst)
#                 print(lst)
#             elif str == '2' and item not in lst:
#                 print('Нет данного товара в корзине')
#             elif str == '2' and item in lst:
#                 summa += addition.rmv()
#                 lst.remove(item)
#                 product = len(lst)
#             else:
#                 print('Выбирайте правильную операцию')
#             print(f'Текущая сумма {summa}', f'В корзине: {product} шт.')
#         else:
#             print('У нас нет данного товара')
#             print(f'Сумма к оплате {summa}', f'В корзине: {product} шт.')
#             break
#
# else:
#     print(f'Общая сумма в корзине: {summa}', f'Количество товара : {product}')



#An other good one
#
# class Shop_crt:
#     magasin = {'Яблоко': 10,
#                'Манго': 24,
#                'Апельсин': 12,
#                'Клубника': 18,
#                'Груша': 15
#                }
#     cart = {}
#
#     def __init__(self, x):
#         self.x = x
#
#     def menu(self):
#         print()
#         print('Вывести каталог товаров >> Нажмите 0')
#         print('Если хотите совершить покупку >> Нажмите 1')
#         print('Убрать продукт из корзины >> Нажмите 2')
#         print('Показать корзину Нажимите 3')
#         print('Посчитать общуу стоимость корзины >> Нажимите 3')
#         print('Очистить корзину >> Нажмите 4')
#         print('Закончить покупки и пойди на кассу >> Нажмите 5')
#         print('Уйти из магазина >> Нажмите 6')
#         n = input('>> ')
#         if n == '0':
#             self.katalog()
#         elif n == '1':
#             self.add()
#         elif n == '3':
#             self.show_cart()
#         # elif n == 3:
#         # elif n == 3:
#         # elif n == 3:
#
#     def katalog(self):
#         for el, price in self.magasin.items():
#             print(el, ':', price, 'Рублей')
#         print()
#         n = input('Нажмите Enter кнопку чтобы продолжить: ')
#         Shop_crt.menu(self)
#
#     def add(self):
#         x = input('Что желаете преобрести? \n>> ')
#         if x in self.magasin:
#             y = int(input('Сколько желаете преобрести? \n>> '))
#             if x not in self.cart:
#                 self.cart[x] = y
#             else:
#                 self.cart[x] += y
#         else:
#             print('К сожалению в магазине отсутсвует данный товар')
#         n = input('Желаете приобрести что-то еще? (y/n)\n>> ')
#         if n == 'y':
#             self.add()
#         else:
#             Shop_crt.menu(self)
#
#     def show_cart(self):
#         for el, count in self.cart.items():
#             print(el, ':', count)
#         n = input('Нажмите Enter кнопку чтобы продолжить: ')
#         Shop_crt.menu(self)
#
#
# shop = Shop_crt(1)
# shop.menu()


# an other one
# class Shop_crt:
#
#     unit = 0
#     total = 0
#     def __init__(self, x):
#         self.x = x
#
#     def add(self):
#         self.total += self.x
#         return self.total
#     def rmv(self):
#         self.total -= self.x
#         return self.total
#
# magasin = {'Яблоко': 10,
#                'Манго': 24,
#                'Апельсин': 12,
#                'Клубника': 18,
#                'Груша': 15
#            }
# lst = []
# summa = 0
# product = 0
# print('Нажмите (1) для совершения покупку или любую клашиву для выхода из магазина')
# Shopping = input('Будем совершать покупку? (1) или любая клавиша >> ')
# if Shopping == '1':
#     while Shopping == '1':
#         item = input('Выбирайте товар из корзины. Для совершения покупки нажмите любую клавашу >>')
#         if item in magasin :
#             a = magasin[item]
#             addition = Shop_crt(a)
#             str = input('добавить (1) или убрать (2) >>')
#             if str == '1':
#                 lst.append(item)
#                 summa += addition.add()
#                 product = len(lst)
#                 print(lst)
#             elif str == '2' and item not in lst:
#                 print('Нет данного товара в корзине')
#             elif str == '2' and item in lst:
#                 summa += addition.rmv()
#                 lst.remove(item)
#                 product = len(lst)
#             else:
#                 print('Выбирайте правильную операцию')
#             print(f'Текущая сумма {summa}', f'В корзине: {product} шт.')
#         else:
#            print(f'Сумма к оплате {summa}', f'В корзине: {product} шт.')
#            break
# else:
#     print(f'Общая сумма в корзине: {summa}', f'Количество товара : {product}')


# '''Строки в Питоне сравниваются на основании значений символовю т.е если мы захотим выяснить, что больше Apple или
# Яблоко, - то Яблоко  окажется больше. А все потому, что английская А имеет значение 65(берется из таблицы кодировки)
# , а русская буква Я -1071 (c помощью функции ord()-это можно выяснить). Такое положение дел не устроило Анну. Она
# считает, что строки нужно сравнивать по количеству входящих в них символов. Для этого девушка создала класс RealString
#  и реализовала озвученный инструментарий. Сравнивать между собой можно как объекты класса, так и обычные строки с
#  экземплярами классе RealString. К слову, Анне понадобилось только 3 метода внутри класса(включая __ init__()) для
#  воплощения задуманного'''

# class RealString:

#     def __init__(self, str1, str2):
#         self.str1 = str1
#         self.str2 = str2

#     def length_str(self):
#         print(f'длина строки 1: {len(self.str1)}')
#         print(f'длина строки 2: {len(self.str2)}')

#     def compare_str(self):
#         if len(self.str1) > len(self.str2):
#             print(f'{self.str1} больше чем {self.str2}')
#         elif len(self.str2) > len(self.str1):
#             print(f'{self.str2} больше чем {self.str1}')
#         else:
#             print('Они равные')


# s =input('Введите 2 слова через проблем >>').split(' ')
# real = RealString(s[0], s[1])

# real.length_str()
# real.compare_str()

'''Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник. 
для этого он решил создать класс TriangleChecker, принимающий только положительные числа. С помощью метода is_triangle
() возвращаются следующие значения(в зависимости от ситуации):
- ура, можно построить треугольник
-С отрицательными числами ничего не выйдет!
-Нужно вводить только числа!
- Жаль, но из этого треугольник не сделать.'''

# class TriangleChecker:

#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#     def is_triangle(self):
#         if self.x != 0 and self.y != 0 and self.z != 0:
#           if self.x + self.y >= self.z:
#               res = 'ура, можно построить треугольник'
#               if self.x < 0 or self.y < 0 or self.z < 0:
#                   res = 'С отрицательными числами ничего не выйдет!'
#           else: res = 'Жаль, но из этого треугольник не сделать.'
#         else: res = 'Жаль, но из этого треугольник не сделать.'
#         return res

# def start():
#     try:
#         str = [int(input(f'Введите отрезок {x + 1} >>')) for x in range(3)]
#         str.sort()
#         triangle = TriangleChecker(str[0], str[1], str[2])
#         print(triangle.is_triangle())
#     except ValueError:
#         print('Нужно вводить только числа!')

# start()
# str = [input(f'Введите сторону треугольника {x + 1} >>') for x in range(3)]
# c = True
# for i in range(len(str)):
#   if (str[i].isdigit()) == False:
#     print('Нужно вводить только числа!')
#     c = False
#     break
# if c:
#   triangle = TriangleChecker(int(str[0]), int(str[1]), int(str[2]))
#   print(triangle.is_triangle())

'''Write a Python program to create a class representing a shopping cart. Include methods for adding and 
removing items, and calculating the total price'''


# class Shop_crt:
#   magasin = {'Яблоко': 10,
#              'Манго': 24,
#              'Апельсин': 12,
#              'Клубника': 18,
#              'Груша': 15
#              }
#   total = 0

#   def __init__(self, x):
#       self.x = x
#   def add(self):
#       self.total += self.x
#       return self.total
#   def rmv(self):
#       self.total -= self.x
#       return self.total

# addition = Shop_crt(4)
# Magasin = addition.magasin
# for el, price in Magasin.items():
#   print(el,':', price, 'Рублей', ' ', end=' ')
# lst = []
# summa = 0
# product = 0
# print('')
# Shopping = input('Совершать покупку, нажмите клавиша (1) или нажмите любую клавишу для выхода из магазина >>__ ')
# if Shopping == '1':
#   while Shopping == '1':
#       item = input('Напишите наименование товара из корзины --> нажмите Enter / нажмите любую клавишу для выхода из магазина >>__')
#       if item in Magasin:
#           a = Magasin[item]
#           addition = Shop_crt(a)
#           str = input('добавить (1) или убрать (2) >>')
#           if str == '1':
#               lst.append(item)
#               summa += addition.add()
#               product = len(lst)
#               print(lst)
#           elif str == '2' and item not in lst:
#               print('Нет данного товара в корзине')
#           elif str == '2' and item in lst:
#               summa += addition.rmv()
#               lst.remove(item)
#               product = len(lst)
#           else:
#               print('Выбирайте правильную операцию')
#           print(f'Текущая сумма {summa}', f'В корзине: {product} шт.')
#       else:
#           print('У нас нет данного товара')
#           print(f'Сумма к оплате {summa}', f'В корзине: {product} шт.')
#           break

# else:
#   print(f'Общая сумма в корзине: {summa}', f'Количество товара : {product}')

# #
# class Shop_crt:
#     magasin = {'Яблоко': 10,
#                'Манго': 24,
#                'Апельсин': 12,
#                'Клубника': 18,
#                'Груша': 15
#                }
#     cart = {}
#
#     def __init__(self, x):
#         self.x = x
#
#     def menu(self):
#         print()
#         print('Вывести каталог товаров >> Нажмите 0')
#         print('Если хотите совершить покупку >> Нажмите 1')
#         print('Убрать продукт из корзины >> Нажмите 2')
#         print('Показать корзину >>  Нажимите 3')
#         print('Посчитать общую стоимость корзины >> Нажимите 4')
#         print('Очистить корзину >> Нажмите 5')
#         print('Закончить покупки и пойди на кассу >> Нажмите 6')
#         print('Уйти из магазина >> Нажмите 7')
#         n = input('>> ')
#         if n == '0':
#             self.katalog()
#         elif n == '1':
#             self.add()
#         elif n == '2':
#             self.rmv()
#         elif n == '3':
#             self.show_cart()
#         elif n == '4':
#             self.addition()
#         elif n == '5':
#             self.cleaning()
#         elif n == '6':
#             self.end_shop()
#         elif n == '7':
#             if input('Желаете Выйти из Магазина? (y/n) >> ') != 'y':
#                 Shop_crt.menu(self)
#             else:
#                 print('Спасибо за покупку')
#
#     def katalog(self):
#         for el, price in self.magasin.items():
#             print(el, ':', price, 'Рублей')
#         print()
#         n = input('Нажмите Enter кнопку чтобы продолжить: ')
#         Shop_crt.menu(self)
#
#     def add(self):
#         x = input('Что желаете преобрести? \n>> ')
#         if x in self.magasin:
#             y = int(input('Сколько желаете преобрести? \n>> '))
#             if x not in self.cart:
#                 self.cart[x] = y
#             else:
#                 self.cart[x] += y
#         else:
#             print('К сожалению в магазине отсутсвует данный товар')
#         n = input('Желаете приобрести что-то еще? (y/n)\n>> ')
#         if n == 'y':
#             self.add()
#         else:
#             Shop_crt.menu(self)
#     def rmv(self):
#         x = input('Какой товар желаете убрать из корзины?: >> ')
#         if x not in self.cart.keys():
#             print('Товар отсутствует в корзине')
#             Shop_crt.menu(self)
#         else:
#             y = int(input('Сколько хотите убрать? \n>> '))
#             if self.cart[x] >= y:
#                 self.cart[x] -= y
#             else:
#                 print(f'В корзине {self.cart[x]} товар(ов) ')
#                 self.rmv()
#         Shop_crt.menu(self)
#     def show_cart(self):
#         for el, count in self.cart.items():
#             print(el, ':', count)
#         Shop_crt.menu(self)
#
#     def addition(self):
#         summa = 0
#         for el in self.cart.keys():
#             price = self.magasin[el] * self.cart[el]
#             summa += price
#         print(f'текущая сумма: {summa}')
#         Shop_crt.menu(self)
#
#     def cleaning(self):
#         print('ВЫ действительно хотите очистить корзину?')
#         if input('y/n : >> ') == 'y':
#             self.cart.clear()
#             print('Корзина пустая')
#             Shop_crt.menu(self)
#         else:
#             self.show_cart()
#
#     def end_shop(self):
#         if input('Хотите завершать покупку и создать чек ? y/n >> ') != 'y':
#             Shop_crt.menu(self)
#         else:
#             print(f' В корзине :')
#             summa = 0
#             for el in self.cart.keys():
#                 price = self.magasin[el] * self.cart[el]
#                 summa += price
#             print(f'Итого: {summa}')
#             Shop_crt.menu(self)
#
# shop = Shop_crt(1)
# shop.menu()


#good one
#
# class Shop_crt:
#   magasin = {'Яблоко': 10,
#              'Манго': 24,
#              'Апельсин': 12,
#              'Клубника': 18,
#              'Груша': 15
#              }
#   cart = {}
#
#   def __init__(self, x):
#       self.x = x
#
#   def menu(self):
#       print()
#       print('Вывести каталог товаров >> Нажмите 0')
#       print('Если хотите совершить покупку >> Нажмите 1')
#       print('Убрать продукт из корзины >> Нажмите 2')
#       print('Показать корзину >>  Нажимите 3')
#       print('Посчитать общую стоимость корзины >> Нажимите 4')
#       print('Очистить корзину >> Нажмите 5')
#       print('Закончить покупки и пойди на кассу >> Нажмите 6')
#       print('Уйти из магазина >> Нажмите 7')
#       n = input('>> ')
#       if n == '0':
#           self.katalog()
#       elif n == '1':
#           self.add()
#       elif n == '2':
#           self.rmv()
#       elif n == '3':
#           self.show_cart()
#       elif n == '4':
#           self.addition()
#       elif n == '5':
#           self.cleaning()
#       elif n == '6':
#           self.end_shop()
#       elif n == '7':
#           if input('Желаете Выйти из Магазина? (y/n) >> ') != 'y':
#               Shop_crt.menu(self)
#           else:
#               print('Спасибо за покупку')
#
#   def katalog(self):
#       for el, price in self.magasin.items():
#           print(el, ':', price, 'Рублей')
#       print()
#       n = input('Нажмите Enter кнопку чтобы продолжить: ')
#       Shop_crt.menu(self)
#
#   def add(self):
#       x = input('Что желаете преобрести? \n>> ')
#       if x in self.magasin:
#           y = int(input('Сколько желаете преобрести? \n>> '))
#           if x not in self.cart:
#               self.cart[x] = y
#           else:
#               self.cart[x] += y
#       else:
#           print('К сожалению в магазине отсутсвует данный товар')
#       n = input('Желаете приобрести что-то еще? (y/n)\n>> ')
#       if n == 'y':
#           self.add()
#       else:
#           Shop_crt.menu(self)
#   def rmv(self):
#       x = input('Какой товар желаете убрать из корзины?: >> ')
#       if x not in self.cart.keys():
#           print('Товар отсутствует в корзине')
#           Shop_crt.menu(self)
#       else:
#           y = int(input('Сколько хотите убрать? \n>> '))
#           if self.cart[x] >= y:
#               self.cart[x] -= y
#           else:
#               print(f'В корзине {self.cart[x]} товар(ов) ')
#               self.rmv()
#       n = input('Нажмите Enter кнопку чтобы продолжить: ')
#       Shop_crt.menu(self)
#   def show_cart(self):
#       for el, count in self.cart.items():
#           print(el, ':', count)
#       n = input('Нажмите Enter кнопку чтобы продолжить: ')
#       Shop_crt.menu(self)
#
#   def addition(self):
#       summa = 0
#       for el in self.cart.keys():
#           price = self.magasin[el] * self.cart[el]
#           summa += price
#       print(f'текущая сумма: {summa}')
#       n = input('Нажмите Enter кнопку чтобы продолжить: ')
#       Shop_crt.menu(self)
#
#   def cleaning(self):
#       print('ВЫ действительно хотите очистить корзину?')
#       if input('y/n : >> ') == 'y':
#           self.cart.clear()
#           print('Корзина пустая')
#           n = input('Нажмите Enter кнопку чтобы продолжить: ')
#           Shop_crt.menu(self)
#       else:
#           self.show_cart()
#
#   def end_shop(self):
#       if input('Хотите завершать покупку и создать чек ? y/n >> ') != 'y':
#           Shop_crt.menu(self)
#       else:
#           print(f' В корзине :')
#           self.addition()
#           Shop_crt.menu(self)
#
# shop = Shop_crt(1)
# shop.menu()

# class Cat:
#   def __init__(self, name):
#     self.name = name

#   # def __new__():
#   #   print('new')

#   # def __del__(self):
#   #   print(format(self.name), 'удаление объекта')

#   def __call__(self, r, v):
#     return r<=40 and v <= 5

# abc = Cat('Bob')
# print(abc(33, 4))

'''Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.'''

#
# class Person:
#
#     def __init__(self, name, country, date_of_birth):
#         self._name = name
#         self._country = country
#         self._date_of_birth = date_of_birth
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def counrty(self):
#         return self._country
#
#     @property
#     def date_of_birth(self):
#         return self._date_of_birth
#
#
# person = Person('Bob', 'Maroco', '12.12.00')
# print(person.name)

# def add(self):
#     self.total += self.x
#     return self.total
# def rmv(self):
#     self.total -= self.x
#     return self.total



# scoops = [scoop (flavor) for flavor in ('vanilla', 'choco', 'persi')]
# print(scoops)



# class Beverage:
#
#     def __init__(self, name, temp=75):
#         self.name = name
#         self.temp = temp
#
#     def decript(self):
#         print(f'{self.name} : {self.temp}')
#
# drink_1 = Beverage('Water', 15)
# drink_2 = Beverage('Limonade', 10)
# drink_3 = Beverage('Beer', 5)
# drink_4 = Beverage('Hot water')
# lst = [drink_1, drink_2, drink_3, drink_4]
# for el in lst:
#     el.decript()



# class LogFile:
#
#     def __init__(self, file):
#         self.file = file
#     def open_w_f(self):
#         with open(self.file, 'w+') as f:
#             f.write('Hello world')
#
# lg = LogFile('text_lf.txt')
# lg.open_w_f()

# class Scoop:
#     def __init__(self, flavor):
#         self.flavor = flavor
#
# class Bowl:
#     def __init__(self):
#         self.scoops = []
#
#     def add_scoops(self, *new_scoops):
#         for one_scoop in new_scoops:
#             self.scoops.append(one_scoop)
#     def __repr__(self):
#        return '\n'.join(s.flavor for s in self.scoops)
#
# s1 = Scoop('Choco')
# s2 = Scoop('vanilla')
# s3 = Scoop('persimmon')
#
# b = Bowl()
# b.add_scoops(s1.flavor, s2.flavor)
# b.add_scoops(s3.flavor)
# print(b.__dict__.items())
# print(b.scoops)
# print(s1.__dict__)
# print(s1.flavor)



#
# class Book:
#
#     def __init__(self, name, autor, price, width):
#         self.name = name
#         self.autor = autor
#         self.price = price
#         self.width = width
#
# class Shelf:
#
#     opt_w = 50
#
#     def __init__(self):
#         self.books = []
#         self.prices = []
#         self.writers = []
#         self.widths = []
#
#     def add_book(self, *args):
#         for book in args:
#             self.books.append(book)
#
#     def total_price(self, *prices):
#         for price in prices:
#             self.prices.append(price)
#         return sum(self.prices)
#
#     def shelf_has_book(self, *writers):
#         c = False
#         x = input('Is there author?: >> ')
#         for writer in writers:
#             self.writers.append(writer)
#         if x in self.writers:
#             c = True
#         return c
#
#     def total_width(self, *widths):
#         for width in widths:
#             self.widths.append(width)
#         if sum(self.widths) > self.opt_w:
#             raise ValueError('No more places in shelf')
#         else:
#             return f'Width of books in shelf {sum(self.widths)}'
#
#
#
# b1 = Book('war and peace', 'l.tolstoi', 25, 10)
# b2 = Book('Croco a luwozi', 'zamenga', 14, 7)
# b3 = Book('Learnig Python', 'P.Asumani', 42, 8)
# b4 = Book('war and peace 2', 'l.tolstoi', 30, 10)
# s = Shelf()
# s.add_book(b1.__dict__, b2.__dict__, b3.__dict__, b4.__dict__)
# s.total_price(b1.price, b2.price, b3.price, b4.price)
# s.shelf_has_book(b1.autor, b2.autor, b3.autor, b4.autor)
# s.total_width(b1.width, b2.width, b3.width, b4.width)
#
# print(s.__dict__.items())
# print(s.add_book())
# print(f'Total price : {s.total_price()}')
# print(s.shelf_has_book())
# print(s.total_width())


# class Person:
#
#      population = 0
#
#      def __init__(self):
#          Person.population += 1
#
#      def __del__(self):
#          Person.population -= 1
#
# p1 = Person()
#
# print(p1.population)
# print(Person.population)
# print(p1.population)


# class Transaction:
#
#     balance = 1500
#
#     def __init__(self, x):
#         Transaction.balance += x
#
# t1 = Transaction(100)
# print(Transaction.balance)
# t2 = Transaction(-500)
# print(Transaction.balance)
# t3 = Transaction(-500)
# print(Transaction.balance)

#


#
# class Envelope:
#
#     weight = 10.2
#     Max_p = weight*10
#     was_sent = False
#
#     def __init__(self, x=0):
#         self.x = x
#     def send(self):
#         if self.x >= self.Max_p:
#             Envelope.was_sent = True
#             print('Письмо отправлено')
#         else:
#             Envelope.was_sent = False
#             print('Письмо не отправлено')
#     def add_postage(self, y):
#         self.x = self.x + y
#         return f'Количество марок : {self.x}'
#
#     def postage_needed(self):
#         if self.Max_p - self.x > 0:
#             print(f'Для отправления письмо нужно : {self.Max_p - self.x} марок')
#         else:
#             print('Достаточно количество марок для отправления ')
#
# class BigEnvelope(Envelope):
#     Max_p = Envelope.weight * 15
#
#
# envelope = Envelope()
# b_envelope = BigEnvelope()
# print(envelope.__dict__)
# print(envelope.add_postage(153))
# envelope.postage_needed()
# envelope.send()
# print(envelope.Max_p)
# print(b_envelope.x)
#
# print(b_envelope.__dict__)
# print(b_envelope.add_postage(153))
# b_envelope.postage_needed()
# b_envelope.send()
# print(b_envelope.Max_p)
# print(b_envelope.x)
#

# class Phone:
#
#     def __init__(self, name):
#         self.name = name
#
#     def dial(self):
#         print(f'Calling : {self.name.upper()}')
# class Smartphone(Phone):
#
#     def __init__(self, name, my_app):
#         super().__init__(name)
#         self.my_app = my_app
#     def run_app(self):
#         print(f'Running application: {self.my_app}')
#
# class Iphone(Smartphone):
#     def dial(self):
#         print(f'Calling: {self.name.lower()}')
#
# phone = Phone('Mommy')
# smartphone = Smartphone('Mommy', 'Google Chrome')
# iphone = Iphone('Mommy', 'Google Chrome')
# phone.dial()
# smartphone.dial()
# smartphone.run_app()
# iphone.dial()
# iphone.run_app()


# class Bread:
#
#     dict_b = {'calorie': 0.3,
#     'protein': 0.2,
#     'vitamine': 0.15,
#     'sugar': 0.15,
#     'gras': 0.2
#      }
#
#     def __init__(self, prt):
#         self.prt = prt
#         self.key = []
#         self.value_prt = []
#
#     def get_nutrition(self):
#         for key in self.dict_b.keys():
#             self.key.append(key)
#         for value in self.dict_b.values():
#             self.value_prt.append(value*self.prt)
#         return dict(zip(self.key, self.value_prt))
#
#
#
#
# bread = Bread(7)
# print(bread.__dict__)
# print(bread.dict_b)
# print(bread.get_nutrition())


#
# class Bank:
#
#     services = ['Your balance ->Press "1"',
#                 'Deposit -> Press "2" ',
#                 'Withdraw money -> Press "3" ',
#                 'New credit account -> Press "4" ',
#                 'To view your credit balance -> Press "5"',
#                 'Your withdraw in credit account -> Press "6"',
#                 'To Deposit in credit account -> Press "7" ',
#                 'To close your credit balance -> Press "8" ',
#                 ' For services -> Press "9" '
#                 ]
#     def __init__(self, name, age, pswrd):
#         self.validate_age(age)
#         self.validate_pswrd(pswrd)
#         self.__name = name
#         self.__age = age
#         self.__pswrd = pswrd
#     def creating_acount(self):
#         print('______________________________________________')
#         print(f'Hello Mr(Ms) {self.__name}, Welcome to our Bank!')
#         print(f'Your balance :->> {self.balance}$')
#         self.main_serv()
#         self.serVices()
#     def serVices(self):
#         for service in self.services:
#             print(service)
#         print('______________________________________________')
#         n = input('Choose your service here : -> ')
#         if n == '1':
#             print(f'Your balance: {self.balance}$')
#             print(input('Press ->"ENTER" to continue" >>'))
#             self.serVices()
#             print('______________________________________________')
#         elif n == '2':
#             if int(input('Enter your password : ->')) == self.__pswrd:
#                 summa = int(input('tape the sum here ->'))
#                 print(f'Your balance : {self.deposite(summa)}$')
#                 self.main_serv()
#                 self.serVices()
#             else:
#                 print('!!!Incorrect password !!!')
#                 self.main_serv()
#                 self.serVices()
#
#         elif n == '3':
#             if int(input('Enter your password : ->')) == self.__pswrd:
#                 summa = int(input('tape the sum to withdraw ->'))
#                 print(f'Your balance : {self.withdraw(summa)}$')
#                 self.main_serv()
#                 self.serVices()
#             else:
#                 print('!!!Incorrect password !!!')
#                 self.main_serv()
#                 self.serVices()
#         elif n == '4':
#             if bank_ac_1.counter < 1:
#                 bank_ac_1.credit_creation()
#
#             else:
#                 print('You have already created a account')
#             self.main_serv()
#             self.serVices()
#         elif n == '5':
#             bank_ac_1.view_cr_bal()
#             self.main_serv()
#             self.serVices()
#
#         elif n == '6':
#             if bank_ac_1.counter == 0:
#                 print('You are about to create an credit account, and it will creating automatically')
#                 if int(input('Enter your password : ->')) == self.__pswrd:
#                     summa = int(input('tape the sum to withdraw ->'))
#                     bank_ac_1.credit_wd(summa)
#                     bank_ac_1.counter = 1
#                     self.main_serv()
#                     self.serVices()
#
#                 else:
#                     print('!!!Incorrect password !!!')
#                     self.main_serv()
#                     self.serVices()
#
#             else:
#                 if int(input('Enter your password : ->')) == self.__pswrd:
#                     summa = int(input('tape the sum to withdraw ->'))
#                     bank_ac_1.credit_wd(summa)
#                     self.main_serv()
#                     self.serVices()
#                 else:
#                     print('!!!Incorrect password !!!')
#                     self.main_serv()
#                     self.serVices()
#
#
#         elif n == '7':
#             if bank_ac_1.counter == 0:
#                 print('You are about an credit account, or it will creating automatically')
#                 if int(input('Enter your password : ->')) == self.__pswrd:
#                     summa = int(input('tape the sum to deposit ->'))
#                     bank_ac_1.deposit_credit(summa)
#                     bank_ac_1.counter = 1
#                     self.main_serv()
#                     self.serVices()
#                 else:
#                     print('!!!Incorrect password !!!')
#                     self.main_serv()
#                     self.serVices()
#             else:
#                 if int(input('Enter your password : ->')) == self.__pswrd:
#                     summa = int(input('tape the sum to deposit ->'))
#                     bank_ac_1.deposit_credit(summa)
#                     bank_ac_1.counter = 1
#                     self.main_serv()
#                     self.serVices()
#                 else:
#                     print('!!!Incorrect password !!!')
#                     self.main_serv()
#                     self.serVices()
#         elif n == '8':
#             bank_ac_1.close_cred_bal()
#             self.main_serv()
#             self.serVices()
#         else:
#             if input('Press the key-> "ENTER" to leave') == '':
#                 print('!!!Goodbye!!! See you soon.!')
#             else:
#                 self.main_serv()
#                 self.serVices()
#
#     def deposite(self, summa):
#         self.balance += summa
#         return self.balance
#
#     def withdraw(self, summa):
#         if self.balance - summa < 0:
#             print('Less money in balance')
#             return self.balance
#         else:
#             return self.balance - summa
#
#     @classmethod
#     def validate_pswrd(cls, pswrd):
#        if type(pswrd) != int:
#            raise TypeError('The password must be a number')
#
#        pwd = str(pswrd)
#        if len(pwd) != 4:
#            raise TypeError('The password must be a number with 4 chars')
#
#     @classmethod
#     def validate_age(cls, age):
#         if age < 18 or age >120 :
#             raise TypeError('Your must be older then 18 years, and less the 120 years old')
#     @staticmethod
#     def main_serv():
#         print('______________________________________________')
#         print(input('Press ->"ENTER" to continue" >>'))
#
#     @staticmethod
#     def avoid():
#         print('Enter correct data: For help, contact our service')
#         print('Your password must be a number with 4 characters')
#         print('You must be older then 18-years old or less then 120-years old')
#
#
# class creditation:
#     percent = 0.17
#     counter = 0
#     def credit_creation(self):
#         print(f"You've just created a credit balance! Thank for believing in us")
#         print(f'Your credit balance : {self.credit_balance}$')
#         self.counter += 1
#     def credit_wd(self, summa):
#             money_1 = self.credit_balance - (summa + (summa * self.percent))
#             self.credit_balance = money_1
#             print(f'Your credit balance : {self.credit_balance}$, percent :{self.percent} ')
#
#     def deposit_credit(self, cash):
#         money_2 = self.credit_balance + cash
#         self.credit_balance = money_2
#
#         print(f' Your credit balance {self.credit_balance}$')
#     def view_cr_bal(self):
#         print(f'Your credit balance : {self.credit_balance }$')
#
#     def close_cred_bal(self):
#         if self.credit_balance < 0:
#             print(f'For closing your credit balance, you must deposit{self.credit_balance}$')
#             print('Press the key -> "7" to deposit')
#         else:
#             print(f'Your credit balance is positif,  your balance : {self.credit_balance}$')
#
#
#
# class Bank_acount_1(Bank, creditation):
#     credit_balance = 0
#     balance = 0
#     neg_bal = 0
#
#
# class Bank_acount_2(Bank, creditation):
#     credit_balance = 0
#     balance = 0
#     neg_bal = 0
#
#
# counter = 0
# while counter < 3:
#     try:
#         print('___________________________________________')
#         print('For creating acount, fill the case below:')
#         print('___________________________________________')
#         Bank.avoid()
#         print('___________________________________________')
#         name = input(f'Enter your name ->>')
#         age = int(input(f'Enter your age ->>'))
#         pswrd = int(input(f'Create your password. Your password must be a number with 4 characters  ->>'))
#         bank_ac_1 = Bank_acount_1(name, age, pswrd)
#         # bank_ac_2 = Bank_acount_2()
#         bank_ac_1.creating_acount()
#         counter = 3
#     except ValueError:
#         print('Incorrect format data')
#         Bank.avoid()
#         counter += 1
#
#
# # # bank_ac_2.creating_acount()
# # print(bank_ac_1.name)
# # print(bank_ac_1.ID)
# # print(bank_ac_1.status(-10))
# # print(bank_ac_1.neg_bal)
# # print(bank_ac_1.credit(1000))
# # bank_ac_1.clear_perc(1000)
# # # print('________________________________')
# # # print(bank_ac_2.name)
# # # print(bank_ac_2.ID)
# # # print(bank_ac_2.neg_bal)
# # # print(bank_ac_2.credit(1000))
# # # bank_ac_2.clear_perc(1000)

#
# class Bank:
#
# # Главный класс банка и его атрибут services
#
#     services = ['To show your balance -> Press "1"',
#                 'Deposition -> Press "2" ',
#                 'Withdraw -> Press "3" ',
#                 'Creating credit account -> Press "4" ',
#                 'To show your credit balance -> Press "5"',
#                 'Withdraw in credit account -> Press "6"',
#                 'Deposition in credit account -> Press "7" ',
#                 'To close your credit balance -> Press "8" ',
#                 'To transfer credit balance to your own card -> Press "9" ',
#                 ' To quit -> Press "Any key" '
#                 ]
# # Инициализатор класса банка
#
#     def __init__(self, name, age, pswrd):
#         self.validate_age(age)
#         self.validate_pswrd(pswrd)
#         self.__name = name
#         self.__age = age
#         self.__pswrd = pswrd
#
# # Методы класса
#     def creating_acount(self): # Метод создания аккаунта
#         print('______________________________________________')
#         print(f'Hello Mr(Ms) {self.__name}, Welcome to our Bank!')
#         print(f'Your balance :->> {self.balance}$')
#         self.main_serv()
#         self.serVices()
#     def serVices(self): # Метод низкоуровний, запускающий другие методы
#         for service in self.services:
#             print(service)
#         print('______________________________________________')
#         n = input('Choose the number of service or Press any key to quit: -> ')
#         if n == '1':
#             print(f'Your balance: {self.balance}$')
#             print(input('Press ->"ENTER" to continue" >>'))
#             self.serVices()
#             print('______________________________________________')
#         elif n == '2':
#             if int(input('Enter your password : ->')) == self.__pswrd:
#                 summa = int(input('tape the sum here ->'))
#                 print(f'Your balance : {self.deposite(summa)}$')
#                 self.main_serv()
#                 self.serVices()
#             else:
#                 print('!!!Incorrect password !!!')
#                 self.main_serv()
#                 self.serVices()
#
#         elif n == '3':
#             if int(input('Enter your password : ->')) == self.__pswrd:
#                 summa = int(input('tape the sum to withdraw ->'))
#                 print(f'Your balance : {self.withdraw(summa)}$')
#                 self.main_serv()
#                 self.serVices()
#             else:
#                 print('!!!Incorrect password !!!')
#                 self.main_serv()
#                 self.serVices()
#         elif n == '4':
#             if bank_ac_1.counter < 1:
#                 bank_ac_1.credit_creation()
#
#             else:
#                 print('You have already created a account')
#             self.main_serv()
#             self.serVices()
#         elif n == '5':
#             bank_ac_1.view_cr_bal()
#             self.main_serv()
#             self.serVices()
#
#         elif n == '6':
#             if bank_ac_1.counter == 0:
#                 print('You are about to create a credit account, and it will creating automatically')
#                 if int(input('Enter your password : ->')) == self.__pswrd:
#                     summa = int(input('tape the sum to withdraw ->'))
#                     bank_ac_1.credit_wd(summa)
#                     bank_ac_1.counter = 1
#                     self.main_serv()
#                     self.serVices()
#
#                 else:
#                     print('!!!Incorrect password !!!')
#                     self.main_serv()
#                     self.serVices()
#
#             else:
#                 if int(input('Enter your password : ->')) == self.__pswrd:
#                     summa = int(input('tape the sum to withdraw ->'))
#                     bank_ac_1.credit_wd(summa)
#                     self.main_serv()
#                     self.serVices()
#                 else:
#                     print('!!!Incorrect password !!!')
#                     self.main_serv()
#                     self.serVices()
#
#
#         elif n == '7':
#             if bank_ac_1.counter == 0:
#                 print('You are about to create a credit account,  it will creating automatically')
#                 if int(input('Enter your password : ->')) == self.__pswrd:
#                     summa = int(input('tape the sum to deposit ->'))
#                     bank_ac_1.deposit_credit(summa)
#                     bank_ac_1.counter = 1
#                     self.main_serv()
#                     self.serVices()
#                 else:
#                     print('!!!Incorrect password !!!')
#                     self.main_serv()
#                     self.serVices()
#             else:
#                 if int(input('Enter your password : ->')) == self.__pswrd:
#                     summa = int(input('tape the sum to deposit ->'))
#                     bank_ac_1.deposit_credit(summa)
#                     bank_ac_1.counter = 1
#                     self.main_serv()
#                     self.serVices()
#                 else:
#                     print('!!!Incorrect password !!!')
#                     self.main_serv()
#                     self.serVices()
#         elif n == '8':
#             bank_ac_1.close_cred_bal()
#             self.main_serv()
#             self.serVices()
#
#         elif n == '9':
#             if creditation.wd_from_credit(bank_ac_1) > 0:
#                 money_4 = self.balance + creditation.wd_from_credit(bank_ac_1)
#                 print(f' After transaction! your balance : {money_4}')
#                 self.balance = money_4
#                 bank_ac_1.credit_balance = 0
#                 self.main_serv()
#                 self.serVices()
#             else:
#                 print('Your credit balance is negative or has no money !!SORRY!!')
#                 self.main_serv()
#                 self.serVices()
#
#         else:
#             if input('Press "ENTER" key to leave') == '':
#                 print('!!!Goodbye!!! See you soon.!')
#             else:
#                 self.main_serv()
#                 self.serVices()
#
#     def deposite(self, summa): # Метод внесения денег
#         money_1 = self.balance + summa
#         self.balance = money_1
#         return self.balance
#
#     def withdraw(self, summa): # Метод снятия денег
#         if self.balance - summa < 0:
#             print('Less money in balance')
#             return self.balance
#         else:
#             money_2 = self.balance - summa
#             self.balance = money_2
#             return self.balance
#
#     @classmethod # Метод класса валидатор
#     def validate_pswrd(cls, pswrd):
#        if type(pswrd) != int:
#            raise TypeError('The password must be a number')
#
#        pwd = str(pswrd)
#        if len(pwd) != 4:
#            raise TypeError('The password must be a number with 4 chars')
#
#     @classmethod # Метод класса валидатор
#     def validate_age(cls, age):
#         if age < 18 or age >120 :
#             raise TypeError('Your must be older then 18 years, and less the 120 years old')
#     @staticmethod  # статич.Метод класса
#     def main_serv():
#         print('______________________________________________')
#         print(input('Press ->"ENTER" to continue" >>'))
#
#     @staticmethod  # статич.Метод класса
#     def avoid():
#         print('Enter correct data: For help, contact our service')
#         print('Your password must be a number with 4 characters')
#         print('You must be older then 18-years old or less then 120-years old')
#
#
# # Дополнительный  класс, отдел кредита
# class creditation:
#     percent = 0.17
#     counter = 0
#     def credit_creation(self): # Метод для создания кредита
#         print(f"You've just created a credit balance! Thank for believing in us")
#         print(f'Your credit balance : {self.credit_balance}$')
#         self.counter += 1
#     def credit_wd(self, summa): # Метод для оформления кредита и снятия денег
#             money_1 = self.credit_balance - (summa + (summa * self.percent))
#             self.credit_balance = money_1
#             print(f'Your credit balance : {self.credit_balance}$, percent : 17% ')
#     def deposit_credit(self, cash): # Метод для пополнениябаланса кредита
#         money_2 = self.credit_balance + cash
#         self.credit_balance = money_2
#
#         print(f' Your credit balance {self.credit_balance}$')
#     def view_cr_bal(self): # Метод для просмотра баланса кредита
#         print(f'Your credit balance : {self.credit_balance }$')
#     def wd_from_credit(self): # Метод для трансфера денег с баланса кредита
#         if self.credit_balance >= 0:
#             money_3 = self.credit_balance
#             return money_3
#         else:
#             return self.credit_balance == 0
#     def close_cred_bal(self):
#         if self.credit_balance < 0:
#             print(f'For closing your credit balance, you must deposit{self.credit_balance}$')
#             print('Press the key -> "7" to deposit')
#         else:
#             print(f'Your credit balance is positive,  your balance : {self.credit_balance}$')
# class Bank_acount_1(Bank, creditation):
#     credit_balance = 0
#     balance = 0
#     neg_bal = 0
#
# # class Bank_acount_2(Bank, creditation):
# #     credit_balance = 0
# #     balance = 0
# #     neg_bal = 0
# counter = 0
# while counter < 3:
#     try:
#         print('___________________________________________')
#         print('For creating account, fill the case below:')
#         print('___________________________________________')
#         Bank.avoid()
#         print('___________________________________________')
#         name = input(f'Enter your name ->>')
#         age = int(input(f'Enter your age ->>'))
#         pswrd = int(input(f'Create your password. Your password must be a number with 4 characters  ->>'))
#         bank_ac_1 = Bank_acount_1(name, age, pswrd)
#         # bank_ac_2 = Bank_acount_2()
#         bank_ac_1.creating_acount()
#         counter = 3
#     except TypeError:
#         print('Incorrect format data')
#         Bank.avoid()
#         counter += 1
#
#
#
#
#
#
# # Good one final
# '''Bank Account — простая программа для симуляции банка с функциями создания счета, снятия и внесения денег, выдачей кредита и его погашением.Добавьте несколько отделений банка главное и дочернее, а так же возможность авторизации с последующей смены параметров текущих ставок.'''
#
# # Главный класс банка и его атрибут services
# class Bank:
#     services = ['To show your balance -> Press "1"',
#                 'Deposition -> Press "2" ',
#                 'Withdraw -> Press "3" ',
#                 'Creating credit account -> Press "4" ',
#                 'To show your credit balance -> Press "5"',
#                 'Withdraw in credit account -> Press "6"',
#                 'Deposition in credit account -> Press "7" ',
#                 'To close your credit balance -> Press "8" ',
#                 'To transfer credit balance to your own card -> Press "9" ',
#                 ' To quit -> Press "Any key" '
#                 ]
# # Инициализатор класса банка
#
#     def __init__(self, name, age, pswrd):
#         self.validate_age(age)
#         self.validate_pswrd(pswrd)
#         self.__name = name
#         self.__age = age
#         self.__pswrd = pswrd
#
# # Методы класса
#     def creating_acount(self): # Метод создания аккаунта
#         print('______________________________________________')
#         print(f'Hello Mr(Ms) {self.__name}, Welcome to our Bank!')
#         print(f'Your balance :->> {self.balance}$')
#         self.main_serv()
#         self.serVices()
#     def serVices(self): # Метод низкоуровний, запускающий другие методы
#         for service in self.services:
#             print(service)
#         print('______________________________________________')
#         n = input('Choose the number of service or Press any key to quit: -> ')
#         if n == '1':
#             print(f'Your balance: {self.balance}$')
#             print(input('Press ->"ENTER" to continue" >>'))
#             self.serVices()
#             print('______________________________________________')
#         elif n == '2':
#             if int(input('Enter your password : ->')) == self.__pswrd:
#                 summa = int(input('tape the sum here ->'))
#                 print(f'Your balance : {self.deposite(summa)}$')
#                 self.main_serv()
#                 self.serVices()
#             else:
#                 print('!!!Incorrect password !!!')
#                 self.main_serv()
#                 self.serVices()
#
#         elif n == '3':
#             if int(input('Enter your password : ->')) == self.__pswrd:
#                 summa = int(input('tape the sum to withdraw ->'))
#                 print(f'Your balance : {self.withdraw(summa)}$')
#                 self.main_serv()
#                 self.serVices()
#             else:
#                 print('!!!Incorrect password !!!')
#                 self.main_serv()
#                 self.serVices()
#         elif n == '4':
#             if bank_ac_1.counter < 1:
#                 bank_ac_1.credit_creation()
#
#             else:
#                 print('You have already created a account')
#             self.main_serv()
#             self.serVices()
#         elif n == '5':
#             bank_ac_1.view_cr_bal()
#             self.main_serv()
#             self.serVices()
#
#         elif n == '6':
#             if bank_ac_1.counter == 0:
#                 print('You are about to create a credit account, and it will creating automatically')
#                 if int(input('Enter your password : ->')) == self.__pswrd:
#                     summa = int(input('tape the sum to withdraw ->'))
#                     bank_ac_1.credit_wd(summa)
#                     bank_ac_1.counter = 1
#                     self.main_serv()
#                     self.serVices()
#
#                 else:
#                     print('!!!Incorrect password !!!')
#                     self.main_serv()
#                     self.serVices()
#
#             else:
#                 if int(input('Enter your password : ->')) == self.__pswrd:
#                     summa = int(input('tape the sum to withdraw ->'))
#                     bank_ac_1.credit_wd(summa)
#                     self.main_serv()
#                     self.serVices()
#                 else:
#                     print('!!!Incorrect password !!!')
#                     self.main_serv()
#                     self.serVices()
#
#
#         elif n == '7':
#             if bank_ac_1.counter == 0:
#                 print('You are about to create a credit account,  it will creating automatically')
#                 if int(input('Enter your password : ->')) == self.__pswrd:
#                     summa = int(input('tape the sum to deposit ->'))
#                     bank_ac_1.deposit_credit(summa)
#                     bank_ac_1.counter = 1
#                     self.main_serv()
#                     self.serVices()
#                 else:
#                     print('!!!Incorrect password !!!')
#                     self.main_serv()
#                     self.serVices()
#             else:
#                 if int(input('Enter your password : ->')) == self.__pswrd:
#                     summa = int(input('tape the sum to deposit ->'))
#                     bank_ac_1.deposit_credit(summa)
#                     bank_ac_1.counter = 1
#                     self.main_serv()
#                     self.serVices()
#                 else:
#                     print('!!!Incorrect password !!!')
#                     self.main_serv()
#                     self.serVices()
#         elif n == '8':
#             bank_ac_1.close_cred_bal()
#             self.main_serv()
#             self.serVices()
#
#         elif n == '9':
#             if creditation.wd_from_credit(bank_ac_1) > 0:
#                 money_4 = self.balance + creditation.wd_from_credit(bank_ac_1)
#                 print(f' After transaction! your balance : {money_4}')
#                 self.balance = money_4
#                 bank_ac_1.credit_balance = 0
#                 self.main_serv()
#                 self.serVices()
#             else:
#                 print('Your credit balance is negative or has no money !!SORRY!!')
#                 self.main_serv()
#                 self.serVices()
#
#         else:
#             if input('Press "ENTER" key to leave') == '':
#                 print('!!!Goodbye!!! See you soon.!')
#             else:
#                 self.main_serv()
#                 self.serVices()
#
#     def deposite(self, summa): # Метод внесения денег
#         money_1 = self.balance + summa
#         self.balance = money_1
#         return self.balance
#
#     def withdraw(self, summa): # Метод снятия денег
#         if self.balance - summa < 0:
#             print('Less money in balance')
#             return self.balance
#         else:
#             money_2 = self.balance - summa
#             self.balance = money_2
#             return self.balance
#
#     @classmethod # Метод класса валидатор
#     def validate_pswrd(cls, pswrd):
#        if type(pswrd) != int:
#            raise TypeError('The password must be a number')
#
#        pwd = str(pswrd)
#        if len(pwd) != 4:
#            raise TypeError('The password must be a number with 4 chars')
#
#     @classmethod # Метод класса валидатор
#     def validate_age(cls, age):
#         if age < 18 or age >120 :
#             raise TypeError('Your must be older then 18 years, and less the 120 years old')
#     @staticmethod  # статич.Метод класса
#     def main_serv():
#         print('______________________________________________')
#         print(input('Press ->"ENTER" to continue" >>'))
#
#     @staticmethod  # статич.Метод класса
#     def avoid():
#         print('Enter correct data: For help, contact our service')
#         print('Your password must be a number with 4 characters')
#         print('You must be older then 18-years old or less then 120-years old')
#
#
# # Дополнительный  класс, отдел кредита
# class creditation:
#     percent = 0.17
#     counter = 0
#     def credit_creation(self): # Метод для создания кредита
#         print(f"You've just created a credit balance! Thank for believing in us")
#         print(f'Your credit balance : {self.credit_balance}$')
#         self.counter += 1
#     def credit_wd(self, summa): # Метод для оформления кредита и снятия денег
#             money_1 = self.credit_balance - (summa + (summa * self.percent))
#             self.credit_balance = money_1
#             print(f'Your credit balance : {self.credit_balance}$, percent : 17% ')
#     def deposit_credit(self, cash): # Метод для пополнениябаланса кредита
#         money_2 = self.credit_balance + cash
#         self.credit_balance = money_2
#
#         print(f' Your credit balance {self.credit_balance}$')
#     def view_cr_bal(self): # Метод для просмотра баланса кредита
#         print(f'Your credit balance : {self.credit_balance }$')
#     def wd_from_credit(self): # Метод для трансфера денег с баланса кредита
#         if self.credit_balance >= 0:
#             money_3 = self.credit_balance
#             return money_3
#         else:
#             return self.credit_balance == 0
#     def close_cred_bal(self):
#         if self.credit_balance < 0:
#             print(f'For closing your credit balance, you must deposit{self.credit_balance}$')
#             print('Press the key -> "7" to deposit')
#         else:
#             print(f'Your credit balance is positive,  your balance : {self.credit_balance}$')
#
#
# class Bank_acount_1(Bank, creditation):
#     credit_balance = 0
#     balance = 0
#     neg_bal = 0
#
#
# # class Bank_acount_2(Bank, creditation):
# #     credit_balance = 0
# #     balance = 0
# #     neg_bal = 0
# counter = 0
# while counter < 3:
#     try:
#         print('___________________________________________')
#         print('For creating account, fill the case below:')
#         print('___________________________________________')
#         Bank.avoid()
#         print('___________________________________________')
#         name = input(f'Enter your name ->>')
#         age = int(input(f'Enter your age ->>'))
#         pswrd = int(input(f'Create your password. Your password must be a number with 4 characters  ->>'))
#         bank_ac_1 = Bank_acount_1(name, age, pswrd)
#         # bank_ac_2 = Bank_acount_2()
#         bank_ac_1.creating_acount()
#         counter = 3
#     except TypeError:
#         print('1Incorrect format data')
#         Bank.avoid()
#         counter += 1
#     except ValueError:
#         print('2Incorrect format data')
#         Bank.avoid()
#         counter += 1

#
# class Animal:
#
#     def __init__(self, species, color):
#         self.species = species
#         self.color = color
#
#     def __repr__(self):
#         return f'{self.species},{self.color}, {self.number_of_lg} leg(s), {self.sonor}'
#
# class ZeroleggedAnimal(Animal):
#     number_of_lg = 0
#
#     def __init__(self, species, color, sonor):
#         super().__init__(species, color)
#         self.sonor = sonor
#
# class TwoleggedAnimal(Animal):
#     number_of_lg = 2
#
#     def __init__(self, species, color, sonor):
#         super().__init__(species, color)
#         self.sonor = sonor
#
#
# class FourleggedAnimal(Animal):
#     number_of_lg = 4
#
#     def __init__(self, species, color, sonor):
#         super().__init__(species, color)
#         self.sonor = sonor
#
# snake = ZeroleggedAnimal('Snake', 'balck', 'ssss_')
# human = TwoleggedAnimal('Human', 'Brown', 'Hello')
# dog = FourleggedAnimal('Dog', 'white', 'wooff')
# sheep = FourleggedAnimal('Sheep', 'black', 'beee')
# print(str(snake))
# print(str(human))
# print(str(dog))
# print(str(sheep))

#
#
# class Animal:
#
#     def __init__(self, species, color, number_of_lg ):
#         self.species = species
#         self.color = color
#         self.number_of_lg = number_of_lg
#         print(f'{self.species},{self.color}, {self.number_of_lg} leg(s)')
#
# class ZeroleggedAnimal(Animal):
#     def __init__(self, species, color):
#         super().__init__(species, color, 0)
#
#
# class TwoleggedAnimal(Animal):
#
#     def __init__(self, species, color):
#         super().__init__(species, color, 2)
#
#
#
# class FourleggedAnimal(Animal):

#     def __init__(self, species, color,):
#         super().__init__(species, color, 4)
#
#
# snake = ZeroleggedAnimal('Snake', 'balck')
# Human = TwoleggedAnimal('Human', 'Brown')
# dog = FourleggedAnimal('Dog', 'white')
# sheep = FourleggedAnimal('Sheep', 'black')
#
#
# class Animal:
#     def __init__(self, species, color, nbr_leg):
#         self.species = species
#         self.color = color
#         self.nbr_leg = nbr_leg
#
#     def __repr__(self):
#         return f'{self.color}, {self.species}, {self.nbr_leg} legs'
#
# class Wolf(Animal):
#     def __init__(self, color, species):
#         super().__init__(color,species, 4)
#
# class Sheep(Animal):
#     def __init__(self, color, species):
#         super().__init__(color, species, 4)
#
# class Snake(Animal):
#     def __init__(self, color, species):
#         super().__init__(color, species, 0)
#
# class Parrot(Animal):
#     def __init__(self, color, species):
#         super().__init__(color, species, 2)
#
# class Cage:
#     def __init__(self, id):
#         self.id = id
#         self.animals = []
#
#     def add_animals(self, *animals):
#         for one in animals:
#             self.animals.append(one)
#
#     def __repr__(self):
#         output = f'Cage {self.id} \n'
#         output += '\n'.join('\t' + str(animal) for animal in self.animals)
#
#         return output
#
# wolf = Wolf('black', 'wolf')
# sheep = Sheep('white', 'sheep')
# snake = Snake('brown', 'snake')
# parrot = Parrot('green', 'parrot')
#
# c1 = Cage(1)
# c1.add_animals(wolf, sheep)
# c2 = Cage(2)
# c2.add_animals(snake, parrot)
#
# print(c1)
# print(c2)

#
# class Animal:
#     def __init__(self, species, color, nbr_leg):
#         self.species = species
#         self.color = color
#         self.nbr_leg = nbr_leg
#
#     def __repr__(self):
#         return f'{self.color}, {self.species}, {self.nbr_leg} legs'
#
# class Wolf(Animal):
#     def __init__(self, color, species):
#         super().__init__(color,species, 4)
#
# class Sheep(Animal):
#     def __init__(self, color, species):
#         super().__init__(color, species, 4)
#
# class Snake(Animal):
#     def __init__(self, color, species):
#         super().__init__(color, species, 0)
#
# class Parrot(Animal):
#     def __init__(self, color, species):
#         super().__init__(color, species, 2)
#
# class Cage:
#     place = 3
#     def __init__(self, id):
#         self.id = id
#         self.animals = []
#
#     def add_animals(self, *animals):
#         if len(animals) <= self.place:
#             for one in animals:
#                 self.animals.append(one)
#         else:
#             print('No places')
#
#     def __repr__(self):
#         output = f'Cage {self.id} \n'
#         output += '\n'.join('\t' + str(animal) for animal in self.animals)
#
#         return output
#
# class BigCage(Cage):
#     place = 5
#
# wolf = Wolf('black', 'wolf')
# sheep = Sheep('white', 'sheep')
# snake = Snake('brown', 'snake')
# parrot = Parrot('green', 'parrot')
#
# c1 = Cage(1)
# c2 = Cage(2)
# bc1 = BigCage(1)
# c1.add_animals(wolf, sheep, parrot)
# c2.add_animals(snake, parrot)
# bc1.add_animals(wolf, sheep, parrot, snake)
# print(c1)
# print(bc1)
# print(c2)



#
# class Animal:
#     def __init__(self, species, color, nbr_leg):
#         self.species = species
#         self.color = color
#         self.nbr_leg = nbr_leg
#
#     def __repr__(self):
#         return f'{self.color}, {self.species}, {self.nbr_leg} legs'
#
# class Wolf(Animal):
#     def __init__(self, color, species, volume):
#         super().__init__(color, species, 4)
#         self.volume = volume
#
# class Sheep(Animal):
#     def __init__(self, color, species, volume):
#         super().__init__(color, species, 4)
#         self.volume = volume
#
# class Snake(Animal):
#     def __init__(self, color, species, volume):
#         super().__init__(color, species, 0)
#         self.volume = volume
# class Parrot(Animal):
#     def __init__(self, color, species, volume):
#         super().__init__(color, species, 2)
#         self.volume = volume
#
# class Cage:
#     space_req = 10
#     def __init__(self, id):
#         self.id = id
#         self.animals = []
#         self.space = []
#
#     def add_animals(self, *animals):
#         for one in animals:
#             self.animals.append(one)
#             self.space.append(one.__dict__['volume'])
#
#     def __repr__(self):
#         if sum(self.space) > self.space_req:
#             return f'No space'
#         else:
#             output = f'Cage {self.id} \n'
#             output += '\n'.join('\t' + str(animal) for animal in self.animals)
#             return output
#
#
# class BigCage(Cage):
#     space_req = 15
#
# wolf = Wolf('black', 'wolf', 3)
# sheep = Sheep('white', 'sheep', 5)
# snake = Snake('brown', 'snake', 2)
# parrot = Parrot('green', 'parrot', 1)
# # print(wolf.__dict__['volume'])
#
# c1 = Cage(1)
# c2 = Cage(2)
# bc1 = BigCage(1)
# c1.add_animals(wolf, sheep)
# c2.add_animals(snake, parrot)
# bc1.add_animals(wolf, sheep, parrot, snake)
# print(c1)
# print(c2)
# print(bc1)

#
# class Animal:
#     def __init__(self, color, species, nbr_leg):
#         self.species = species
#         self.color = color
#         self.nbr_leg = nbr_leg
#
#     def __repr__(self):
#         return f'{self.color}, {self.species}, {self.nbr_leg} legs'
#
# class Wolf(Animal):
#     def __init__(self, color, species, volume):
#         super().__init__(color, species, 4)
#         self.volume = volume
#
# class Sheep(Animal):
#     def __init__(self, color, species, volume):
#         super().__init__(color, species, 4)
#         self.volume = volume
#
# class Snake(Animal):
#     def __init__(self, color, species, volume):
#         super().__init__(color, species, 0)
#         self.volume = volume
# class Parrot(Animal):
#     def __init__(self, color, species, volume):
#         super().__init__(color, species, 2)
#         self.volume = volume
#
# class Cage:
#     avoid_1 = ['sheep', 'wolf']
#     avoid_2 = ['snake', 'parrot']
#
#     def __init__(self, id):
#         self.id = id
#         self.animals = []
#         self.species = []
#
#     def add_animals(self, *animals):
#         for one in animals:
#             self.animals.append(one)
#             self.species.append(one.__dict__['species'])
#
#
#     def __repr__(self):
#         if self.avoid_1 in self.species or self.avoid_2 in self.species:
#             output = f'In this cage \n'
#             output += '\n'.join('\t' + str(specie) for specie in self.species)
#             return output
#         else:
#             output = f'Cage {self.id} \n'
#             output += '\n'.join('\t' + str(animal) for animal in self.animals)
#             return output
#
#
# class BigCage(Cage):
#     space_req = 15
#
# wolf = Wolf('black', 'wolf', 3)
# sheep = Sheep('white', 'sheep', 5)
# snake = Snake('brown', 'snake', 2)
# parrot = Parrot('green', 'parrot', 1)
# # print(wolf.__dict__['color'])
# # print(Cage.avoid_1)
#
# c1 = Cage(1)
# c2 = Cage(2)
# bc1 = BigCage(1)
# c1.add_animals(wolf, parrot)
# c2.add_animals(snake, parrot)
# bc1.add_animals(wolf, sheep, parrot, snake)
# print(c1)
# print(c2)
# print(bc1)


#
# class Animal:
#
#     def __init__(self, species, color, nbr_leg):
#         self.species = species
#         self.color = color
#         self.nbr_leg = nbr_leg
#
#     def __repr__(self):
#         return f'{self.species}, {self.color}, {self.nbr_leg} leg(s)'
#
#
# class Cage:
#
#     def __init__(self, id):
#         self.id = id
#         self.cage = []
#
#     def add_animal(self, *args):
#         for animal in args:
#             self.cage.append(animal)
#
#     def __repr__(self):
#         output = f'Cage {self.id} \n'
#         output += '\n'.join('\t' + str(animal) for animal in self.cage)
#         return output
#
#     def animalsBycolors(self, color):
#         return [animal.species for animal in self.cage if animal.color == color]
#
#     def animalsBylegs(self, nbr_leg):
#         return [animal.species for animal in self.cage if animal.nbr_leg == nbr_leg]
#
#
# class Zoo:
#     cages = []
#     animals = []
#
#     def add_cage(self, *args):
#         for cage in args:
#             self.cages.append(cage)
#
#     def z(self):
#         lst = [cage for cage in self.cages]
#         for cage in lst:
#             print(cage)
#
#     def add_animals(self, *args):
#         for animal in args:
#             self.animals.append(animal)
#
#     def animalsBycolors(self, color):
#         for cage in self.cages:
#             self.animals.append(cage.animalsBycolors(color))
#         return self.animals
#
#
# # Экземплары class Animals
#
# wolf = Animal('wolf', 'black', 4)
# sheep = Animal('sheep', 'white', 4)
# snake = Animal('snake', 'black', 0)
# lion = Animal('lion', 'brown', 4)
# parrot = Animal('parrot', 'green', 2)
# bonobo = Animal('bonobo', 'black', 2)
# austrich = Animal('austrich', 'white', 2)
#
#
#
# #Экземплары class cage и методы
#
# cage_1 = Cage(1)
# cage_2 = Cage(2)
# cage_3 = Cage(3)
#
# cage_1.add_animal(wolf, sheep, snake, parrot)
# cage_2.add_animal(bonobo, lion, austrich)
# cage_3.add_animal(parrot, snake, austrich)
#
# print(cage_1)
# # print(cage_2)
# # print(cage_3)
#
# # print(cage_1.animalsBycolors('black'))
# # print(cage_1.animalsBylegs(0))
# # print(cage_1.animalsBylegs(4))
#
# #Экземплар class Zoo и методы
#
# zoo = Zoo()
# zoo.add_cage(cage_1, cage_2, cage_3)
# zoo.z()
# print(zoo.animalsBycolors('white'))


#
# from math import pi, sqrt
#
# class Geom:
#
#     def __init__(self, a=0 , b=0, c=0):
#         self.a = a
#         self.b = b
#         self.c = c
#
# class Circle(Geom):
#     def area(self):
#         s = 0.5*pi*(self.a**2)
#         return s
#
#     def calculate_perimeter(self):
#         return pi * (self.a * 2)
#
#     def __repr__(self):
#         return f'The area of circle : {self.area()} cm2, Perimeter of circle :{self.calculate_perimeter()} cm'
#
# class Triangle(Geom):
#     def area(self):
#         s = (self.a * self.b)/2
#         return s
#
#     def calculate_perimeter(self):
#         return  self.a + self.b + self.c
#
#     def __repr__(self):
#         return f'The area of triangle: {self.area()} cm2, Perimeter of triangle :{self.calculate_perimeter()} cm'
#
# class Hexagon(Geom):
#     def area(self):
#         s = (self.a**2) * 2 * sqrt(3)
#         return s
#     def calculate_perimeter(self):
#         return self.a * 6
#
#     def __repr__(self):
#         return f'The area of hexagon: {self.area()} cm2, Perimeter of hexagon :{self.calculate_perimeter()} cm'
#
# class LibraryOfShapes:
#
#     def __init__(self):
#         self.libs = []
#
#     def add_geom(self, *args):
#         for geom in args:
#             self.libs.append(geom)
#
#     def __repr__(self):
#         output = f' Shape \n'
#         output += '\n'.join('\t' + str(geom) for geom in self.libs)
#         return output
#
#
# c1 = Circle(3)
# t1 = Triangle(4, 3)
# h1 = Hexagon(4)
#
# # print(c1.__dict__)
# # print(c1.area())
# print(c1)
#
# # print(t1.__dict__)
# # print(t1.area())
# print(t1)
#
# # print(h1.__dict__)
# # print(h1.calculate_perimeter())
# print(h1)

# libs = LibraryOfShapes()
# a = libs.add_geom(c1, t1, h1)
# print(libs)


#
# #
# class Shape:
#     def what_am_i(self):
#         print(f'I am a {self.name_}')
#
# class Polygon:
#     def __init__(self, a=0, b=0, c=0):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def calculate_perimeter(self):
#         perimeter = (self.a + self.b + self.c) * self.n
#         return perimeter
#
#     def change_size(self, x=0, y=0, z=0):
#         self.a = self.a + x
#         self.b = self.b + y
#         self.c = self.c + z
#
#     def __repr__(self):
#         return f'The perimeter of {self.name_}: {self.calculate_perimeter()}'
# class Rectangle(Polygon, Shape):
#     name_ = 'rectangle'
#     n = 2
# class Square(Polygon, Shape):
#     name_ = 'square'
#     n = 4
#     square_list = []
#     def __init__(self, a=0, b=0, c=0):
#         super().__init__(a, b, c)
#         self.square_list.append((self.a, self.a))
#
#     def __repr__(self):
#         return f'{self.name_} parameters : {self.a} x {self.a}'
#
# rect = Rectangle(2, 4)
# sqr = Square(4)
# sqr1 = Square(6)
# sqr2 = Square(4)
#
# rect.calculate_perimeter()
# sqr.calculate_perimeter()
#
# print(rect)
# print(sqr)
#
# print(sqr.square_list)
#
# # # rect.change_size(2, 4)
# # sqr.change_size(1)
# #
# # rect.what_am_i()
# # print(rect)
# # sqr.what_am_i()
#
# print(sqr)
#
# print(sqr is sqr1)
# print(sqr.calculate_perimeter() is sqr2.calculate_perimeter())



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# class Horse:
#     def __init__(self, name, age, owner):
#         self.name = name
#         self.age = age
#         self.owner = owner
#
#     def __repr__(self):
#         return f'The horse named {self.name} with his owner named {self.owner.name} are riding in city'
#
# prs = Person('Vlad', 45)
# hrs = Horse('Violet', 12, prs)
#
# print(hrs)

'''Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.'''

# from math import *
# class Circle:
#     def __init__(self, r, id):
#         self.id = id
#         self.r = r
#
#     def perimeter(self):
#         return (2 * self.r) * pi
#
#     def area(self):
#         return pi * (self.r**2)
#
#     def __repr__(self):
#         output = f'The perimeter of circle {self.id} : {self.perimeter()} cm \n '
#         output += f'The Area of circle {self.id} : {self.area()} cm2'
#         return output
#
# circle_1 = Circle(4, 1)
# circle_2 = Circle(8, 2)
# circle_3 = Circle(10, 3)
# lst = [circle_1, circle_2, circle_3]
#
# for circle in lst:
#     circle.perimeter()
#     circle.area()
#     print('\n', circle, '\n')


'''Write a Python program to create a person class. Include attributes like name, country and date of birth. 
 Implement a method to determine the person's age'''
#
# from  datetime import date
# class Person:
#     d = date(2024, 12, 20)
#     y = d.year
#     def __init__(self, name, country, year_of_bd):
#         self.name = name
#         self.country = country
#         self.year_of_bd = year_of_bd
#
#     def define_age(self):
#         t = self.y - self.year_of_bd
#         return t
#
#     def __repr__(self):
#         output = f'The age of Mr. {self.name} from {self.country} is {self.define_age()} year old'
#         return output
#
# prs1 = Person('Mark', 'Germany', 1987)
# prs2 = Person('Dmitriy', 'Russia', 1978)
# prs3 = Person('Ntumba', 'D.R. Congo', 1959)
#
# lst = [prs1, prs2, prs3]
# for person in lst:
#     person.define_age()
#     print('\n', person, '\n')

#
# ''' Write a Python program to create a calculator class. Include methods for basic arithmetic operations.'''
# class Calculator:
#     operation = ['+', '-', '*', '/']
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def addition(self):
#         return self.x + self.y
#     def substraction(self):
#         return self.x - self.y
#     def multiplication(self):
#         return self.x * self.y
#     def division(self):
#         if self.y == 0:
#             return f'Zero division'
#         return self.x / self.y
#
# print('Welcome to our calculator')
# c = 1
# def start():
#     global c
#     try:
#         while c <= 1:
#             print('Press "ENTER" for living')
#             a = int(input('Enter first nbr : >> '))
#             b = int(input('Enter second nbr : >> '))
#             sg = input('Choose the sign below (+, -, /, *): >>')
#             if sg not in Calculator.operation:
#                 print('choose the correct operation')
#                 finish()
#             elif sg == '+':
#                 calc = Calculator(a, b)
#                 print(f'{a} + {b} = {calc.addition()}')
#             elif sg == '-':
#                 calc = Calculator(a, b)
#                 print(f'{a} - {b} = : {calc.substraction()}')
#             elif sg == '*':
#                 calc = Calculator(a, b)
#                 print(f'{a} * {b} = : {calc.multiplication()}')
#             elif sg == '/':
#                 calc = Calculator(a, b)
#                 print(f'{a} / {b} = : {calc.division()}')
#     except TypeError:
#         print('Not correct type value')
#         finish()
#
#     except ValueError:
#         print('Not correct type value')
#         finish()
# def finish():
#     global c
#     opt = input('Do you want to leave (y/n):>>')
#     if opt == 'n':
#         start()
#     else:
#         c = 2
#
# start()
#
#
# '''Write a Python program to create a class that represents a shape. Include methods to calculate its area
#  and perimeter. Implement subclasses for different shapes like circle, triangle, and square.'''
#
# from  math import *
# class Shape:
#     def __init__(self, a=0, b=0, c=0, h=0):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.h = h
#
#     def perimeter(self):
#         p = (self.a + self.b + self.c) * self.n
#         return p
#
#     def area(self):
#         return f'Define formula'
#
#     def __repr__(self):
#         output = f'The perimeter of {self.name} : {self.perimeter()} cm, the area : {self.area()} cm^2'
#         return output
#
# class Circle(Shape):
#     n = pi
#     name = 'Circle'
#     def area(self):
#         s = pi * (self.a**2)
#         return s
#
# class Triangle(Shape):
#     n = 3
#     name = 'Triangle'
#     def area(self):
#         s = (self.a * self.h)/2
#         return s
#
# class Square(Shape):
#     n = 4
#     name = 'Square'
#     def area(self):
#         s = (self.a**2)
#         return s
#
# class List_of_Shape:
#     lst = []
#     def __init__(self):
#         self.lst = []
#
#     def add_shape(self, *args):
#         for shape in args:
#             self.lst.append(shape)
#         return self.lst
#     def __repr__(self):
#         output = f'shape \n'
#         output += '\n'.join('\t' + str(shape) for shape in self.lst)
#         return output
#
# circle = Circle(9)
# triangle = Triangle(8, 5, 6, 7)
# square = Square(3)
#
# circle.perimeter()
# circle.area()
# triangle.perimeter()
# triangle.area()
# square.perimeter()
# square.area()
#
# list = List_of_Shape()
# list.add_shape(circle, triangle, square)
# print(list)

'''Write a Python program to create a class representing a stack data structure. Include methods for pushing 
and popping elements.'''

# class Stack:
#     stk = []
#     def __init__(self):
#         self.stk = []
#     def pushing(self, x):
#         lst = self.stk.append(x)
#         self.stk.sort()
#         return lst
#     def popping(self, x):
#         if len(self.stk) == 0:
#             return f'stack is empty'
#         elif x not in self.stk:
#             return f'{x} not in stack'
#         r = self.stk.index(x)
#         self.stk.pop(r)
#         return self.stk
#
#     def displaying_stk(self):
#         print(f'Actual stack : {self.stk}')
#
#
# stack = Stack()
# print(stack.popping(4))
# stack.pushing(4)
# stack.pushing(0)
# stack.pushing(1)
# stack.popping(4)
# stack.displaying_stk()

'''Write a Python program to create a class representing a queue data structure. Include methods for 
enqueueing and dequeueing elements.'''
#
# class Queue:
#
#     lst = []
#
#     def __init__(self):
#         self.lst = []
#
#     def enqueueing(self, x):
#         if x not in self.lst:
#             self.lst.append(x)
#             return self.lst
#         return f'Item  already in queue'
#
#     def dequeueing(self, x):
#         if x not in self.lst:
#             print(f'Item {x} not in queue')
#         else:
#             self.lst.remove(x)
#             return self.lst
#
#     def __repr__(self):
#         output = f'The queue {self.lst}'
#         return output
#
#
# queue = Queue()
# queue.enqueueing(10)
# queue.enqueueing(10)
# queue.enqueueing(30)
# queue.enqueueing(40)
# queue.enqueueing(50)
# queue.enqueueing(60)
# queue.dequeueing(10)
# queue.enqueueing(20)
# queue.enqueueing(30)
# queue.enqueueing(10)
# queue.dequeueing(80)
# print(queue)

#
# class Calculator:
#
#     def add (self, x=0, y=0):
#         return x + y
#
#
# class Screen:
#     def display(self):
#         return f'Show : {cal.add(4, 6)}'
#
# cal = Calculator()
# screen = Screen()
# y = screen.display()
#
# print(y)


# class Animal:
#     def move(self):
#         print('moving foward')
#
#     def left_foot_forward(self):
#         print('Moving left foot forward')
#
#     def right_foot_forward(self):
#         print('Moving right foot forward')
#
#     def left_foot_back(self):
#         print('Moving left foot back')
#
#     def right_foot_back(self):
#         print('Moving right foot back')
#
# class Giraffe(Animal):
#     def __init__(self, spots):
#         self.spots = spots
#     def dacing(self):
#         self.move()
#         self.left_foot_forward()
#         self.right_foot_back()
#         self.left_foot_back()
#         self.right_foot_forward()
#
# gerald = Giraffe(200)
# gerald.dacing()



# class MyEnumerate:
#
#     def __init__(self, data):
#         self.data = data
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.data):
#             raise StopIteration
#         value = (self.index, self.data[self.index])
#         self.index += 1
#         return value
#
#
# for index, element in MyEnumerate([1, 4, 5, 7]):
#     print(f'{index}, {element}')



# class MyEnumerate:
#
#     def __init__(self, data, max_time):
#         self.data = data
#         self.max_time = max_time
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= self.max_time:
#             raise StopIteration
#         value = (self.index, self.data[self.index % len(self.data)])
#         self.index += 1
#         return value
#
#
# for index, element in MyEnumerate([1, 4, 5, 7], 6):
#     print(f'{index}, {element}')



# for i, el in enumerate('abc'):
#     print(f'{i+1}, {el}')


# def Myenumerate(data):
#     for i, el in enumerate(data):
#         print(f'{i}, {data[i]}')
#
# Myenumerate('abc')

# def Myenumerate():
#     yield 'a'
#     yield 'b'
#     yield 'c'
#
# for el in Myenumerate():
#     print(el)

# lst_1 = (1, 2, 3)
# lst_2 = ('a', 'b', 'c')
#
# lst_3 = zip(lst_1, lst_2)
# lst_3 = dict(lst_3)
# print(lst_3)


#
# dict_1 = {1: 'a', 2: 'b', 3: 'c'}
# def unzip(data):
#     lst_1, lst_2 = [], []
#     for item in data:
#         lst_1.append(item)
#     for value in data.values():
#         lst_2.append(value)
#     return lst_1, lst_2
#
# print(unzip(dict_1))


# x = 'Hello'
# print(f'{ "hi" if x == "Hello" else "hello"}')


'''Лернер реувен : Python интенсив стр.108. Упражнение Ресторан'''
#
# # \Процедурное программирование
#
# menu = {'Bread': 2,
#         'Pepper-soup': 10,
#         'Spagethie': 7,
#         'Rice': 5,
#         'Potatos': 8,
#         'Chicken': 15,
#         'Salad': 11
#         }
# c = 0
# dict_0 = {}
# lst_price = []
# def prices():
#     for el, count in dict_0.items():
#         price = count * menu[el]
#         lst_price.append(price)
#     return sum(lst_price)
#
# prices()
# def resume():
#     print(f'Your order:{dict_0}, total items :{sum(dict_0.values())}')
# resume()
#
# print('_'*100, '|')
# print('Welcome to our online menu')
# print('_'*100, '|')
# print('Here our menu ->')
# for el in menu:
#     print(f'{el}: {menu[el]} $')
# print('_'*100, '|')
# if input('Do you like to do some order ? (y/n) ->> ') == 'n':
#     print(f'Your finally cart:{dict_0}, total items:{sum(dict_0.values())}, Total price {prices()} $ ')
# else:
#     while not c:
#         a = input('Tape your order Here or Press key "q" to quit:->> ')
#         if a == 'q':
#             resume()
#             print('See you!!')
#             break
#         elif a in menu:
#             x = input('Do you like to add or remove food ? (+/-) ->>')
#             if x == '+':
#                 y = int(input('How many items do you like to add? ->>'))
#                 if a not in dict_0:
#                     dict_0[a] = y
#                     resume()
#                 else:
#                     dict_0[a] += y
#                     resume()
#             elif x == '-':
#                 if a not in dict_0:
#                     print('No food in cart')
#                     resume()
#                 else:
#                     y = int(input('How many items do you like to remove? ->>'))
#                     if dict_0[a] < y:
#                         print('Wrong quantity')
#                         resume()
#                     else:
#                         dict_0[a] = dict_0[a] - y
#                     resume()
#         elif a not in menu:
#             print('For now, we dont have this food')
#             if input('Would you like to leave our menu? (y/n) ->>:') == 'y':
#                 break
#             else:
#                 print('Great')
#
#     print(f'Your cart:{dict_0}, total items:{sum(dict_0.values())}, Total price {prices()} $ ')
#     print('See you!!')

# Объектно-ориентированное программирование

class Menu:

    menu = {'Bread': 2,
        'Pepper-soup': 10,
        'Spagethie': 7,
        'Rice': 5,
        'Potatos': 8,
        'Chicken': 15,
        'Salad': 11,
        'Limonad' : 1,
        'Beer': 20,
        'Water' : 1
        }
    script = ['For adding items to your cart PRESS "+" ',
              'For removing items to your cart PRESS "-" ',
              'For clear  your cart PRESS "0" ',
              'For showing your cart PRESS "*" ',
              'For Exit  PRESS "x" ']

    def __init__(self):
        print('_' * 100, '|')
        print('Our menu ->')
        for el in self.menu:
            print(f'{el}: {self.menu[el]} $')
        self.cart = {}

    def create_order(self):
        self.script_0(self.script)
        y = input('Tape here : ->> ')
        if y == '+':
            z = input('Enter item here : ->> ')
            if z not in self.menu:
                print('No item in menu')
            else:
                print(f'Your cart : {self.add_food(z)}')
        elif y == '-':
            z = input('Enter item here : ->> ')
            if z not in self.menu:
                print('No item in menu')
            else:
                print(f'Your cart : {self.remove_food(z)}')
        elif y == '0':
            if input('Do you like to clear your cart ? (y/n)') == 'y':
                self.clear_menu()
                print(f' Your cart is clear : {self.cart}')
            else:
                print(f'Your cart : {self.cart} ')
        elif y == '*':
            if len(self.cart) == 0:
                print('No order')
            else:
                print(f' Your order : {self.cart}, Total price : {self.total_price(self.cart, self.menu)} $')
        elif y == 'x':
            pass
    def add_food(self, x):
        y = int(input('How many items too add ->_'))
        if x not in self.cart:
            self.cart[x] = y
        else:
            self.cart[x] = self.cart[x] + y
        return self.cart
    def remove_food(self, x):
        y = int(input('How many items to remove ->_'))
        if x not in self.cart:
            print('No item in cart!!')
        else:
            if y <= self.cart[x]:
                self.cart[x] = self.cart[x] - y
            else:
                print('Wrong quantity')
        return self.cart
    def clear_menu(self):
        return self.cart.clear()

    def show_cart(self):
        return self.cart
    @staticmethod
    def total_price(data_1, data_2):
        lst = []
        for el in data_1:
            price = data_1[el] * data_2[el]
            lst.append(price)
        return sum(lst)
    @staticmethod
    def script_0(data):
        print(' Our online services')
        print('_' * 100, '|')
        for el in data:
            print(el)
    @staticmethod
    def continue_0():
        print('_' * 100, '|')
        print(input('Press "c" key to continue or any key to quit : __'))


print('_' * 100, '|')
print('WELCOME TO OUR ONLINE MENU')
order = Menu()
c = True
service = input('Do you wish a personal help ? (y/n) ->> _')
if service == 'n':
    while c:
        order.create_order()
        stop = input('Would you like to continue ? (y/n):__')
        if stop == 'y':
            c = True
        else:
            print(f' Total to pay : {order.total_price(order.cart, order.menu)} $')
            print('THANK YOU!!')
            break
elif service == 'y':
    print('Great')
    print('Our manager will join you soon')

else:
    print('See you soon')




# order.add_food('Bread')
# order.remove_food('Bread')
# print(order.cart)








