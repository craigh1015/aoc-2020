import copy
import functools
import re


##########
### DAY 01


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


##########
### DAY 02


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
    return (first + second) == 1


##########
### DAY 03


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


##########
### DAY 04


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
    passportLines = [parsePassportLine(line.rstrip('\n'))
                     for line in open(fileName)]
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
    lambda x: (x[-2:] == 'cm' and 150 <= int(x[:-2]) <=
               193) or (x[-2:] == 'in' and 59 <= int(x[:-2]) <= 76),
    lambda x: re.fullmatch(r'#[\da-f]{6}', x) != None,
    lambda x: re.fullmatch(r'(amb|blu|brn|gry|grn|hzl|oth)', x) != None,
    lambda x: re.fullmatch(r'\d{9}', x) != None,
    lambda x: True
]


##########
### DAY 05


def parseBoardingPass(boardingPass):
    value = boardingPass.replace('B', '1').replace(
        'F', '0').replace('R', '1').replace('L', '0')
    return [int(value[:7], 2), int(value[7:], 2), int(value, 2)]


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


##########
### DAY 06


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


##########
### DAY 07


def parseBaggageRule(rule):
    parts = rule.split(' bags contain ')
    if parts[1] == "no other bags.":
        return dict({parts[0]: []})
    contents = list(map(lambda x: [int(x.split(' ')[0]), x.split(' ')[1] + ' ' + x.split(' ')[2]], parts[1].split(', ')))
    return dict({parts[0]: contents})


def readBaggageRules(fileName):
    lines = [parseBaggageRule(line.rstrip('\n')) for line in open(fileName)]
    rules = {}
    for rule in lines:
        rules.update(rule)
    return rules


def canContain(holder, content, baggageRules):
    rules = baggageRules[holder]
    if rules == []:
        return False
    for rule in rules:
        if content == rule[1]:
            return True
        if canContain(rule[1], content, baggageRules):
            return True
    return False


def getContainers(bag, baggageRules):
    results = []
    for holder in baggageRules.keys():
        if canContain(holder, bag, baggageRules):
            results.append(holder)
    return results


def countDeepContents(bag, count, baggageRules):
    rules = baggageRules[bag]
    total = count
    if rules != []:
        for rule in rules:
            total += count * countDeepContents(rule[1], rule[0], baggageRules)
    return total


##########
### DAY 08


opCodes = ['nop', 'acc', 'jmp']


def parseInstruction(instruction):
    parts = instruction.split(' ')
    return [opCodes.index(parts[0]), int(parts[1])]


def readProgram(fileName):
    return [parseInstruction(line.rstrip('\n')) for line in open(fileName)]


instructions = [
    lambda state, value: {'pc': state['pc'] + 1, 'acc': state['acc']},
    lambda state, value: {'pc': state['pc'] + 1, 'acc': state['acc'] + value},
    lambda state, value: {'pc': state['pc'] + value, 'acc': state['acc']},
]

def runInstruction(state, program):
    instruction = program[state['pc']]
    return instructions[instruction[0]](state, instruction[1])

def runProgram(program):
    history = [False] * len(program)
    state = {'pc': 0, 'acc': 0}
    infiniteLoop = False
    while not infiniteLoop:
        history[state['pc']] = True
        state = runInstruction(state, program)
        if state['pc'] == len(program):
            break
        infiniteLoop = history[state['pc']]
    return state, infiniteLoop

def runIterations(program):
    for line in range(len(program)):
        if program[line][0] == 1:
            continue
        program_copy = copy.deepcopy(program)
        program_copy[line][0] = 2 if program[line][0] == 0 else 0
        (state, failed) = runProgram(program_copy)
        if failed == False:
            return state


##########
### DAY 09


def findInvalid(numbers, size):
    for pos in range(size, len(numbers)):
        sums = map(lambda x: x[1], getSums(getPairs(numbers[pos-size:pos])))
        if numbers[pos] not in sums:
            return numbers[pos]


def findWeakness(numbers, invalid):
    for start in range(len(numbers)):
        for end in range(start, len(numbers)):
            total = sum(numbers[start:end])
            if total == invalid:
                return numbers[start:end]
            if total > invalid:
                break
