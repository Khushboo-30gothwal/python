#factorial function defining
def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)


n = int(input("enter the integer: "))
print("factorial of",n," is: ",factorial(n))

####defining fibonacchi series
# fib(0) = 0
# fib(1) = 1
# fin(n) = fib(n-1) + fib(n-2)
def fib(n):
  if(n==0):
    return 0
  elif(n==1):
    return 1
  else:
    return fib(n-1) + fib(n-2)

a = int(input("enter the integer: "))
print("fibonacchi number of ",a,"is: ",fib(a))
