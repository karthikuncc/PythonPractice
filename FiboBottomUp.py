memo={1:0,2:1}
def Fib(n):
    for i in range(3,n+1):
        memo[i]=memo[i-1]+memo[i-2]
    #print(memo[n])
    return memo[n]
for i in range(1,10):
    print(Fib(i))