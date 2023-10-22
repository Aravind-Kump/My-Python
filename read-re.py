import sys
import re

for x in sys.argv[1:]:
    with open(x, 'r+') as f:
        collection = []
        data = f.readlines()
        for line in data:
            # if "." in line and "namespace" not in line and "_" not in line and "ldap" not in line:
            #     a = line.split(":")
            #     copy = a[0].replace(".", "_").upper()
            #     collection.append(copy + ":" + a[1])
                a = line.split(":")
                print( a[0])
                print( a[1])
                #print(copy)

        #     if "." in line and "namespace" not in line and "_" not in line and "ldap" not in line:
        #         a = line.split(":")
        #         copy = a[0].replace(".", "_").upper()
        #         collection.append(copy + ":" + a[1])
        # f.write('\n')
        # for i in collection:
        #     f.write(i)
