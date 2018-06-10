def rec_fib(n):
    #Recursion Fibonacci
    if n < 1:
        print("Incorrect input")
    #First Fibonacci Number is 0
    elif n==1:
        return 0
    #Second Fibonacci Number is 1
    elif n==2:
        return 1
    else:
        return rec_fib(n-1) + rec_fib(n-2)

print(rec_fib(10))
