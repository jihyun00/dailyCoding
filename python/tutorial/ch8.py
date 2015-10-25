"""
syntax error -> 문법 에러

ZeroDivisionError, NameError, TypeError 존재
ZeroDivisionError -> 값을 0으로 나눴을 때 발생
NameError -> 정의되지 않은 변수를 사용했을 때 발생
TypeError -> 잘못된 타입을 사용하였을 때
ex ) '2' + 2
"""


"""
아래 예제는 Error를 handling 하는 것
value에 int 값이 들어와야 하나 그렇지 않을 경우 ValeueError 로 except 하여 에러를 처리
"""
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try agagin...")


"""
맨 마지막 except를 보면 exception을 wildcard로 넘겨주고 있음
"""
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS Error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


"""
else 구문은 try에서 error를 발생시키지 않으면 반드시 발생
"""
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


"""
exception이 발생했을 때 exception의 arguments를 다루는 예제 
"""
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x, y = inst.args
    print('x =', x)
    print('y =', y)
    

"""
예외가 발생했을 때 ZeroDivisionError을 err 로 받았고,
err 내용을 출력해주고 있다.
"""
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
    

"""
Raising Exceptions

raise -> Error 발생
"""
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise


"""
User-defined Exceptions

자체적으로 에러를 정의한 클래스를 만들어 사용할 수 있음
"""
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

"""
try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:' e.value)

raise MyError('oops!')
"""


"""
Error Handling을 하기 위한 class를 만들 때
아래 예제처럼 xxxError로 끝나게 하는 게 표준 예외처리
"""
class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    def __init__(self,previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message


"""
finally 구문이 포함되어 있으면 어떤 상황이든 무조건 실행
아래 예제에서는 Goodbye, world! 출력하고 
KeyboardInterrupt 발생
"""
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')


"""
try 부분에서 ZeroDivisionError가 발생했음에도 불구하고,
finally 구분은 항상 실행된다.
"""
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('division by zero!')
    else:
        print('result is ', result)
    finally:
        print('executing finally clause')


"""
with절을 이용하여 파일을 open하게 되면
굳이 f.close() 를 수행하지 않아도 with절이 끝나면 파일이 닫힘
"""
for line in open('myfile.txt'):
    print(line, end="")

with open('myfile.txt') as f:
    for line in f:
        print(line, end="")
