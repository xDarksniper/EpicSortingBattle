# TODO: Kør flere runder og tag gennemsnit

import time
import sorteringsAlgoritmer as algo
import testDataGenerator
import matplotlib.pyplot as mpl

maxSample = 2500
datapoints = 20

print('Genererer {} linjer tilfældigt ordnet data'.format(maxSample))
case = testDataGenerator.generateNearlySortedList(maxSample)

scaleResults = {}

try:
    scaleResults['BubbleSort'] = {}
    for sampleSize in range(1, maxSample, int(maxSample/datapoints)):
        print('Starter Bubble Sort med {} elementer'.format(sampleSize))
        tStart = time.time()
        algo.bubbleSort(case[:sampleSize])
        tSlut = time.time()
        scaleResults['BubbleSort'][sampleSize] = tSlut - tStart
        print(tSlut - tStart, 'sekunder')
except:
    print('Bubble Sort ikke implementeret eller har fejl. Springer over.')

try:
    scaleResults['insertionSort'] = {}
    for sampleSize in range(1, maxSample, int(maxSample/datapoints)):
        print('Starter insertionSort med {} elementer'.format(sampleSize))
        tStart = time.time()
        algo.insertionSort(case[:sampleSize])
        tSlut = time.time()
        scaleResults['insertionSort'][sampleSize] = tSlut - tStart
        print(tSlut - tStart, 'sekunder')
except:
    print('insertionSort ikke implementeret eller har fejl. Springer over.')

try:
    scaleResults['selectionSort'] = {}
    for sampleSize in range(1, maxSample, int(maxSample/datapoints)):
        print('Starter selectionSort med {} elementer'.format(sampleSize))
        tStart = time.time()
        algo.selectionSort(case[:sampleSize])
        tSlut = time.time()
        scaleResults['selectionSort'][sampleSize] = tSlut - tStart
        print(tSlut - tStart, 'sekunder')
except:
    print('selectionSort ikke implementeret eller har fejl. Springer over.')

try:
    scaleResults['Merge Sort'] = {}
    for sampleSize in range(1, maxSample, int(maxSample/datapoints)):
        print('Starter Merge Sort med {} elementer'.format(sampleSize))
        tStart = time.time()
        algo.mergeSort(case[:sampleSize])
        tSlut = time.time()
        scaleResults['Merge Sort'][sampleSize] = tSlut - tStart
        print(tSlut - tStart, 'sekunder')
except:
    print('Merge Sort ikke implementeret eller har fejl. Springer over.')

for key in scaleResults.keys():
    mpl.plot(list(scaleResults[key].keys()), list(scaleResults[key].values()))
mpl.xlabel('Elementer i listen')
mpl.ylabel('Tid')
mpl.legend(scaleResults.keys())
mpl.title('Skaleringstest - Tilfældigt ordnet liste')
mpl.grid(True)
mpl.savefig('scaleTest.png')
mpl.show()

print(scaleResults)
