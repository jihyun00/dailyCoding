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
TODO
"""
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x, y = inst.args
    print('x =', x)
    print('y =', y)
    
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
"""
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:' e.value)

raise MyError('oops!')


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


try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')

