##default function
# def isgreater(a=400, b=50):
#   if(a > b):
#     print("first number is greater that is: ", a)
#   else:
#     print("second number is greater or equal", b)

# isgreater()
# print("out of the function")
# isgreater(b=30)
# isgreater(a=1,b=2)
# isgreater(70)
# def name(fname, mname = "Jhon", lname = "Whatson"):
#     print("Hello,", fname, mname, lname)

# name("Amy")

# def tsum(a=20,b=30):
#   sum = a + b
#   print("sum of numbers is: ", sum)
# # print(sum)
# tsum()

#in default function , after it we can use key values to print
#  and their order doesnot matter "key=value"
# def pname(fname, mname= "mayank", cname="kannu"):
#   print("fname: ",fname,", mname: ", mname,", cname: ", cname)
# # pname("kaveri")
# pname("kavi", mname="moksh")


#variable length arg
#arbitrary, keyword arbitrary variable length

##arbitrary arg
# def names(*name):
#   print("list of names: ", name[0],"and",name[1])
# names("xukai","renan")

# ##keyword arbitrary
# def rollno(**rno):
#   print("list of roll numbers: ", rno["num1"], "and", rno["num2"])
# rollno(num1 = 123,num2 = 234)

##return stmt
def names(fname, mname, cname):
  return fname +","+ mname +","+ cname
print(names("kavi","raghu","saavi"))