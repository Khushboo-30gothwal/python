########################ex1##################
#union and intersection set methods
l1 = {1,3,4,5,6}
l2 = {3,5,6,1,7,2}

print(l1.union(l2))#l1 union l2
# print(l1.intersection(l2))#l1 intersection l2

# #update in both set methods
# l1.update(l2)
# print(l1)
# # in updation l1 have it's own and thos element that are present in l2 but not in l1

# #intersection_update
# l1.intersection_update(l2)
# print(l1)
# print common elements between two sets

###symmetric_difference() and  symmetric_difference_update()
# l3 = l1.symmetric_difference(l2)
# print(l3)

# #symmetric_difference():: non-common elements of given sets and store it into other set
# l1.symmetric_difference_update(l2)
# print(l1)
##symmetric_difference_update() also give output like symmetric_difference() but
## it update the original set but symmetric_difference() donot update
## original set rather then store it into anither set

# #difference() and difference_update()
# l3 = l1.difference(l2)
# l4 = l2.difference(l1)
# print(l3)
# print(l4)

###difference(): output of original set's elements those are not in present in other set

# l1.difference_update(l2)
# print(l1)
# l2.difference_update(l1)
# print(l2)

###difference_update():make changes like difference() but store changes in
# ## original set rather then new_set

###############ex2###############
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# # ##union and update
# cities3 = cities.union(cities2)
# print(cities3)
# cities.update(cities2)
# print(cities)

# ##intersection and intersection_update()
# cities3 = cities.intersection(cities2)
# print(cities3)
# cities.intersection_update(cities2)
# print(cities)

# ##symmetric_difference() and symmetric_difference_update()
# cities3 = cities.symmetric_difference(cities2)
# print(cities3)
# cities.symmetric_difference_update(cities2)
# print(cities)

# ##difference() and difference_update()
# cities3 = cities.difference(cities2)
# print(cities3)
# cities.difference_update(cities2)
# print(cities)
