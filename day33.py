# dictionary in python
dict = {'name':'arif', 'branch':'cse', 'batch':2024}

print(dict)

for key in dict:
  print(f"the dictionary key {key} is {dict[key]}")

# accessing single values:
print(dict.get('name'))

# accessing multiple values using values() mrthod:
print(dict.values())

# accessing multiple values using keys() method:
print(dict.keys())

# accessing key-value painrs uaing items() method:
print(dict.items())

