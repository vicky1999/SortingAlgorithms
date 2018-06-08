def quicksort(S):
    if len(S) == 0 or len(S) == 1:
        return S
    l, e, g = [], [], []
    for elem in S:
        if elem < S[0]:
            l.append(elem)
        elif elem == S[0]:
            e.append(elem)
        else:
            g.append(elem)
    return quicksort(l) + e + quicksort(g)

if __name__ == '__main__':
    array = [2,4,3,5,1,6,7,13,12,10,11]
    print(quicksort(array))
