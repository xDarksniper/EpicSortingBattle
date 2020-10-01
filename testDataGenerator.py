import os, random, string, pprint

def makeFile(list, filename):
    if not os.path.exists('./testfiles'):
        os.mkdir('./testfiles')
    if not os.path.isfile('./testfiles/{}'.format(filename)):
        fil = open('./testfiles/{}'.format(filename), 'w')
        for e in list:
            fil.write(e)
            fil.write('\n')
        fil.close()

def generateRandomString(length):
    out = ''
    while len(out) < length:
        out += random.choice(string.ascii_letters)
    return out

def generateRandomList(length, chars=50):
    out = []
    while len(out) < length:
        out.append(generateRandomString(chars))
    return out

def generateNearlySortedList(length, chars=50):
    out = generateRandomList(length, chars)
    out.sort()
    offset = random.randint(1,10)
    for i in range(0, len(out)-offset, 5):
        out[i], out[i+offset] = out[i+offset], out[i]
    return out

def generateReverseSortedList(length, chars=50):
    out = generateRandomList(length, chars)
    out.sort()
    out.reverse()
    return out

def generateFewUniqueList(length, chars=50):
    temp = generateRandomList(length/10, chars)
    out = []
    for i in range(10):
        out.extend(temp)
    random.shuffle(out)
    return out

def generate():
    print('Genererer ca. 5 Mb testfiler')
    makeFile(generateRandomList(1000), 'testcase0.txt')
    print('I gang...')
    makeFile(generateFewUniqueList(25000), 'testcase1.txt')
    print('Stadig i gang...')
    makeFile(generateNearlySortedList(25000), 'testcase2.txt')
    print('Det var halvdelen')
    makeFile(generateReverseSortedList(25000), 'testcase3.txt')
    print('Næsten...')
    makeFile(generateRandomList(25000), 'testcase4.txt')
    print('Færdig! Check mappen "testfiles".')

if __name__ == '__main__':
    generate()
