import json, pprint
import matplotlib.pyplot as mpl

def importData(filename):
    file = open(filename, 'r')
    data = json.loads(file.read())
    file.close()
    return data

testdata = importData('testresults.txt')
#pprint.pprint(testdata)

# Summer alle runs
cases = {}
for run in testdata:
    for case in testdata[run]:
        if not case in cases.keys():
            cases[case] = {}
        for algo in testdata[run][case]:
            if not algo in cases[case].keys():
                cases[case][algo] = 0
            cases[case][algo] += testdata[run][case][algo]
            #print(case, algo, cases[case][algo])

# Beregn snit af alle runs
for case in cases:
    for algo in cases[case]:
        cases[case][algo] = cases[case][algo]/len(testdata)

pprint.pprint(cases)

# Lav en bar pr. testcase
for case in cases:
    mpl.bar(range(len(cases[case])), list(cases[case].values()))
    mpl.ylabel('Sekunder')
    mpl.xlabel(case)
    mpl.xticks(range(len(cases[case])), list(cases[case].keys()))
    mpl.savefig(case + '.png')
    mpl.close()
