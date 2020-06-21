'''

Loops - You use loops to repeat a line or a set of lines few number of times.
Avoids duplication of lines.

Types of loops present in general:

While
Do-While -- Python does not support this.
For

Python has only for and while loop

'''

'''

for loop

For loop is written with RANGE() and without RANGE()

Range can have either 1 parameter, 2 parameters or 3 parameters

'''

#With Range
'''
for i in range(15):
    print(i)
'''
'''
In the above loop
for is a keyword
i is a variable name - it can be anything a,b,c,etc
in is a operator
range is a inbuilt function

'''

#With Range and 2 parameters

#for i in range(5, 15):
#    print(i)

#With Range and 2 parameters

#for i in range(3, 31, 3):
#    print(i)


# For without Range()
# We use a datastructure instead of a range function

l1 = [5, 10, 15, 20, "Bangalore"]
d1 = {'Bangalore' : 45, 'Mumbai' : 50, 100 : "Hundred", 33.33 : 55}

#for i in l1:
#    print(i)

# only d1 will iterate over keys only
# d1.values() will iterate over values
# d1.items() will iterate over both

#for j in d1.items():
#    print(j)

for i in d1.items():
    print(i)
    #print(l1)