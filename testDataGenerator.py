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

def generate(sampleSize):
    print('Genererer testfiler')
    makeFile(generateFewUniqueList(sampleSize), 'few_unique.txt')
    makeFile(generateNearlySortedList(sampleSize), 'nearly_sorted.txt')
    makeFile(generateReverseSortedList(sampleSize), 'reverse.txt')
    makeFile(generateRandomList(sampleSize), 'random.txt')
    print('Færdig! Check mappen "testfiles".')

if __name__ == '__main__':
    generate()
