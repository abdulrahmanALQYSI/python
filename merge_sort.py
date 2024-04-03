
numbers = [6, 5, 4 ,2]
def merge_sort(list):
    
    """
    this is a merge sort algorithm which takes the list and divide to half 
    and than recurvilly do it till it reach to one element on each list and than sort and merge

    it follow the divide and concire approch
    """

    if len(list) <= 1:
        return list
    
    leftSide , rightSide = split(list)
    left = merge_sort(leftSide)
    right = merge_sort(rightSide)

   

    return merge(left , right)

   

 

def split(list):
    halfList = len(list) // 2
    leftSide = list[: halfList]
    rightSide = list[halfList:]

    return leftSide, rightSide

def merge(left, right):
    
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else :
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


print(merge_sort(numbers))

 
 

