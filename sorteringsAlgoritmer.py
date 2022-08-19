import random, copy



"""""
def abubbleSort(array):
    for o in enumerate(array):
        for i in enumerate(array):
                if array[i]>array[i+1]:
                    temp = array[i+1]
                    array[i+1] = array[i]
                    array[i] = temp
"""

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
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




def insertionSort(array):
    for i in range(len(array)):
        while i>i+1:
            array[i], array[i+1] = array[i+1], array[i]
        if i>i-1:
            array[i], array[i-1] = array[i-1], array[i]
            return array




