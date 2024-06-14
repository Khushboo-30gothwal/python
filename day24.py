#tuples in python
# tup = (1,2,3,56,778,34,2345,565,4,23)
# print(type(tup), tup)
# tup1 = (1,)#it is a tuple
# print(type(tup1), tup1)
# tup1 = (1)#it is an integer type
# print(type(tup1), tup1)
# tuple1 = (1,2,2,3,5,4,6)
# tuple2 = ("Red", "Green", "Blue")
# print(tuple1)
# print(tuple2)
# details = ("Abhijeet", 18, "FYBScIT", 9.8)
# print(details)
########tuple indexes
##positive indexing
# tup = (1,2,3,56,778,34,2345,565,4,23)
# print(tup)
# print(tup[0])
# for i in range(10):
#   if i <= 9:
#     print("index no is :",i,"is have the item: ",tup[i])
#   else:
#     print("out of the range")
# # i = 0
# while(i <= 8):
#   print("index no is :",i,"is have the item: ",tup[i])
#   i = i+1
#negative indexing
# tup = (1,2,3,56,778,34,2345,565,4,23)
# print(tup)
# # print(len(tup))
# # # print(tup[-1])
# # print(tup[len(tup)-1])
# # print(tup[10-1])
# # print(tup[9])
# if 778 in tup:
#   print("yes")
# else:
#   print("no")
# country = ("Spain", "Italy", "India", "England", "Germany")
# # if "Germany" in country:
# #     print("Germany is present.")
# # else:
# #     print("Germany is absent.")
# print(country[1:4])#positive range
# print(country[1:-3])#negative range
# animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
# print(animals[3:7])     #using positive indexes
# print(animals[-7:-2])   #using negative indexes
# animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
# # print(animals[4:])      #using positive indexes
# # print(animals[-4:])     #using negative indexes
# #printing all elements frm start
# print(animals[:6])      #using positive indexes
# print(animals[:-3])     #using negative indexes
#print alternative values
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[::2])     #using positive indexes
print(animals[-8:-1:2]) #using negative indexes