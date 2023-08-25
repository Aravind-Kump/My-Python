###############################
##### INTERACTIVE SCRIPT   ####
###############################

print("hello !")
print("What is your name?")
name = input()
print("Hey," + name + "!")     ### This will form a proper sentence with required spaces
print("Hey," + name, "!")      ### This gives some space next to the variable
print("Length of given name is:", len(name))
print("What's the time??")
time = input()                 ### Input always takes only string values
print("It will be " + str(float(time) + 1) + ' after an hour')    #### Float to pass floating values like 10.25 in the interger

###############################
##### COMPARISON OPERATORS ####
###############################
### if statements ###
name = "Python"

if name == 'Python':
    print('Hello Python')
print('########### DONE ###########')


### if else statements ###
password = 'mypassa'
if password == 'mypass':
    print('Access Granted')
else:
    print('Wrong Password')

### if elif statements ###
name = 'Python2'
age = 50
if name == 'Python':
    print('Hi Python')
elif age > 50:
    print('Incorrect age')
elif age < 14:
    print('Python is elder')
elif age == 52:
    print('Python is 50 years old')
elif age > 14:
    print('Python is elder')

## Truthy and Falsey values

print('Enter a name')
name = input()
if name:
   print("Thanks for the details")
else:
   print("You do not provided any details")

print('Enter a name')
name = input()
if name != '':
   print("Thanks for the details")
else:
   print("You do not provided any details")