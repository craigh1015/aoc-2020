import re


def getPairs(numbers):
    if len(numbers) < 2:
        return []
    if len(numbers) == 2:
        return [[numbers[0], numbers[1]]]

    head = numbers[0]
    rest = numbers[1:]

    pairs = list(map(lambda x: [head, x], rest))
    return pairs + getPairs(rest)


def getSums(numberLists):
    return list(map(lambda val: [val, sum(val)], numberLists))


def filterSums(sums, total):
    return list(filter(lambda val: val[1] == total, sums))


def readNumbers(fileName):
    return [int(line.rstrip('\n')) for line in open(fileName)]


def getTriples(numbers):
    if len(numbers) < 3:
        return []
    if len(numbers) == 3:
        return [[numbers[0], numbers[1], numbers[2]]]

    head = numbers[0]
    rest = numbers[1:]
    pairs = getPairs(rest)

    result = list(map(lambda x: [head, x[0], x[1]], pairs))
    return result + getTriples(rest)


def parsePolicyAndPassword(policyAndPassword):
    matches = re.search(
        r'(?P<pMin>\d+)\-(?P<pMax>\d+) (?P<pChar>\w): (?P<password>\w+)', policyAndPassword)
    pMin = int(matches.group('pMin'))
    pMax = int(matches.group('pMax'))
    pChar = matches.group('pChar')
    password = matches.group('password')
    return [pMin, pMax, pChar, password]


def countCharInString(char, string):
    return len(list(filter(lambda x: x == char, string)))


def isValidPolicyAndPassword(policyAndPassword):
    [pMin, pMax, pChar, password] = policyAndPassword
    charCount = countCharInString(pChar, password)
    return (pMin <= charCount) & (pMax >= charCount)


def readPolicyAndPasswords(fileName):
    return [parsePolicyAndPassword(line.rstrip('\n')) for line in open(fileName)]


def isValidPolicyAndPasswordOfficial(policyAndPassword):
    [pMin, pMax, pChar, password] = policyAndPassword
    first = 1 if password[pMin-1] == pChar else 0
    second = 1 if password[pMax-1] == pChar else 0
    return (first + second ) == 1


def parseMapLine(line):
    return [1 if x == '#' else 0 for x in line]


def countTreeAt(pos, mapLine):
    return mapLine[pos % len(mapLine)]


def readMap(fileName):
    return [parseMapLine(line.rstrip('\n')) for line in open(fileName)]


def treesInSlope(right, down, mapLines):
    treeCount = 0
    for (row, mapLine) in enumerate(mapLines):
        pos = int(row / down) * right
        val = countTreeAt(pos, mapLine) if (row % down) == 0 else 0
        treeCount += val
    return treeCount
