## lists are immutable

spam = 'This is a test'

print(spam[8])

# spam[8] = 'K'  --> This fails
print(spam[8])

####

spam = [1, 4, 2, 3, -4, 5, 0, -1]
cheese = spam
cheese[1] = 'someval'
print(spam)
print(cheese)

### COPY
import copy

spam = [1, 4, 2, 3, -4, 5, 0, -1]
cheese = copy.deepcopy(spam)
cheese[1] = 'someChange'
print(cheese)
print(spam)


print('some value ' + \
  'here')

spam = ['a',
        'b',
        'c']

print(spam)