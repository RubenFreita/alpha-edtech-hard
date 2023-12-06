# Dicionários em Python

# Dicionario vazio
dic1 = {}
print(dic1)
print()

# key-value pairs 
dic1 = {1:'Pyton', 2:'Java'}
print(dic1)
print()

dic1 = {'First': 'Python', 'Second': 'Java'}
print(dic1)
print()
#
dic1['Second'] = 'C++'
print(dic1)
print()
#
dic1['Third'] = 'Ruby'
print(dic1)

#pop element
a = dic1.pop('Third')
print('Value:', a)
print('Dictionary:', dic1)
print()

#pop the key-value pair
b = dic1.popitem()
print('Key, value pair:', b)
print('Dictionary', dic1)
print()

#empty dictionary
dic1.clear()
print(dic1)
