
def merge(left,right):
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

#The loop may break before all elements are copied hence append the remaining elements
    result += left[i:]
    result += right[j:]
    return result


def mergesort(lst):
    #Base case when list has one element it is sorted
    if len(lst)<=1:
        return lst
    
    #calculate mid
    middle=len(lst)//2
    left=mergesort(lst[:middle])
    right=mergesort(lst[middle:])
    return merge(left,right)

if __name__== '__main__':
    print(mergesort([3, 4, 8, 0, 6, 7, 4, 2, 1, 9, 4, 5]))