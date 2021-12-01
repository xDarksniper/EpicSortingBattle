import os, time, json, sys, math, matplotlib.pyplot as mpl, testDataGenerator as tg
from inspect import getmembers

def sortsCorrectly(case, algorithm):
    sortedCase = case.copy()
    sortedCase.sort()
    return sortedCase == algorithm(case)

def runFunctionTest(algoList):
    for algo in algoList:
        if sortsCorrectly(tg.generateNearlySortedList(10, 5), algo):
            print(algo.__name__, 'sorterer korrekt')
        else:
            print(algo.__name__, 'har fejl i sorteringen')
            algoList.remove(algo)
    return algoList

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

def runPerformaceTest(algoList):
    print('\nAfvikler performance tests')
    maxSample = 2500
    datapoints = 20
    runs = 1

    testcases = {'Random': tg.generateRandomList,
    'Reverse Sorted': tg.generateReverseSortedList,
    'Nearly Sorted': tg.generateNearlySortedList,
    'Few Unique': tg.generateFewUniqueList}

    testResults = {}
    for case in testcases.keys():
        testResults[case] = {}
        for algorithm in algoList:
            testResults[case][algorithm.__name__] = {}
            step = int(maxSample/datapoints)
            for sampleSize in range(step, maxSample+step, step):
                testResults[case][algorithm.__name__][sampleSize] = []
                for run in range(runs):
                    toSort = testcases[case](sampleSize)
                    tStart = time.time()
                    algorithm(toSort)
                    tSlut = time.time()
                    testResults[case][algorithm.__name__][sampleSize].append(tSlut - tStart)
                    print('{} \t {} elementer fra {} \t Run {} af {} \t {} sekunder'.format(algorithm.__name__.capitalize(), sampleSize, case, run+1, runs, round(tSlut - tStart, 5)))
                testResults[case][algorithm.__name__][sampleSize] = sum(testResults[case][algorithm.__name__][sampleSize])/runs
                print('Gennemsnit:', round(testResults[case][algorithm.__name__][sampleSize], 5), '\n')
    datestring = time.localtime(time.time())
    datestring = '{}-{}-{}_{}.{}.{}'.format(datestring[0], str(datestring[1]).zfill(2), str(datestring[2]).zfill(2), str(datestring[3]).zfill(2), str(datestring[4]).zfill(2), str(datestring[5]).zfill(2))
    fil = open('Performance Test Results {}.txt'.format(datestring), 'w')
    fil.write(json.dumps(testResults))
    fil.close()
    return testResults

def renderGraphs(data):
    font = {'size': 10, 'color': 'blue'}

    if not os.path.exists('./grafer'):
        print(os.getcwd())
        os.mkdir('./grafer')

    for case in data.keys():
        mpl.copper()
        for algorithm in data[case].keys():
            mpl.plot(list(data[case][algorithm].keys()), list(data[case][algorithm].values()))
        mpl.legend(data[case].keys())
        mpl.grid(True)
        mpl.title('Skaleringstest - {}'.format(case))
        mpl.tick_params(axis='x', labelrotation=45, labelsize=6)
        mpl.xlabel('Elementer i listen')
        mpl.ylabel('Tid')
        mpl.savefig('./grafer/{}.png'.format(case), dpi=300)
        mpl.clf()

def loadFromJson(filename):
    file = open(filename, 'r')
    data = json.loads(file.read())
    file.close()
    return data

if __name__ == '__main__':
    separator = '-----------------------------------------------------------------'
    try:
        import sorteringsAlgoritmer as algo
    except ModuleNotFoundError:
        print('Fejl: Algoritmerne skal implementeres i en fil ved navn: sorteringsAlgoritmer.py\nTesten er afbrudt.')
    else:
        foundAlgorithms = []
        print('Finder algoritmer...')
        for function in getmembers(algo):
            if 'Sort' in function[0]:
                foundAlgorithms.append(function[1])
                print(function[1].__name__, 'fundet')

        print(separator + '\nKontrollerer at fundne algoritmer sorterer korrekt')
        functionalAlgorithms = runFunctionTest(foundAlgorithms)
        print(separator)
        testdata = runPerformaceTest(functionalAlgorithms)
        renderGraphs(testdata)
