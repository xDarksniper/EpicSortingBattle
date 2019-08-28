import time, json, testDataGenerator, sorteringsAlgoritmer as algo

def importFile(filename):
    outList = []
    fil = open(filename)
    for line in fil:
        outList.append(line.strip())
    return outList

def runTestCase(filename):
    caseResults = {}
    print('\nImporterer', filename)
    case = importFile('./testfiles/' + filename)

    print('Starter Select Sort')
    tStart = time.time()
    algo.selectSort(case)
    tSlut = time.time()
    caseResults['Select Sort'] = tSlut - tStart
    print('Select Sort:', tSlut - tStart)

    print('Starter Insert Sort')
    tStart = time.time()
    algo.insertSort(case)
    tSlut = time.time()
    caseResults['Insert Sort'] = tSlut - tStart
    print('Insert Sort:', tSlut - tStart)

    print('Starter Bubble Sort')
    tStart = time.time()
    algo.bubbleSort(case)
    tSlut = time.time()
    caseResults['Bubble Sort'] = tSlut - tStart
    print('Bubble Sort:', tSlut - tStart)

    print('Starter Timsort')
    tStart = time.time()
    case.sort()
    tSlut = time.time()
    caseResults['Timsort'] = tSlut - tStart
    print('Timsort:', tSlut - tStart)

    return caseResults

testResults = {}
for run in range(1):
    runResults = {}
    runResults['Testcase 0'] = runTestCase('testcase0.txt')
    runResults['Testcase 1'] = runTestCase('testcase1.txt')
    runResults['Testcase 2'] = runTestCase('testcase2.txt')
    runResults['Testcase 3'] = runTestCase('testcase3.txt')
    runResults['Testcase 4'] = runTestCase('testcase4.txt')
    testResults[run] = runResults

fil = open('testresults.txt', 'w')
fil.write(json.dumps(testResults))
fil.close()
