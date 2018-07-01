def InsertionSort(lst):

    for i in range(1,len(lst)):
        #Taking second card as key
        key=lst[i]
        j=i-1

        while j>=0 and lst[j]> key:
            lst[j+1]=lst[j]
            j-=1
        lst[j+1]=key
    return lst

arr = [12, 11, 13, 5, 6]
print(InsertionSort(arr))


