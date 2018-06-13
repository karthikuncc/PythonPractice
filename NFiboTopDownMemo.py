#Memoization Algo
#1)Check if Cache table is not empty -->Return it
#2)If empty and base case--->store the base case and return it
#3)If empty and not base --->recurse the subproblems
#4)Finally update the Cache table and return


fib_cache={}
def NFiboDP(n):
    
    #Check if n in cache
    if n in fib_cache:
        return fib_cache[n]
    
    #Compute Nth Fibonacci
    if n==1:
        result=0
    elif n==2:
        result=1
    elif n>2:
        result=NFiboDP(n-1)+NFiboDP(n-2)
    #Cache the Value and return
    fib_cache[n]=result
    return result

    #Fibonacci N Numbers
for n in range(1,1001):
    print(n,":",NFiboDP(n))

