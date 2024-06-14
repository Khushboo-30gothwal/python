# ##function in python
# # normally we write code like
# a = 10
# b = 20
# gmean = (a*b)/(a+b)#geometric means
# print(gmean)

# # do it for n numbers of element like that
# def calculatemean(a,b):
#   mean = (a*b)/(a+b)
#   print(mean)
# a = 8
# b = 10
# c = 22
# d = 40
# calculatemean(a,b)
# calculatemean(a,c)
# calculatemean(c,b)
# calculatemean(a,d)


#function fro comparision code
def isgreater(a,b):
  if(a>b):
    print("first is greater",a)
  else:
    print("maybe second is greater or equal",b)

a = 8
b = 10
c = 22
d = 40

isgreater(a,b)
isgreater(a,c)
isgreater(c,b)
isgreater(a,d)