pie = "applepie"
length = len(pie)

print(length)

print(pie[:5]) #it will automatically take starting index 0 zero incase it is not given
print(pie[5:]) #it will automatically taking ending index equal to it's length incase not given 
print(pie[2:6])
print(pie[-8:])
print(pie[:-5])
print(pie[-8:-2]) #print(pie[len(pie)-8:len(pie)-2])


alphabets = "ABCDE"
for i in alphabets:
  print(i)