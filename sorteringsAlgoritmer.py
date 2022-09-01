import random, copy



if __name__ == '__main__':
    l = list(range(0, 5))
    lb = l.copy()
    for i in range(50):
        random.shuffle(lb)
        ## Kald den funktion, du vil teste
        ls = bogoSort(l)
        ## Kald den funktion, du vil teste
        if ls != l:
            print('Fejl! Algoritmen kan ikke sortere.')
            break
    print('Succes! Algoritmen sorterer korrekt.')
    print('blandet: ', lb)
    print('sorteret:', ls)

def abubbleSort(array):
    for o in range(len(array)):
        for i in range(len(array)):
                if i != len(array)-1 and array[i] > array[i+1]:
                    temp = array[i+1]
                    array[i+1] = array[i]
                    array[i] = temp
    return array

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array






def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        l = i-1
        while l >= 0 and key < array[l]:
            array[l+1] = array[l]
            l = l-1
        array[l+1]= key
    return array



def insertionSort(arr):
    for i in range(len(arr)):
        while i>i+1 and i>i-1:
            if i>i+1:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            if i>i-1:
                arr[i], arr[i-1] = arr[i-1], arr[i]
    return arr
