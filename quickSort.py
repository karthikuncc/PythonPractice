

def quickSort(lst):
    quick(lst,0,len(lst)-1)
    return lst

def quick(lst,left,right):
    if left >= right:
        return
    pivot=lst[(left+right)//2]
    index=partition(lst,left,right,pivot)
    quick(lst,left,index-1)
    quick(lst,index,right)
    



def partition(lst,left,right,pivot):
    while left<=right:
        while lst[left]<pivot:
            left+=1
        while lst[right] > pivot:
            right-=1
        if left<=right:
            lst[left],lst[right]=lst[right],lst[left]
            left+=1
            right-=1
    return left

if __name__== '__main__':
    print(quickSort([3, 4, 8, 0, 6, 7, 4, 2, 1, 9, 4, 5]))