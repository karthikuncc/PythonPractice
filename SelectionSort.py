def SelectionSort(lst):
    
    for i in range(len(lst)):
        min_index=i

        for j in range(i+1,len(lst)):
            if  lst[j]<lst[min_index]:
                min_index=j
                
        #Swap found with Minimum
        lst[i],lst[min_index]=lst[min_index],lst[i]
    return lst


arr = [12, 11, 13, 5, 6]
print(SelectionSort(arr))
