print('How many pets do you have ?')
numPets = input()

try:
   if int(numPets) >= 4:
      print('You have a lot of pets')
   else:
      print('That is not that many pets')
except ValueError:
   print('No number was passed!')

#############################################

def div42by(dividedBy):
   try:
      return 42 / dividedBy
   except ZeroDivisionError:
      print('ERROR: You tried to divide by zero')

print(div42by(3))
print(div42by(2))
print(div42by(30))
print(div42by(0))
print(div42by(1))
