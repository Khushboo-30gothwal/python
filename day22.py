#list in  python
#list can have, numbers, strings in a single collection, different data types
# lst = [2,4,6, 8,"hii","akshu",True]
# print(lst)
#list indexing is same as string indexing and accessing list item
# print("list number at index 0 is: ",lst[0])#positive indexing
# print("list number at index 1 is: ",lst[1])
# #negative indexing
# #all way below is give same output through indexing
# print(lst[-2])
# print(lst[len(lst) - 2])#negative indexing performing way
# print(len(lst))
# print(lst[7-2])
# print(lst[5])
# #checking wheter item present in list or not
# if "akshu" in lst:
#   print("yes")
# else:
#   print("no")
# if "5" in lst:
#   print("yes")
# else:
#   print("no")
#range in indexing i n list
# print(lst[1:])
# # print(lst[1:len(lst)])
# # print(lst[1:3])
# print(lst[1:4])#startindex=1,endindex=4
# # print(lst[1:4:2])#jumpindex = 2
# lst = [2,4,6, 8,"hii","akshu",True]
# print(lst)
# print(len(lst))
# #range in indexing using negative indexing
#below is negative indexing example and how to get answer through it
# print(lst[1:-5])
# print(lst[1:len(lst) - 5])
# print(lst[1:7-5])
# print(lst[1:2])
# #printng item of list in a fix range
# print(lst[1:4])
# print(lst[-3:-2])
# print(lst[1:])#printing till end
# print(lst[:-3])#start 0 to given index
#printing alternative values
# print(lst[::2])#print(lst[0:len(lst):2])#the way it is in real
# #using negative values
# print(lst[-7:6:3])

#print every 3rd item

# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(len(animals))
# print(animals[1:8])
# print(animals[1:8:3])
#list comprehension
# newlst = [item for item in animals if "c" in item]
# print(newlst)
new_list = [i for i in range(10) if i%2==0]
print(new_list)
for i in new_list:
  print(i, i * i)
