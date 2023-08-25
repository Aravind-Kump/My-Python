###ERROR##
# def div42by(dividedby):
#     return 42 / dividedby
#
# print(div42by(2))
# print(div42by(3))
# print(div42by(12))
# print(div42by(0))

#### EXCEPTION TO TRY AND PROCEED FURTHER
def div42by(dividedby):
    try:
        return 42 / dividedby
    except ZeroDivisionError:
        print('Error: You tried to divide by zero')
print(div42by(2))
print(div42by(3))
print(div42by(12))
print(div42by(0))
####
#OR#
####
def div42by(dividedby):
    try:
        return 42 / dividedby
    except:
        print('Error: You tried to divide by zero')
print(div42by(2))
print(div42by(3))
print(div42by(12))
print(div42by(0))


##########################

print('How many cats do you have')
numCats = input()
if int (numCats) >= 4:
    print('That is lot')
else:
    print('That is not many')
