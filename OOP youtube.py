from accessify import private, protected

'''
class Pointer:
    "Class of point"
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords (self):
        return (self.x, self.y)


Pointer.circle = 10
print(Pointer.__doc__)
#print(Pointer.color, Pointer.circle)

pt = Pointer()
pt.set_coords(1, 3)
print(pt.__dict__)

pt2 = Pointer()
pt2.set_coords(2, 4)
print(pt2.__dict__)

f = pt.get_coords()
print(f)

g = getattr(pt2, 'get_coords')
print(g())
'''


'''
class Pointer:
    "Class of point"
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0):
        print('Calling init')
        self.x = x
        self.y = y

    def __del__(self):
        print('Deleting object' + str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords (self):
        return (self.x, self.y)

pt = Pointer(2)

print(pt.__dict__)
print(Pointer.__dict__)

'''
'''
class Pointer:
    "Class of point"
    color = 'red'
    circle = 2

    def __new__(cls, *args, **kwargs):
        print('Calling new ' + str(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print('Calling init' + str(self))
        self.x = x
        self.y = y


pt = Pointer(1, 2)
print(pt)

'''

'''
class Vector:
    MIN_COORD = 0
    MAX_COORD = 100


    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y
        print(self.norm2(self.x, self.y))


    def get_coords(self):
        return self.x, self.y
    @staticmethod
    def norm2(x, y):
        return x*x + y*y

v = Vector(5,6)
v2 = Vector(10, 20)


res = v.get_coords()
res1 = v2.get_coords()
res2 = Vector.get_coords(v)
res3 = Vector.validate(5)
res4 = Vector.norm2(5, 6)

print(res, res1, res2)
print(res3)
print(res4)

 '''
# Зашита аттрибутов  @public, private, protected

'''class Pointer:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

pt = Pointer(1, 2)

print(pt.x, pt.y)


class Pointer:

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

pt = Pointer(1, 2)

print(pt._x, pt._y)

class Pointer:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

pt = Pointer(1, 2)

print(pt.__x, pt.__y)


class Pointer:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def set_coord(self, x, y):
        if type(x) in (int, float) and type(y) in (int, float):
            self.__x = x
            self.__y = y
        else:
            raise ValueError ('must be a number')

    def get_coord(self):
        return self.__x, self.__y


pt = Pointer(1, 2)
print(pt.set_coord('10', 20))
print(pt.get_coord())

'''
'''class Pointer:

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y


    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError ('must be a number')

    def get_coord(self):
        return self.__x, self.__y


pt = Pointer(1, 2)
print(pt.set_coord(10, 20))
print(pt.get_coord())
'''


'''class Pointer:

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y

    @private
    @classmethod
    def check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError ('must be a number')

    def get_coord(self):
        return self.__x, self.__y


pt = Pointer(1, 2)
print(pt.set_coord(10, 20))
print(pt.get_coord())
print(pt.check_value(5))
'''

# settatr , getattr, delattr,//
'''class Point:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:  # либо Point.MIN_COORD <= x <= Point.MAX_COORD: # только так можно обращатся к аттрибутам класса.!
            self.__x = x
            self.__y = y

    def set_bound(self, left): # Метод который позволяет изменить аттрибута класса (но некорректный)
        self.MIN_COORD = left


pt1 = Point(1, 2)
pt2 = Point(10, 20)
print(pt1.MAX_COORD)

pt1.set_bound(-100)
print(pt1.__dict__)
print(Point.MIN_COORD)
print(Point.__dict__)'''

'''class Point:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:  # либо Point.MIN_COORD <= x <= Point.MAX_COORD:
            self.__x = x
            self.__y = y
    @classmethod
    def set_bound(cls, left): # Метод который позволяет изменить аттрибута класса, более правильный метод через cls
        cls.MIN_COORD = left


pt1 = Point(1, 2)

print(pt1.MAX_COORD)
print(pt1.MIN_COORD)
print(pt1.__dict__)
pt1.set_bound(-100)
print(Point.MIN_COORD)
print(Point.__dict__)
print(pt1.MIN_COORD)'''

