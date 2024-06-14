a = int(input("enter your number:"))
b = int(input("enter the total number:"))

p = a/b * 100
print("percentage is:",p)

if(p >= 0):
  if(p >=34):
    if(p >= 34 and p <= 60):
      print("recieve gade c")
    elif(p >60 and p <= 80):
      print("recieve grade b")
    elif(p > 80 and p <= 90):
      print("recieve grade A")
    elif(p > 90):
      print("receieve grade A+")
  else:
    print("you are fail")
else:
  print("numbers can't be negative")