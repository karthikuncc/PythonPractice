bottom_up={1:1,2:2,3:4}
def stairCaseBottomUp(n):
    for i in range(4,n+1):
        bottom_up[i]=bottom_up[i-1]+bottom_up[i-2]+bottom_up[i-3]
    return bottom_up[n]
for i in range(1,10):
    print(stairCaseBottomUp(i))

    #Bottom-Up DP--Algo
    #1) Bottom Up Dictionary-->Initialize base cases
    #2)Def Func(n):
            #for i in range(notBasecase,n+1):
            #bottom_up[i]=bottom_up[i-1]+bottom_up[i-2]+...
    #3) Return bottom_up[n]
    #4) Func Call (i)
