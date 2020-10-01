import random, math, sys

def insertionSort(items):
    items = items.copy()
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j-1] > items[j]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1
    return items

def selectionSort(items):
    items = items.copy()
    sorted = []
    while len(items) > 0:
        smallest = len(items)-1
        for i in range(len(items)):
            if items[i] < items[smallest]:
                smallest = i
        sorted.append(items.pop(smallest))
    return sorted

def bubbleSort(items):
    items = items.copy()
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items

def quickSort(items, l=0, r=None):
    sys.setrecursionlimit(sys.getrecursionlimit()+2)
    #print(items[l:r])
    if r == None:
        r = len(items)-1
        items = items.copy()
    i = l - 1
    pivot = r
    #print(l, r, items[l:r])
    if l < r:
        for j in range(l, r):
            if items[j] <= items[pivot]:
                i = i + 1
                items[i], items[j] = items[j], items[i]
        items[i+1], items[r] = items[r], items[i+1]
        i += 1
        #print(items[i])
        quickSort(items, l, i-1)
        quickSort(items, i+1, r)
    return items

def mergeSort(items):
    left = items[0:math.floor(len(items)/2)]
    right = items[math.floor(len(items)/2):len(items)]

    if len(left) > 2:
        left = mergeSort(left)
    elif len(left) == 2 and left[0] > left[1]:
        left[0], left[1] = left[1], left[0]

    if len(right) > 2:
        right = mergeSort(right)
    elif len(right) == 2 and right[0] > right[1]:
        right[0], right[1] = right[1], right[0]

    output = []
    while len(output) < len(items):
        #print('-------------------------------\nl:', left,'\nr:', right)
        if len(left) > 0 and len(right) > 0:
            if left[len(left)-1] < right[len(right)-1]:
                output.append(left.pop())
            else:
                output.append(right.pop())
        else:
            if len(left) == 0:
                output.append(right.pop())
            elif len(right) == 0:
                output.append(left.pop())
        #print('sorted:', output)
    return output


if __name__ == '__main__':
    l = list(range(0, 5))
    print(l)
    random.shuffle(l)
    print(l)
    l = mergeSort(l)
    print(l)
