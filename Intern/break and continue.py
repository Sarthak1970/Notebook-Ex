
'''
#break

print("Before")
for i in range(10):
    print(i)
    if i == 5:
        print("I is 5")
        break
    print("Here")

print("After")
'''

#continue - will skip a particular iteration

print("Before")
for i in range(10):
    print(i)
    if i == 5:
        print("I is 5")
        break
    print("Here")
    print("Here2")

print("After")