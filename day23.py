# # #list methods
# # sort() to sort list items in ascending order
# # index() to find first occurence of given item in list
# # count() to repition of given item in list
# # reverse() to reverse the given list without changing their order
# # reverse=True as parameter give` decending order of list items and change their order
# # copy() to copy list item without changing their order if any
# # operation perform on copied list then original list donot chnage in thier items
# # append() to add more items in list , at the end of list
# # insert() to insert item in list an given specific position
# # extend() to add an entire list to end of the another list
# # concatenating two list using '+' operator
# lt = [1, 2, 345,657,798,123, 34,56,8765,463,74,2,5,76]
# print(lt)
# lt.sort()
# print(lt)
# lt.sort(reverse=True)
# print("decreasing order: ",lt)
# #reverse()
# lt.reverse()
# print("reverse order: ",lt)
# print(len(lt))
# print(lt.index(34))
# print(lt.index(657))
# colors = ["voilet", "green", "indigo", "blue", "green"]
# print(colors)
# # print(colors.index("green"))
# print(colors.count("green"))

# num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
# print(num)
# # print(num.index(3))
# print(num.count(2))
##normal copy way
#this way original list change so this is not an effective way
# m[0] = "10000"
# print(num)
#using copy() method
# m = num.copy()
# m[0] = 11110
# print("original: ",num)
# print("copies: ",m)

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num)
# num.append(234)
# print(num) 
# num.insert(5,27)
# print(num)
num2 = [234,435,345]
print(num2)
# num.extend(num2) # extend() method
print(num + num2)#concatenating of two list