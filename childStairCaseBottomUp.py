bottom_up={1:1,2:2,3:4}
def stairCaseBottomUp(n):
    for i in range(4,n+1):
        bottom_up[i]=bottom_up[i-1]+bottom_up[i-2]+bottom_up[i-3]
    return bottom_up[n]
for i in range(1,10):
    print(stairCaseBottomUp(i))