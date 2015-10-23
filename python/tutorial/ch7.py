s = 'Hello, world.'
str(s)
repr(s)
str(1/7)
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
hello = 'hello world\n'
hellos = repr(hello)
print(hellos)

repr((x, y, ('spam', 'eggs')))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end= ' ')
    print(repr(x*x*x).rjust(4))


for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print('We are the {} who say "{}!"'.format('knights', 'Ni'))

print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

import math
print('The value of PI is approximately {}.'.format(math.pi))
print('The value of PI is approximately {!r}.'.format(math.pi))

print('The value of PI is approximately {0:.3f}.'.format(math.pi))

table = {'sjoerd': 4127, 'jack': 4098, 'dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d};'
      'Dcab: {0[Dcab]:d}'.format(table))
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

print('The value of PI is approximately %5.3f.' % math.pi)

f = open("test.txt", 'w')

f.read()
print(f)
f.read()
print(f)

f.readline()
print(f)
f.readline()
print(f)

for line in f:
    print(line, end= ' ')

f.write('This is a test\n')
value = ('the answer', 42)
s = str(value)
f.write(s)

f = open('test.txt', 'rb+')
f.write(b'234234asdf')
f.seek(5)
f.seek(-3, 2)
f.read(1)

f.close()
#f.read() -> As file closed, this occurs error.

with open('test.txt',  'r') as f:
    read_data = f.read()

f.closed

json.dumps([1, 'simple', 'list'])
json.dump(x, f)
x = json.load(f)