'''class Point:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:  # либо Point.MIN_COORD <= x <= Point.MAX_COORD:
            self.__x = x
            self.__y = y
    def __getattribute__(self, item): # Управлять обращение к тому или иной аттрибут
        if item == "x":
            raise ValueError('Access denied') # запрещаем доступ к  конкретному аттрибуту х
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value): # Позволяет присваинме аттрибут определенное значение 
        if key == 'z':
            raise AttributeError ('Aviod attribut name') Запретить присвайвать кокретный аттрибут определенное значение
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):  # Исключить ошубку при обращении к несуществующему аттрибуту
        return False


    def __delattr__(self, item): #  Удаление аттрибута
        print(' Delete attribut' +' '+ item)
        object.__delattr__(self, item)

pt1 = Point(1, 2)
pt2 = Point(5, 7)

# print(pt1.x)

#pt1.z = 5

# print(pt1.r)

del(pt1.x)
print(pt1.__dict__)
print(Point.__dict__)
'''


# Паттерн моносостояние

'''
class ThreadData:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


class ThreadData:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }
    def __init__(self):
        self.__dict__ = self.__shared_attrs
        
t
th1 = ThreadData()
th1.__dict__
{'name': 'thread_1', 'data': {}, 'id': 1}
th2 = ThreadData()
th2.id = 4
th1.age = 14
th1.__setattr__('age', 45 )

'''
#Свойства @property,
'''class Person:
    def __init__(self,name, old):
        self.__name = name
        self.__old = old

    def set_old(self, old):
        self.__old = old

    def get_old(self):
        return self.__old


p = Person('Сергей', 20)
p.set_old(35)
print(p.get_old())
'''

'''class Person:
    def __init__(self,name, old):
        self.__name = name
        self.__old = old

    def set_old(self, old):
        self.__old = old

    def get_old(self):
        return self.__old

    old = property(get_old, set_old) #Аттрибут для быстрого доступа и удобного доступа к нашим сеттеру и геттеру, он приоритетный аттрибут
    
    # или в таком виде написать
    # old = property()
    # old = old.setter(set_old)
    # old = old.getter(get_old)


p = Person('Сергей', 20)
p.__dict__['old'] = 10
p.old = 35
print(p.old, p.__dict__)
'''


'''class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old
    @old.setter
    def old(self, old):
        self.__old = old



p = Person('Сергей', 20)
p.__dict__['old'] = 10
p.old = 35
print(p.old, p.__dict__)
'''
'''class Person:
    def __init__(self, name, old):
        self.name = name
        self.old = old

    @property
    def old(self):
        return self.__old
    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old



p = Person('Сергей', 20)
del p.old

print(p.__dict__)'''

# Пример использования @property  в ООп
from  string import ascii_letters
class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыьэюя-'
    S_RUS_UPPER = S_RUS.upper()


    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_ps(ps)
        self.verify_weight(weight)

        self.__fio = fio.split()
        self.__old = old
        self.__passport = ps
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФИО должно быть строкой')

        f = fio.split()
        if len(f) != 3:
            raise TypeError('Неверный формат ФИО')

        letters = ascii_letters + cls.S_RUS + cls. S_RUS_UPPER
        for s in f:
            if len(s) <1:
                raise TypeError('В ФИО должен быть хотя бы один символ')
            if len(s.strip(letters)) != 0:
                raise TypeError ('В ФИО можно использовать только буквенные символы и дефис')

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old >120:
            raise TypeError('Возраст должен быть целым числом в диапазоне от 14 до 120')

    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w < 20:
            raise TypeError('Вec должен быть вещественный (float)от 20 кг')

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str :
            raise TypeError('Паспорт должен быть строкой')

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError('Неверный формат паспорта')

        for p in s:
            if not p.isdigit():
                raise TypeError('Сения и номер паспорта должны быть числами')

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @old.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__passport

    @old.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__passport = ps


p = Person('Балакирев Сергей Михайлович', 30, '1234 567890', 80.0)
p.old = 100
p.passport = '2453 123456'
p.weight = 70.0
print(p.old)
