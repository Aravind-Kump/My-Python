some = 0
while some < 5:
    print("Loop with while condition which runs following times", some)
    some = some + 1

some = 0
if some < 5:
    print('Loop with if condition which runs', some,'(1) time')
    some = some + 1

##########################
### TYPE YOUR NAME LOOP ##
##########################

name = ''
while name != 'your name':
     print('Please type your name')
     name = input()
print('Thanks')
############
#### OR ####
############
name = ''
while True:
    print('Please enter your name')
    name = input()
    if name == 'your name':
        break
print('Thank you')

#### Continuous loop ####
#while True:
#    print("hello")
##########################


some = 0
while some < 5:
    print("Loop with while condition which runs following times", some)
    some = some + 1
    if some == 3:
        continue
    print('some is ' + str(some))


###############################
####### FOR LOOP ##############
###############################
print('My name is')
for i in range(5):
    print('Kakashi ' + str(i))

print('My name is')
i = 0
while i < 5:
    print('Naruto ' + str(i))
    i = i + 1


total = 0
for num in range(101):
    total = total + num
print(total)
print(num)

for i in range(33, 45):
    print('gaara' + str(i))

for i in range(5, -1, -1):
    print('gaara' + str(i))