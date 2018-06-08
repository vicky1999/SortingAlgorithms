import random #always a promising import :)
def bogosort(S):
    sorted = False
    copyS = S[:]
    while not sorted: #NOTE This could theoretically never exit...
        checked = [False]*len(S)
        length = len(S)
        for i in range(0, length):
            index, checked = getUniqueRand(checked, length)
            S[i] = copyS[index]
        if isSorted(S):
            sorted = True
            return S

def isSorted(S):
    for i in range(0, len(S) - 1):
        if S[i] > S[i + 1]:
            return False
    return True

def getUniqueRand(checked, length):
    unique = False
    while not unique:
        randomInt = random.randint(0, length - 1)
        if not checked[randomInt]:
            checked[randomInt] = True
            unique = True
            return randomInt, checked


if __name__ == '__main__':
    array = [2, 4, 1, 6, -2, 10, -4, 7]
    print(bogosort(array))
