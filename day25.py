# manipulating tuples
countries =("india","pakisthan","nepal","chiana")
print(countries)
temp = list(countries) #convert tuple to list
temp.append("Russia")
# countries=tuple(temp) #convert list to tuple
# print(countries)

temp.pop(temp.index("india"))
countries=tuple(temp)
print(countries)
#we can use all modification to make any change i tuple but most important condition is 
#that tuple shoul firstly converted in list then any chqnge will happen
