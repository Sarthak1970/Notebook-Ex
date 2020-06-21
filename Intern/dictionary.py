'''

Dictionary is represented using {}

word and meaning are a pair
Similaraly dictionary uses pair concept
where a pair consists of key and value

Dictionary does not have index concept

Syntax :

d1 = {key1 : value1 , key2 : value2}

'''

d1 = {}
print(d1)
print(type(d1))

d1 = {
    'Nikhil' : 40,
    'Ritesh' : 45,
    'Shweta' : 30,
}

print(d1['Ritesh'])

# Adding element to dictionary syntax is d1[key] = value
# New pair is Alex 50
d1['Alex'] = 50
print(d1)

d1['Ritesh'] = 55
print(d1)

# Remove a pair syntax is del d1[key]

del d1['Shweta']
print(d1)




