

l1 = []
print(l1)
print(type(l1))
a = 10
c = type(a)
l1 = [c]

'''

List is represented using []

You can store int, floats, strings and any other datatype/datastructure in a single list.

Datatstructures are list, tuple, dict, etc.. Where combination of different datatypes can be inserted in one place holder
Datatype are int, float, strings, etc. It defines the type of value a placeholder contains 

List has few inbuild functions
append() - Will add number to the end
insert() - will insert value at specified index
count() - it will return you number of occurences
index() - it will return you the index of an element
sort() - will sort ascending to descending
reverse() - will reverse list element
'''

l2 = [5, 10, 15.33, "India", -99.003]

#print(l2[3])
#print(type(l2[4]))
l2.append(500)
#print(l2)

l2.insert(1,1000)
#print(l2)

l3 = [5, 5, 10, 15, 20, 5, 25, -5, 10]
count = l3.count(5)
print(count)

print(l3.index(10))
l3.sort()
l3.sort(reverse=True)
print(l3)

l3.reverse()
print(l3)



'''
remove() - 1,0
append() - 1, 0
insert() - 2, 0
count() - 1, 1
index() - 1, 1
sort() - 0 (One optional parameter), 0 
reverse() 0,0

'''
