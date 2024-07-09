# else can be used with for and while loop
# in loop else represnts the successfull compalation of that loop
# it does not related to breaking the loop

# in case of for loop
# for this loop sucessfully executed
for i in range(5):
  print(i)

else:
  print("not in i")

# incase for while loop
j = 0
while j<7:
  print(j)
  j = j+1

else:
  print("not in i")

# for this loop is not sucessfully executed
for i in range(6):
  print(i)
  if i == 5:
    break

else:
  print("not in i")

# in case of while looping
j = 0
while j<7:
  print(j)
  j = j+1
  if i == 3:
    break

else:
  print("not in i")

for x in range(5):
  print ("iteration no {} in for loop".format(x+1))
else:
  print ("else block in loop")
print ("Out of loop")