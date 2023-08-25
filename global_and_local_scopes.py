spam = 42 ## Global Variable

def eggs():
    spam = 42 ## Local Variable

print('some')
print('some more')

def spam():
    eggs = 99
    print(eggs)

spam()
print(eggs)
##################################################
#### LOCAL VARIABLE ####
##################################################
def spam():
    eggs = 99
    bacon()
    print(eggs)
def bacon():
    ham = 22
    eggs = 0

spam()

##################################################
####### GLOBAL VARIABLE ##
##################################################
def spam():
    print(eggs)

eggs = 33
spam()


#####
#####
def spam():
    eggs = 'Hey'
    print(eggs)

eggs = 22
spam()
print(eggs)

###########
## TO STICK FOR GLOBAL VARIABLE
###########
def spam():
    global eggs
    eggs = 'Hey'
    print(eggs)

eggs = 22
spam()
print(eggs)
