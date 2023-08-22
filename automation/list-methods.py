spam = ['he', 'hel', 'hello', 'hey']
spam.index('hey')
spam.index('he')
#spam.index('something') ## This will fail

spam = ['he', 'hel', 'hello', 'hey', 'hel']
spam.index('hel')
print(spam)
### APPEND
spam = ['he', 'hel', 'hello', 'hey', 'hel']
spam.append('holla')
print(spam)

### INSERT

spam.insert(1, 'hoho')
print(spam)

### REMOVE
spam.remove('hel')
print(spam)

### DELETE
del spam[0]
print(spam)

### SORT
spam = [1, 4, 2, 3, -4, 5, 0, -1]
spam.sort()
print(spam)

spam = ["a", "v", "b", "s", "c", "f"]
spam.sort()
print(spam)

spam = ['A', 'b', 'B', 'a']
spam.sort()
print(spam)

spam.sort(key=str.lower)
print(spam)