#if condition
def a_name():
    '''
    This is a sample definition
    :return:
    '''
    print("Enter a name")


a_name()
name = input()
if name == "alice":
    print("Hello alice")
print("done")

print('#using same definition and trying multiple FOR loops#')

a_name()
name = input()
if name == "alice":
    print('Hello alice')
print('done')

a_name()
name = input()
print("HELLO " + name)

print(a_name.__name__)
print(a_name.__doc__)