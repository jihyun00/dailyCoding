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


"""TODO -> Error 뜨는데?
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


"""TODO
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


"""TODO
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


"""TODO
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


"""TODO
"""
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')


"""TODO
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


"""TODO
"""
from array import array
a = array('H', [4000, 10, 700, 22222])
sum(a)
a[1:3]
array('H', [10, 700])


"""TODO
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


"""TODO
"""
import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)


"""TODO
"""
from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)
heappush(data, -5)
[heappop(data) for i in range(3)]


"""TODO
"""
from decimal import *
round(Decimal('0.70') * Decimal('1.05'), 2)
round(.70 * 1.05, 2)


Decimal('1.00') % Decimal('.10')
sum([Decimal('0.1')]*10) == Decimal('1.0')
sum([0.1]*10) == 1.0

getcontext().prec = 36
Decimal(1) / Decimal(7)
