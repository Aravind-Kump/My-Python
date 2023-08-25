#count items

import time

# def count_items(items):
#     print('Counting ', end='')
#     num = 0
#     for item in items:
#         num += 1
#         print('.', end='')
#     print(f'/nThere were {num} items')
#
# from count_items import count_items
#
# pythons = ['cola', 'mint', 'salt']
#
# count_items(pythons)
#
#
# import time
#
# def count_items(items):
#     print('Counting ', end='', flush=True)
#     num = 0
#     for item in items:
#         num += 1
#         time.sleep(1)
#         print('.', end='', flush=True)
#
#     print(f'\nThere were {num} items')



def sentences():
    print('one', end='. ')
    print('two', end='. ')
    print('three', end='. ')

sentences()

def planets():
    print('Mercury', 'Venus', sep=',', end=',')
    print('Earth', 'Mars', sep=',', end=',')
    print('Jupiter', 'Saturn', sep=',', end=',')
planets()

def planets():
    print('Planets:', end='\n *')
    print('Mercury', 'Venus', end='\n *')
    print('Earth', 'Mars', sep=',', end='\n *')
    print('Jupiter', 'Saturn', sep=',')
planets()