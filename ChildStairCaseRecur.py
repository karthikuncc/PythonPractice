 #Recursive Child Staircase
def findStep(n):
    if n==1 or n==0:
        return 1
    elif n==2:
        return 2
    else:
        return findStep(n-3)+findStep(n-2)+findStep(n-1)

print(findStep(4))
