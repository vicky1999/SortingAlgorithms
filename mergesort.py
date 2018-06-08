import math

def mergesort(S):
    n = len(S)
    if n == 1:
        return S
    halfway = math.ceil(n/2)
    l, r = [], []
    for i in range (0, halfway):
        l.append(S[i])
    for j in range(halfway, n):
        r.append(S[j])

    left = mergesort(l)
    right = mergesort(r)

    leftLen = len(left)
    rightLen = len(right)

    retArr = []

    i, j = 0, 0
    while i < leftLen and j < rightLen:
        if left[i] < right[j]:
            retArr.append(left[i])
            i+=1
        else:
            retArr.append(right[j])
            j+=1
    while i < leftLen:
        retArr.append(left[i])
        i+=1
    while j < rightLen:
        retArr.append(right[j])
        j+=1
    return retArr

if __name__ == '__main__':
    testarray = [2,4,3,5,1,6,7,13,12,10,11]
    print(mergesort(testarray))
