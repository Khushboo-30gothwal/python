for k in range(1,400):
  k = k + 1
  print(k)
  k = k * k
  print(k)
  if (k % 100 == 0):
    print("now i am going to skip code part where k is: ", k)
    break
  else:
    print("condition abhi tk true nhi hui where k is: ", k)
  # k = k + 1
  # print("skip the code part")
print("out of the loop")
