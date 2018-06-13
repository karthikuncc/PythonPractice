bottomUp={1:0,2:1}
def Fib(n):
    for i in range(3,n+1):
        bottomUp[i]=bottomUp[i-1]+bottomUp[i-2]
    return bottomUp[n]
for i in range(1,10):
    print(Fib(i))