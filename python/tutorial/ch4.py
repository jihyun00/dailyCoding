'''
'''
a, b = 0, 1
while b < 1000:
    print(b, end =',')
    a, b = b, a+b
print('\n')

print(list(range(5)))


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end= ' ')
        a, b = b, a+b
    print()

fib(2000)


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
print(f100)


def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries -1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)


ask_ok('Are you ok?')
ask_ok('Do you really want to quit?', 2)
ask_ok('Do you really want to quit?', 2, 'Come on, only yes or no!')


i = 5
def f(arg=i):
    print(arg)

i = 6
f()


'''
이 예제 잘 모르겠음;
'''
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


'''
이 예제 잘 모르겠음;
'''
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("--This parrot wouldn't", action, end= ' ')
    print("if you put", voltage, "volts through it.")
    print("--Lovely plumage, the", type)
    print("It's", state, "!")

parrot(1000)
parrot(voltage=1000)
parrot(voltage=100000, action='VOOOOM')
parrot(action='VOOOOM', voltage=1000000)
parrot('a million', 'bereft of life', 'jum')
parrot('a thousand', state='pushing up the daisies')


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

print(list(range(3, 6)))
args = [3, 6]
print(list(range(*args)))


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end= ' ')
    print("if you put", voltage, "volts through it.", end= ' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


def make_incrementor(n):
    return lambda x: x+n

f = make_incrementor(42)
print(f(0))
print(f(1))


def my_function():
    """Hello World

    15duck Hurray
    """
    pass

print(my_function.__doc__)


def f(ham:str, eggs: str = 'eggs') -> str:
    print('Annotations:', f.__annotations__)
    print('Arguments:', ham, eggs)
    return ham + ' and ' + eggs

print(f('spam'))


"""
InterMezzo: Coding Stype(자세한 건 pep8 참고) -> 코딩할 때는 flake8 깔면 pep8 안 맞는 코딩 스타일들을 볼 수 있음

1. 4-space 이용, tab 안됨
2. 한 줄에 79자를 넘지 않는다.
3. 함수와 클래스 구분하기 위해 blank line 사용
4. 주석 자주 사용하기
5. docstring 사용할 것 -> """ """ (O) ''' '''(x)
6. 연산자나 comma 뒤에 space 사용할 것, 단 ( 다음에는 space 사용하지 않음
ex) a = f(1, 2,) + g(3, 4)
7. Class에는 CamelCase, 함수나 method에는 lower_case_with_underscores, 함수의 첫번째 함수 인자로 무조건 'self' 사용
8. 기본적으로 UTF-8, 혹은 ASCII encoding 사용
9. 식별자에 non-ASCII 문자 쓰지 말기

"""
    

