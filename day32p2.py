#isdisjoint():means donot have common elements
####does both set have any common elements or not
# ##if have the sets are not disjoint else they are disjoint
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# print(cities.isdisjoint(cities2))
# print(cities.intersection(cities2))  ##set have common elements

# ###issupserset():chosen et items are present in original set or not
# ##true means have all items of chosen set in original set
# ##false means donot have all items of chosen set in original set
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul"}
# print(cities.issuperset(cities2))
# cities3 = {"Seoul", "Madrid","Kabul"}
# print(cities.issuperset(cities3))

# ##issubset():chosen items are present in original set or not
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Delhi", "Madrid"}
# print(cities2.issubset(cities))

# ##add():to an item in given set
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

# ##update():adding more then one items in set
# ##adding set ,list,tuples and dictionary into existing set
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Helsinki", "Warsaw", "Seoul"}
# cities.update(cities2)
# print(cities)

# ##remove() or delete(): to remove an item from set
# ##basic difference between them is when item is not present
# ##in set then remove() raise and error but delete() donot raise an error
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.remove("Tokyo")
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.remove("Seoul")
# print(cities)

# ##pop():remove last from set but in unordered set we cannot find which item
# ##is popped
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# item = cities.pop()
# print(cities)
# print(item)

# ##del:keyword which delete entire set
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities
# print(cities)

# ##clear():method to clear all items from set nd remaining with empty set
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.clear()
# print(cities)

# ##check if item exists: item is present in set or not
# info = {"Carla", 19, False, 5.9}
# if "Carla" in info:
#     print("Carla is present.")
# else:
#     print("Carla is absent.")
