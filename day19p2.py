#continue only skip iteration that follows given condition
i = int(input("enter the value: "))
for k in range(1, i):
  k = k + 1
  print("k value for condition trial is: ",k)
  if(k%7 != 0):
    print("value of k is: ", k)
    continue
  else:
    print("............condition false.........")
print("out of the loop")