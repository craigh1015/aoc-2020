import functools
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


passportKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
def lookupPassportKey(key):
    return passportKeys.index(key)

def parsePassportKeyVal(keyVal):
    if keyVal == '':
        return [99, '']
    [key, value] = keyVal.split(':')
    return [lookupPassportKey(key), value]


def parsePassportLine(passportLine):
    pairs = passportLine.split(' ')
    return [parsePassportKeyVal(x) for x in pairs]


def readPassports(fileName, rules):
    passportLines = [parsePassportLine(line.rstrip('\n')) for line in open(fileName)]
    passports = [[0, 0, 0, 0, 0, 0, 0, 0]]
    for line in passportLines:
        if line == [[99, '']]:
            passports.append([0, 0, 0, 0, 0, 0, 0, 0])
            continue
        index = len(passports) - 1
        for [key, value] in line:
            passports[index][key] = 1 if rules[key](value) else 0
    return passports

passportRulesPresent = [
    lambda x: True,
    lambda x: True,
    lambda x: True,
    lambda x: True,
    lambda x: True,
    lambda x: True,
    lambda x: True,
    lambda x: True
]

passportRulesValid = [
    lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
    lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
    lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
    lambda x: (x[-2:] == 'cm' and 150 <= int(x[:-2]) <= 193) or (x[-2:] == 'in' and 59 <= int(x[:-2]) <= 76),
    lambda x: re.fullmatch(r'#[\da-f]{6}', x) != None,
    lambda x: re.fullmatch(r'(amb|blu|brn|gry|grn|hzl|oth)', x) != None,
    lambda x: re.fullmatch(r'\d{9}', x) != None,
    lambda x: True
]


def parseBoardingPass(boardingPass):
    value = boardingPass.replace('B', '1').replace('F','0').replace('R','1').replace('L','0')
    return [int(value[:7],2), int(value[7:],2), int(value, 2)]


def readBoardingPasses(fileName):
    return [parseBoardingPass(line.rstrip('\n')) for line in open(fileName)]


def findMissing(seats):
    sorted_seats = sorted(seats)
    a, b = 0, 0
    results = []
    for seat in sorted_seats:
        a, b = b, seat
        if b-a > 1:
            results.append([a, b])
    return results


def readCustomForms(fileName, operation):
    lines = [line.rstrip('\n') for line in open(fileName)]
    groups = [[]]
    for line in lines:
        if line == '':
            groups.append([])
            continue
        index = len(groups) - 1
        groups[index].append(set(line))
    return [functools.reduce(operation, group) for group in groups]
