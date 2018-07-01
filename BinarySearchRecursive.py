def BinarySearchRecursive(lst,item):
    low=0
    high=len(lst)-1
    if len(lst)==0:
        return '{item} was not found'.format(item=item)
    else:
        mid=(low+high)//2
        if lst[mid]==item:
            return  '{item} found'.format(item=item)
        elif lst[mid]< item:
            return BinarySearchRecursive(lst[low+1:], item)
        else:
            return BinarySearchRecursive(lst[:mid], item)
test_list = [1,3,9,11,15,19,29]
test_val1 = 25
print(BinarySearchRecursive(test_list, test_val1))
