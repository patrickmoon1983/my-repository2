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
#     print(el,':', price, 'Рублей', ' ', end=' ')
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



class Bank:

    services = ['Your balance ->Press "1"',
                'Deposit -> Press "2" ',
                'Withdraw money -> Press "3" ',
                'New credit account -> Press "4" ',
                'To view your credit balance -> Press "5"',
                'Your withdraw in credit account -> Press "6"',
                'To Deposit in credit account -> Press "7" ',
                'To close your credit balance -> Press "8" ',
                ' For services -> Press "9" '
                ]
    def __init__(self, name, age, pswrd):
        self.validate_age(age)
        self.validate_pswrd(pswrd)
        self.__name = name
        self.__age = age
        self.__pswrd = pswrd
    def creating_acount(self):
        print('______________________________________________')
        print(f'Hello Mr(Ms) {self.__name}, Welcome to our Bank!')
        print(f'Your balance :->> {self.balance}$')
        self.main_serv()
        self.serVices()
    def serVices(self):
        for service in self.services:
            print(service)
        print('______________________________________________')
        n = input('Choose your service here : -> ')
        if n == '1':
            print(f'Your balance: {self.balance}$')
            print(input('Press ->"ENTER" to continue" >>'))
            self.serVices()
            print('______________________________________________')
        elif n == '2':
            if int(input('Enter your password : ->')) == self.__pswrd:
                summa = int(input('tape the sum here ->'))
                print(f'Your balance : {self.deposite(summa)}$')
                self.main_serv()
                self.serVices()
            else:
                print('!!!Incorrect password !!!')
                self.main_serv()
                self.serVices()

        elif n == '3':
            if int(input('Enter your password : ->')) == self.__pswrd:
                summa = int(input('tape the sum to withdraw ->'))
                print(f'Your balance : {self.withdraw(summa)}$')
                self.main_serv()
                self.serVices()
            else:
                print('!!!Incorrect password !!!')
                self.main_serv()
                self.serVices()
        elif n == '4':
            if bank_ac_1.counter < 1:
                bank_ac_1.credit_creation()

            else:
                print('You have already created a account')
            self.main_serv()
            self.serVices()
        elif n == '5':
            bank_ac_1.view_cr_bal()
            self.main_serv()
            self.serVices()

        elif n == '6':
            if bank_ac_1.counter == 0:
                print('You are about to create an credit account, and it will creating automatically')
                if int(input('Enter your password : ->')) == self.__pswrd:
                    summa = int(input('tape the sum to withdraw ->'))
                    bank_ac_1.credit_wd(summa)
                    bank_ac_1.counter = 1
                    self.main_serv()
                    self.serVices()

                else:
                    print('!!!Incorrect password !!!')
                    self.main_serv()
                    self.serVices()

            else:
                if int(input('Enter your password : ->')) == self.__pswrd:
                    summa = int(input('tape the sum to withdraw ->'))
                    bank_ac_1.credit_wd(summa)
                    self.main_serv()
                    self.serVices()
                else:
                    print('!!!Incorrect password !!!')
                    self.main_serv()
                    self.serVices()


        elif n == '7':
            if bank_ac_1.counter == 0:
                print('You are about an credit account, or it will creating automatically')
                if int(input('Enter your password : ->')) == self.__pswrd:
                    summa = int(input('tape the sum to deposit ->'))
                    bank_ac_1.deposit_credit(summa)
                    bank_ac_1.counter = 1
                    self.main_serv()
                    self.serVices()
                else:
                    print('!!!Incorrect password !!!')
                    self.main_serv()
                    self.serVices()
            else:
                if int(input('Enter your password : ->')) == self.__pswrd:
                    summa = int(input('tape the sum to deposit ->'))
                    bank_ac_1.deposit_credit(summa)
                    bank_ac_1.counter = 1
                    self.main_serv()
                    self.serVices()
                else:
                    print('!!!Incorrect password !!!')
                    self.main_serv()
                    self.serVices()
        elif n == '8':
            bank_ac_1.close_cred_bal()
            self.main_serv()
            self.serVices()
        else:
            if input('Press the key-> "ENTER" to leave') == '':
                print('!!!Goodbye!!! See you soon.!')
            else:
                self.main_serv()
                self.serVices()

    def deposite(self, summa):
        self.balance += summa
        return self.balance

    def withdraw(self, summa):
        if self.balance - summa < 0:
            print('Less money in balance')
            return self.balance
        else:
            return self.balance - summa

    @classmethod
    def validate_pswrd(cls, pswrd):
       if type(pswrd) != int:
           raise TypeError('The password must be a number')

       pwd = str(pswrd)
       if len(pwd) != 4:
           raise TypeError('The password must be a number with 4 chars')

    @classmethod
    def validate_age(cls, age):
        if age < 18 or age >120 :
            raise TypeError('Your must be older then 18 years, and less the 120 years old')
    @staticmethod
    def main_serv():
        print('______________________________________________')
        print(input('Press ->"ENTER" to continue" >>'))

    @staticmethod
    def avoid():
        print('Enter correct data: For help, contact our service')
        print('Your password must be a number with 4 characters')
        print('You must be older then 18-years old or less then 120-years old')


class creditation:
    percent = 0.17
    counter = 0
    def credit_creation(self):
        print(f"You've just created a credit balance! Thank for believing in us")
        print(f'Your credit balance : {self.credit_balance}$')
        self.counter += 1
    def credit_wd(self, summa):
            money_1 = self.credit_balance - (summa + (summa * self.percent))
            self.credit_balance = money_1
            print(f'Your credit balance : {self.credit_balance}$, percent :{self.percent} ')

    def deposit_credit(self, cash):
        money_2 = self.credit_balance + cash
        self.credit_balance = money_2

        print(f' Your credit balance {self.credit_balance}$')
    def view_cr_bal(self):
        print(f'Your credit balance : {self.credit_balance }$')

    def close_cred_bal(self):
        if self.credit_balance < 0:
            print(f'For closing your credit balance, you must deposit{self.credit_balance}$')
            print('Press the key -> "7" to deposit')
        else:
            print(f'Your credit balance is positif,  your balance : {self.credit_balance}$')



class Bank_acount_1(Bank, creditation):
    credit_balance = 0
    balance = 0
    neg_bal = 0


class Bank_acount_2(Bank, creditation):
    credit_balance = 0
    balance = 0
    neg_bal = 0


counter = 0
while counter < 3:
    try:
        print('___________________________________________')
        print('For creating acount, fill the case below:')
        print('___________________________________________')
        Bank.avoid()
        print('___________________________________________')
        name = input(f'Enter your name ->>')
        age = int(input(f'Enter your age ->>'))
        pswrd = int(input(f'Create your password. Your password must be a number with 4 characters  ->>'))
        bank_ac_1 = Bank_acount_1(name, age, pswrd)
        # bank_ac_2 = Bank_acount_2()
        bank_ac_1.creating_acount()
        counter = 3
    except ValueError:
        print('Incorrect format data')
        Bank.avoid()
        counter += 1


# # bank_ac_2.creating_acount()
# print(bank_ac_1.name)
# print(bank_ac_1.ID)
# print(bank_ac_1.status(-10))
# print(bank_ac_1.neg_bal)
# print(bank_ac_1.credit(1000))
# bank_ac_1.clear_perc(1000)
# # print('________________________________')
# # print(bank_ac_2.name)
# # print(bank_ac_2.ID)
# # print(bank_ac_2.neg_bal)
# # print(bank_ac_2.credit(1000))
# # bank_ac_2.clear_perc(1000)