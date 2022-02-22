ani = ["cat", "bat", "dog"]
print(ani[0])
print(ani.index('cat'))
print(ani.index('dog'))



pets = [['cats','dogs'],['parrot','owl']]
print(pets[0])
print(pets[1][1])

pets.append('moose')

print(pets)

pets.append('mangose')

print(pets)

ani = ['cats', 'rats', 'dogs', 'fish', 'kitty']
print(ani)
ani.remove('cats')

print(ani)
print("")
print('###################')
print('SORT FUNCTIONALITY :')

int = [1,4,2,0.5,-1,0,12]
int.sort()
print(int)

ani.sort()
print(ani)

print("SORT REVERSE :")
ani.sort(reverse=True)
print(ani)

alpha = ['a', 'B', 'A', 'b']
alpha.sort()
print(alpha)
alpha.sort(key=str.lower)
print(alpha)