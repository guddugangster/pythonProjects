# Program to display the Fibonacci sequence up to n-th term

n = int(input("How many terms? "))
Fibonacci(n)

#Fibonacci Using recursion
def Fibonacci(n):
    if n<=0:
        print("Incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 
print(Fibonacci(9))
