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

class RealString:

    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def length_str(self):
        a = f'длина строки 1: {len(self.str1)}'
        b =  f'длина строки 2: {len(self.str2)}'
        return a, b

    def compare_str(self):
        res = ''
        if len(self.str1) > len(self.str2):
            res = f'{self.str1} больше чем {self.str2}'
        elif len(self.str2) > len(self.str1):
            res = f'{self.str2} больше чем {self.str1}'
        else:
            res = 'Они равные'
        return res



s =input('Введите 2 слова через проблем >>').split(' ')
real = RealString(s[0], s[1])

print(real.length_str())
print(real.compare_str())



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


class Shop_crt:
    magasin = {'Яблоко': 10,
               'Манго': 24,
               'Апельсин': 12,
               'Клубника': 18,
               'Груша': 15
               }
    total = 0

    def __init__(self, x):
        self.x = x
    def add(self):
        self.total += self.x
        return self.total
    def rmv(self):
        self.total -= self.x
        return self.total

addition = Shop_crt(4)
Magasin = addition.magasin
for el, price in Magasin.items():
    print(el,':', price, 'Рублей', ' ', end=' ')
lst = []
summa = 0
product = 0
print('')
Shopping = input('Совершать покупку, нажмите клавиша (1) или нажмите любую клавишу для выхода из магазина >>__ ')
if Shopping == '1':
    while Shopping == '1':
        item = input('Напишите наименование товара из корзины --> нажмите Enter / нажмите любую клавишу для выхода из магазина >>__')
        if item in Magasin:
            a = Magasin[item]
            addition = Shop_crt(a)
            str = input('добавить (1) или убрать (2) >>')
            if str == '1':
                lst.append(item)
                summa += addition.add()
                product = len(lst)
                print(lst)
            elif str == '2' and item not in lst:
                print('Нет данного товара в корзине')
            elif str == '2' and item in lst:
                summa += addition.rmv()
                lst.remove(item)
                product = len(lst)
            else:
                print('Выбирайте правильную операцию')
            print(f'Текущая сумма {summa}', f'В корзине: {product} шт.')
        else:
            print('У нас нет данного товара')
            print(f'Сумма к оплате {summa}', f'В корзине: {product} шт.')
            break

else:
    print(f'Общая сумма в корзине: {summa}', f'Количество товара : {product}')



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










