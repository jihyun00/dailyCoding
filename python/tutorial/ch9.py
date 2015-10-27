"""
변수 설정을 아무것도 붙이지 않고 했을 때는 지역변수로 선언,
nonlocal을 붙였을 때는 클래스 내에서 할당
global로 할당했을 때는 전역변수로 할당
"""
def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

"""
class의 사용법을 보여주기 위한 예제
class ClassName:
    blahblah...
"""
class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'

"""
class의 초기화는 아래와 같이 진행
"""
x = MyClass()


"""
클래스 초기상태에 빈 리스트 생성
"""
def __init__(self):
    self.data = []


"""
def __init__() 함수에서 클래스 초기 생성시에 필요한 값들을 할당해주고 있다.
"""
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

print(x.r)
print(x.i)

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2

print(x.counter)
del x.counter


x.f()

xf = x.f
while True:
    print(xf())


class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name

d = Dog('Fido')
e = Dog('Buddy')

print(d.kind)
print(e.kind)
print(d.name)
print(e.name)

class Dog:
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)


class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)


def f1(self, x, y):
    return min(x, x+y)


class C:
    f = f1
    def g(self):
        return 'hello world'

    h = g


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)


"""
TODO : inheritance
"""

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.item_list.append(item)

    __update = update


class MappingSubclass(Mapping):
    for item in zip(keys, values):
        self.items_list.append(item)


class Employee:
    pass

john = Employee()

john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000


class B(Exception):
    pass
class C(B):
    pass
class D(C);
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two': 2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt")
    print(line, end=' ')


class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
print(iter(rev))

for char in rev:
    print(char)


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)


sum(i*i for i in range(10))
xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x, y in zip(xvec, yvec))


from math import pi, sin
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}
unique_words = set(word for line in page for word in line.split())
valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))
