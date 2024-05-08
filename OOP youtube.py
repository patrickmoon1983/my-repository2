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

'''from  string import ascii_letters
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
'''

# Дескрипторы (data descriptor, non-data descriptor)

'''class Point3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def verify_coord(cls,coord):
        if type(coord) != int:
            raise TypeError('Координата должны быть целым числом')

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, coord):
        self.verify_coord(coord)
        self._x = coord

    @property
    def y(self):
        return self._y

    @x.setter
    def y(self, coord):
        self.verify_coord(coord)
        self._y = coord

    @property
    def z(self):
        return self._z

    @x.setter
    def z(self, coord):
        self.verify_coord(coord)
        self._z = coord

p = Point3D(1, 2, 3)
print(p.__dict__)
'''

# Допустим что у нас более 10 точек, код станет объёмный, нам на помощь приходит дескриптор.

'''class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('Координата должны быть целым числом')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify_coord(value)
        instance.__dict__[self.name] = value

class Point3D:

    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z



p = Point3D('1', 2, 3)
print(p.__dict__)
'''

'''class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = '_x'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
class Integer: # Дескриптор данных
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('Координата должны быть целым числом')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        setattr(instance, self.name, value)

class Point3D:

    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z



p = Point3D(1, 2, 3)
print(p.__dict__)
p.xr = 5
print(p.xr, p.__dict__)
'''

# Магический метод __call__ Позволяет сделать из экзампляра(обьекта) вызывающие т.е вызывать как функция : класс называется Функтором
'''class Counter:
    def __init__(self):
        self.__counter = 0
    def __call__(self, *args, **kwargs):
        print("__call__")
        self.__counter +=1
        return self.__counter

c = Counter()
c2 = Counter()
c()
c()
res = c()
res2 = c2()
print(res, res2)
'''
'''class Counter:
    def __init__(self):
        self.__counter = 0
    def __call__(self,step=1, *args, **kwargs):
        print("__call__")
        self.__counter += step
        return self.__counter

c = Counter()
c2 = Counter()
c()
c(2)
res = c(10)
res2 = c2(-5)
print(res, res2)'''


'''class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('Аргумент должен быть строкой')

        return args[0].strip(self.__chars)

s1 = StripChars('?:!., ')
s2 = StripChars(' ')
res = s1('Hello world! ')
res2 = s2(' Hello world! ')
print(res, res2, sep='\n')
'''
'''import math
class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x))/ dx


def df_sin(x):
    return math.sin(x)

df_sin = Derivate(df_sin)

print(df_sin(math.pi/3))'''


# Можем создать декоратор с помощью __call__
'''
import math
class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x))/ dx

@Derivate
def df_sin(x):
    return math.sin(x)

print(df_sin(math.pi/3))
'''


# Наследование
'''class Geom:
    name = 'Geom'

    def set_coords(self,x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        print('Рисование гео')

class Line(Geom):
    name = 'Line'

    def draw(self):
        print('Рисование линии')



class Rect(Geom):
        def draw(self):
            print('Рисование прямоугольника')



g = Geom()
l = Line()
r = Rect()
'''

'''class Geom:
    pass

class Line(Geom):
    pass



g = Geom()
l = Line()
print(issubclass(Line, Geom))
print(isinstance(l, Geom))
print(issubclass(int, object))
print(issubclass(list, object))
'''

'''class Vector(list):
    def __str__(self):
        return ' '.join(map(str, self))

v = Vector([1, 2, 3])

print(v, type(v))

#
# def vision (lst):
#     return ' '.join(lst)
# lst = ['1', '2', '3']
# print(vision(lst))

'''
# Наследование иннициализатора super().__init__()
'''class Geom:
    name = 'Geom'
    
    def __init__(self):
        print('Иннициализатор ГЕОМ')
        
class Line(Geom):
    def __init__(self):
        print('Иннициализатор ГЕОМ')'''

'''class Geom:
    name = 'Geom'

    def __init__(self):
        print('Иннициализатор ГЕОМ')

class Line(Geom):

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        print('Рисование линии')

class Rect(Geom):

    def __init__(self, x1, y1, x2, y2, fill=None):
        self.x1 = x1
        self.x1 = y1
        self.x2 = x2
        self.y2 = y2
        self.fill = fill

    def draw(self):
        print('Рисование Прямоугольник')'''


'''class Geom:
    name = 'Geom'


    def __init__(self, x1, y1, x2, y2):
        print(f'Иннициализатор ГЕОМ для {self.__class__}')
        self.x1 = x1
        self.x1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):

    def draw(self):
        print('Рисование линии')

class Rect(Geom):

    def __init__(self, x1, y1, x2, y2, fill=None):
        Geom.__init__(self, x1, y1, x2, y2)
        # или super().__init__(x1, y1, x2, y2)
        print('Иннициализатор Rect')
        self.fill = fill

    def draw(self):
        print('Рисование Прямоугольник')

l = Line(0, 0, 1, 2)
r = Rect(1, 2, 3, 4)
print(r.__dict__)'''

# Наследование аттрибутов

'''class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f'Иннициализатор ГЕОМ для {self.__class__}')
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        
    def get_coords(self): # x1, y1 доступны тут
        return (self.__x1, self.__y1)


class Rect(Geom):

    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self.__fill = fill
        
    def get_coords(self): # x1, y1 недоступны тут
        return (self.__x1, self.__y1)


r = Rect(0, 1, 2, 3)
print(r.__dict__)
'''


