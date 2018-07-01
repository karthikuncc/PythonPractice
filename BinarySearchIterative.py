def BinarySearchIterative(lst,item):
    low=0
    high=len(lst)-1

    while low<=high:
        mid=(low+high)//2
        if  lst[mid] == item:
            return item
        elif lst[mid]< item:
            low = mid +1
        else:
            high=mid-1
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 29
print(BinarySearchIterative(test_list, test_val1))

    