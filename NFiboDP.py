fib_cache={}
def NFiboDP(n):
    
    #Check if n in cache
    if n in fib_cache:
        return fib_cache[n]
    
    #Compute Nth Fibonacci
    if n==1:
        value=0
    elif n==2:
        value=1
    elif n>2:
        value=NFiboDP(n-1)+NFiboDP(n-2)
    #Cache the Value and return
    fib_cache[n]=value
    return value

    #Fibonacci N Numbers
for n in range(1,1001):
    print(n,":",NFiboDP(n))

