# # error handling using "try", "except"
# a = input("enter the value: ")

# print(f"multiplication table of {a} is: ")
# try:
#   for i in range(1, 11):
#     print(f"{int(a)} x {i} = {int(a) * i}")

# except:
#   print("invalid index")

# print("code completed without error")

try:
  num = int(input("Enter an integer: "))
  a = [6, 3]
  print(a[num])
except ValueError:
  print("Number entered is not an integer.")

except IndexError:
  print("Index Error")
