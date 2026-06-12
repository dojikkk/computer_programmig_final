"""
Recursive mergesort sorting algorithm implementation.
"""


def mergeSort(slist):
    """Recursive mergesort, divide and conquer."""
    if len(slist) <= 1:
        # Trivially sorted, early exit:
        return
    # If we fall through here it means our list has at least 2 elements
    print("Dividing: ", slist)
    mid = len(slist) // 2
    lefthalf = slist[:mid]
    righthalf = slist[mid:]

    mergeSort(lefthalf)
    mergeSort(righthalf)

    #
    # Merge sorted halfs:
    #
    LeftCount = 0
    RightCount = 0
    GlobalCount = 0

    while LeftCount < len(lefthalf) and RightCount < len(righthalf):
        if lefthalf[LeftCount] < righthalf[RightCount]:
            slist[GlobalCount] = lefthalf[LeftCount]
            LeftCount += 1
            GlobalCount += 1
        else:
            slist[GlobalCount] = righthalf[RightCount]
            RightCount += 1
            GlobalCount += 1

    # Collect remainder from left half (if any):
    while LeftCount < len(lefthalf):
        slist[GlobalCount] = lefthalf[LeftCount]
        LeftCount += 1
        GlobalCount += 1

    # Collect remainder from right half (if any):
    while RightCount < len(righthalf):
        slist[GlobalCount] = righthalf[RightCount]
        RightCount += 1
        GlobalCount += 1

    print("Merged:   ", slist)


slist = [2, 22, 23, 4, 8, 99, 78, 98, 100]
mergeSort(slist)
print(slist)
