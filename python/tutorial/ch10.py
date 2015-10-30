"""
os module을 import 헀을 때 쓸 수 있는 함수들.
getcwd() -> get current working directory
chdir -> change directory
os.system() 하면 C언어에서 system() 함수 호출하는 것과 같은 효과
아래 예제에서는 mkdir tody 이므로 tody 폴더 생성
"""
import os
os.getcwd()
os.chdir('../')
os.system('mkdir tody')


"""
dir(os) 수행 시 os module의 모든 함수 리스트 리턴
help(os) -> os module에 대한 man page 리턴
"""
dir(os)
help(os)


"""
shutil 모듈 import시 파일을 좀 더 높은 레벨에서 다루기 쉽게 해줌
"""
import shutil
shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')


"""
특정 패턴과 맞는 경로명을 찾는 모듈
"""
import glob
glob.glob('*.py')


"""
command line의 argument return
"""
import sys
print(sys.argv)

sys.stderr.write('Warning, log file not found starting a new one\n')

"""
re 모듈 import 시 정규화 관련된 함수 사용 가능
"""
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

'tea foo too'.replace('too', 'two')


"""
math 모듈 import시, cos, sin 등 수학연산을 수행할 수 있음
"""
import math
math.cos(math.pi / 4)
math.log(1024, 2)


"""
random 모듈 import시, random과 관련된 함수들을 사용할 수 있음
"""
import random
random.choice(['apple', 'pear', 'banana'])
random.sample(range(100), 10)
random.random()
random.randrange(6)


"""
statistics 모듈은 통계관련 모듈
"""
import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)
statistics.median(data)
statistics.variance(data)


"""
urllib 모듈은 url 주소 접근하는 모듈
"""
from urllib.request import urlopen
with urlopen('http://naver.com') as response:
    for line in response:
        line = line.decode('utf-8')
        if 'EST' in line or 'EDT' in line:
            print(line)


"""
mail 보내는 모듈
"""
import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('noblea1117@gmail.com', 'noblea1117@naver.com',
        """To: noblea1117@gmail.com
        From: noblea1117@naver.com

        Hello World
        """)
server.quit()


"""
날짜와 관련된 모듈과 그의 사용법
"""
from datetime import date
now = date.today()
print(now)
datetime.date(2003, 12, 2)
print(now.strftime("%m-%d-%y. %d %b %Y is a %AA on the %d day of %B."))

birthday = date(1993, 11, 17)
age = now - birthday
print(age.days)


"""
압축 관련 모듈
"""
import zlib
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
len(t)
zlib.decompress(t)
zlib.crc32(s)


"""
performance 측정 관련 모듈
"""
from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
Timer('a,b = b,a', 'a=1; b=2').timeit()


"""
doctest 모듈은 docstring으로 쌓여 있는 값을 실행했을 때
유효한지 판단하는 모듈
"""
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()


"""
함수 테스트 모듈
"""
import unittest

class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()
