# x =int(input("enter the value of x: "))

# match x:
#     case 0:
#       print("x is zero")
#     case 1:
#       print("x is a natural number")
#     case _ :
#       print("x can be negative, float and greater then 1 and x = ", x)
x = int(input("enter the value of x is: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _ if x % 2 == 0:
      print("x % 2 == 0 and x = ", x)
    case _:
        print(x)