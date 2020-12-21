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