'''class Geom:
    __name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f'Иннициализатор ГЕОМ для {self.__class__}')
        self.__verify_coord(x1)
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._name = self.__name

    def __verify_coord(self, coord):
        return 0 <= coord < 100


class Rect(Geom):

    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self._fill = fill

    def get_coords(self):  # x1, y1 доступны теперь тут
        return (self._x1, self._y1)


r = Rect(0, 1, 2, 3)
print(r.get_coords())
print(r.__dict__)'''

# или
'''class Geom:
    __name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f'Иннициализатор ГЕОМ для {self.__class__}')
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._name = self.__name

    def _verify_coord(self, coord):
        return 0 <= coord < 100


class Rect(Geom):

    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self._verify_coord(x1)
        self._fill = fill

    def get_coords(self):  # x1, y1 доступны теперь тут
        return (self._x1, self._y1)


r = Rect(0, 1, 2, 3)
print(r.get_coords())
print(r.__dict__) '''
# Привать метод можно его вызывать только в классе где он определеный, в дочерныз классах доступ запрешен

# Полиморфизм
'''class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def get_rect_pr(self):
        return 2*(self.w + self.h)

class Square:
    def __init__(self, a):
        self.a = a

    def get_sq_pr(self):
        return 4*self.a


r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
s1 = Square(10)
s2 = Square(20)

# print(r1.get_rect_pr(), r2.get_rect_pr())
# print(s1.get_sq_pr(), s2.get_sq_pr())

geom = [r1, r2, s1, s2]
for g in geom:
    if isinstance(g, Rectangle):
        print(g.get_rect_pr())
    else:
        print(g.get_sq_pr())
'''



'''class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def get_rect_pr(self):
        return 2*(self.w + self.h)

class Square:
    def __init__(self, a):
        self.a = a

    def get_sq_pr(self):
        return 4*self.a

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_tr_pr(self):
        return self.a + self.b + self.c


r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
s1 = Square(10)
s2 = Square(20)
t1 = Triangle(1, 2, 3)
t2 = Triangle(4, 5, 6)

# print(r1.get_rect_pr(), r2.get_rect_pr())
# print(s1.get_sq_pr(), s2.get_sq_pr())

geom = [r1, r2, s1, s2, t1, t2]
for g in geom:
    if isinstance(g, Rectangle):
        print(g.get_rect_pr())
    else:
        print(g.get_sq_pr())
'''


'''class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def get_pr(self):
        return 2*(self.w + self.h)

class Square:
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4*self.a

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c


# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# s1 = Square(10)
# s2 = Square(20)
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
# geom = [r1, r2, s1, s2, t1, t2]
#
# for g in geom:
#    print(g.get_pr())

geom = [Rectangle(1, 2), Rectangle(3, 4),
        Square(10), Square(20),
        Triangle(1, 2, 3), Triangle(1, 2, 3)
        ]
for g in geom:
   print(g.get_pr())
'''
# Оптимизация

'''class Geom:
    def get_pr(self):
        raise NotImplementedError('В дочернем классе должен быть переопределен метод get_pr()')

class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
     return 2 * (self.w + self.h)
class Square(Geom):
    def __init__(self, a):
            self.a = a

    def get_pr(self):
        return 4 * self.a

class Triangle(Geom):
    def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c



geom = [Rectangle(1, 2), Rectangle(3, 4),
        Square(10), Square(20),
        Triangle(1, 2, 3), Triangle(1, 2, 3)
        ]
for g in geom:
    print(g.get_pr())
    
'''

# Множественное наследование
'''class Goods:

    def __init__(self, name, weight, price):
        super().__init__()
        print('Init Goods')
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.price}')


class Mixinlog:
    ID = 0

    def __init__(self):
        print('Init Mixinlog')
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f'{self.id}: Товар был продан в 00:00 часов')

class Notebook(Goods, Mixinlog):
    pass


n = Notebook('Acer', 1.5, 30000)
n.print_info()
n.save_sell_log()
'''
'''class Goods:

    def __init__(self, name, weight, price):
        super().__init__()
        print('Init Goods')
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.price}')


class Mixinlog:
    ID = 0

    def __init__(self): #без параметров только self
        super().__init__()
        print('Init Mixinlog')
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f'{self.id}: Товар был продан в 00:00 часов')

class Mixinlog2:

        def __init__(self): #без параметров только self
            super().__init__()
            print('Init Mixinlog')

class Notebook(Goods, Mixinlog, Mixinlog2):
    pass


n = Notebook('Acer', 1.5, 30000)
n.print_info()
n.save_sell_log()
print(Notebook.mro())
# В дополнительных классов иннициализатор следует подписывать без параметров только self..'''

class Goods:

    def __init__(self, name, weight, price):
        super().__init__()
        print('Init Goods')
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.price}')


class Mixinlog:
    ID = 0

    def __init__(self): #без параметров только self
        super().__init__()
        print('Init Mixinlog')
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f'{self.id}: Товар был продан в 00:00 часов')

    def print_info(self):
        print(f'Print_info from Mixinglog')



class Notebook(Goods, Mixinlog):
    def print_info(self):
        Mixinlog.print_info(self)


n = Notebook('Acer', 1.5, 30000)
n.print_info()

# Вызов метода print_info от доп.класс Mixinglog