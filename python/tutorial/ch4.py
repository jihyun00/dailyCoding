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


"""
의무적으로 써야하는 prompt argument만 쓸 수 있고, 
이미 값이 지정되어 있는 keyword argument에 새로운 값을 넣어 함수를 호출할 수도 있다.
"""
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


"""
아래와 같은 예제일 경우 f()를 호출하면 5를 출력함.
default value는 함수 선언부에서만 영향을 받기 때문.
즉, i = 6을 선언한 후 f() 함수를 호출해도 f 함수에 영향을 주지 않음.
"""
i = 5
def f(arg=i):
    print(arg)

i = 6
f()


"""
이 경우 f 함수의 arguments로 1을 주었기 때문에 a 값에 1이 들어감.
위와 같은 논리라면 함수는 중간에 영향을 받지 않고, 선언부에서만 영향을 받기 때문에
각각 1, 2, 3을 출력할 것이라고 보임.
하지만, list가 dictionary, class의 instance 같은 경우 예외가 발생. 함수 호출한 부분에서 영향을 받음.
따라서, 첫번째 값 1, 두번째 1, 2, 세 번째 1, 2, 3 출력
"""
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


"""
만약 위의 예제처럼 그 전에 호출된 함수에 영향을 받게 하지 않기 위해선 
아래 예제와 같이 해주면 이전값에 영향을 받지 않음
"""
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

"""
함수를 호출할 때 arguments를 설정하는 방법들이다.
자리에 맞게 arguments를 설정하고 함수를 호출할 수도 있고,
자리와 다르게 arguments를 설정할 경우, argument의 이름을 호출하여 설정해줄 수 있다.
"""
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


"""
함수 parameter로 *arugments, **keywords를 받을 수 있음.
keywords 방식의 경우 dict 처럼 key와 value값을 받는 형태를 취함
"""
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


"""
dictionary를 이용하여 함수의 매개변수에 값을 전달하는 방식
"""
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end= ' ')
    print("if you put", voltage, "volts through it.", end= ' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


"""
lambda는 작은 단위의 익명함수.. 라고 생각하면 될 듯
lambda x: x + n 의 함수는
def <lambda>(x):
    return x+n
과 동일한 기능을 한다.
"""
def make_incrementor(n):
    return lambda x: x+n

f = make_incrementor(42)
print(f(0))
print(f(1))

"""
lambda 함수를 이용하여 리스트를 sorting하였음
pair[1]번 값, 즉, 'one', 'two', 'three', 'four' 값을 비교해 sorting 하였음
결과는 알파벳 순서대로 sorting
"""
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])


"""
function_name.__doc__ 형식을 취할 경우 docstring에 있는 내용 출력
"""
def my_function():
    """Hello World

    15duck Hurray
    """
    pass

print(my_function.__doc__)


"""
함수에 -> 쓸 경우 return형 지정
따라서 f 함수는 str을 return
function_name.__annotations__ 는 함수에 대한 설명 가져옴
함수에 들어가는 arguement, argument들의 type, 그리고 함수의 반환형에 대한 정보를 가져옴
"""
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
    

