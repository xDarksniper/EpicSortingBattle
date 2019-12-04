import time, json, sys, matplotlib.pyplot as mpl, testDataGenerator, pprint
from inspect import getmembers

try:
    import sorteringsAlgoritmer as algo
except ModuleNotFoundError:
    print('Fejl: Algoritmerne skal implementeres i en fil ved navn: sorteringsAlgoritmer.py\nTesten er afbrudt.')
else:
    algoList = []
    for function in getmembers(algo):
        if 'sort' in function[0].lower():
            algoList.append(function[1])

def importFile(filename):
    outList = []
    fil = open(filename)
    for line in fil:
        outList.append(line.strip())
    return outList

def runTestCase(case, algorithm):
    caseResults = {}

    try:
        print('Starter', algorithm.__name__)
        tStart = time.time()
        algorithm(case)
        tSlut = time.time()
        caseResults[algorithm.__name__] = tSlut - tStart
        print(algorithm.__name__, tSlut - tStart, 'sekunder')
    except Exception as x:
        print('Fejl i funktionen.')
        print(x)

def reallyDoesSort(case, algorithm):
    sortedCase = case.copy()
    sortedCase.sort()
    if sortedCase == algorithm(case):
        return True
    else:
        return False

def runFunctionTest():
    for algo in algoList:
        print('Checker', algo.__name__)
        if reallyDoesSort(testDataGenerator.generateNearlySortedList(5), algo):
            print(algo.__name__, 'sorterer korrekt')
        else:
            print(algo.__name__, 'Har fejl i sorteringen')

def runPerformaceTest():
    try:
        importFile('./testfiles/random.txt')
    except FileNotFoundError:
        print('Kunne ikke finde testfiler. Prøver at generere.')
        testDataGenerator.generate(2500)
    else:
        print('\nAfvikler tests')

        #for algorithm in algoList:

        #runTestCase(case, algo.mergeSort)




if __name__ == '__main__':
    runFunctionTest()
    #runPerformaceTest()
