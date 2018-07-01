


def bubbleSort(lst):
    isSorted=False
    lastUnsorted=len(lst)-1
    while not isSorted:
        isSorted=True
        for i in range(lastUnsorted):
            if lst[i]>lst[i+1]:
                lst[i],lst[i+1]=lst[i+1],lst[i]
                isSorted=False
        lastUnsorted-=1
    return lst

    



if __name__== '__main__':
    print(bubbleSort([3, 4, 8, 0, 6, 7, 4, 2, 1, 9, 4, 5]))