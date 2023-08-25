import sys


def hello():
    print('hello')
    print('hell')
    print('hel')

hello()
hello()
hello()


##############

def hello(name):
    print('hello ' + name)

hello("Sensei")
hello("Jiraya")

###### RETURN STATEMENTS ####

len('Hello')
print('hello has ' + str(len("hello")) + ' letters in it')

###################

def plusone(num):
    return num + 1

NewNum = plusone(6)
print(NewNum)


print('hello')
print('mate')
print('hello', end='')
print('mate')

print('a', 'b', 'c')
print('a', 'b', 'c', sep='&')
print('a', 'b', 'c', sep='\n')


data = [
        ['year', 'last', 'first'],
        [1943, 'Idle', 'Eric'],
        [1939, 'Cleese', 'John']
        ]

for row in data:
    print(row, sep=',')

print('==========')

for row in data:
    print(*row, sep=',')

print('==========')

print(*row, sep=' ', end='\n', file=sys.stdout, flush=False)

