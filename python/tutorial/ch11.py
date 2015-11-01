"""문자열 집합 표현한 것을 repr type으로 리턴
"""
import reprlib

reprlib.repr(set('supersupersuperchoiji'))


"""리스트 길이 제한
"""
import pprint

t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
pprint.pprint(t, width=30)


"""docstring 길이 제한
"""
import textwrap
doc = """The wrap() method is awesome awesome blahblah yeah awesome fantastic baby."""
print(textwrap.fill(doc, width=40))


"""TODO -> Error 뜨는데? setlocale error;
"""
import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')
conv = locale.localeconv()
x = 1234567.8
locale.format("%d", x, grouping=True)
locale.format_string("%s%.*f", (conv['currency_symbol'],
                     conv['frac_digits'], x), grouping=True)


"""${variable}을 통해서 값을 넣을 수 있다.
아래예제에서 villages, cause가 각각 substitute에서 대입한 문자열로 바뀐다.
"""
from string import Template
t = Template('${village}folk send $$10 to $cause.')
t.substitute(village='Nottingham', cause='the ditch fund')

"""$owner가 정의되어 있지 않으므로 Error
"""
t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
t.substitute(d)

t.safe_substitute(d)


""" time 모듈은 시간과 관련된 함수들 제공
"""
import time, os.path
photofiles = ['img.jpg', 'img2.jpg']

class BatchRename(Template):
    delimiter = '%'

fmt = input('Enter name rename style (%d-date %n-seqnum %f-format): ')
t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))


""" struct module은 pack 함수와 unpack 함수를 제공
"""
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size


""" threading 모듈은 thread 생성, join, start 등을 할 수 있는
thread와 관련된 모듈
"""
import threading, zipfile

class Asynczip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
    def run(self):
        f = zipfile.Zipfile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of : ', self.infile)

background = AsyncZip('test.txt', 'mytest.txt')
background.start()
print('The main program continues to run in foreground.')

background.join()
print('Main program waited until background was done.')


""" logging module은 debug할 때, Error, Warning 등이 났을 때
설정할 수 있는 문구들
"""
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')


""" gc module은 garbage collector 
del a 수행 후 gc.collect() 를 수행하면 지워진 a 변수에 남아있는
쓰레기값을 제거해준다
weakref module은 object를 reference 변수를 생성하지 않고 
트래킹하는 거 
"""
import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])

del a
gc.collect()
d['primary'] # This occurrs error


""" array 모듈은 array object 제공
"""
from array import array
a = array('H', [4000, 10, 700, 22222])
sum(a)
a[1:3]
array('H', [10, 700])


""" chap5에서 했던 거 
"""
from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())

unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)


""" bisect 모듈을 쓰면 오름차순으로 순서대로 정리
"""
import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)


""" heapq 모듈은 list를 기본으로 heap 자료구조 제공 
"""
from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)
heappush(data, -5)
[heappop(data) for i in range(3)]


""" decimal 모듈은 decimal datatype을 제공
"""
from decimal import *
round(Decimal('0.70') * Decimal('1.05'), 2)
round(.70 * 1.05, 2)


Decimal('1.00') % Decimal('.10')
sum([Decimal('0.1')]*10) == Decimal('1.0')
sum([0.1]*10) == 1.0

getcontext().prec = 36
Decimal(1) / Decimal(7)
