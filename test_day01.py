import main


def test_part1():
    assert main.getPairs([1, 2]) == [[1, 2]]
    assert main.getPairs([1, 2, 3]) == [[1, 2], [1, 3], [2, 3]]

    assert main.getSums([[1, 2]]) == [[[1, 2], 3]]

    assert main.filterSums([[[1, 2], 3]], 1) == []
    assert main.filterSums([[[1, 2], 3]], 3) == [[[1, 2], 3]]

    assert main.readNumbers('day01_test') == [1721, 979, 366, 299, 675, 1456]


def test_solve_part1():
    numbers = main.readNumbers('day01_input')
    pairs = main.getPairs(numbers)
    sums = main.getSums(pairs)
    filteredSums = main.filterSums(sums, 2020)
    val0 = filteredSums[0][0][0]
    val1 = filteredSums[0][0][1]
    assert (val0 * val1) == 299299


def test_part2():
    assert main.getTriples([1, 2]) == []
    assert main.getTriples([1, 2, 3]) == [[1, 2, 3]]
    assert main.getTriples([1, 2, 3, 4]) == [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]


def test_solve_part2():
    numbers = main.readNumbers('day01_input')
    triples = main.getTriples(numbers)
    sums = main.getSums(triples)
    filteredSums = main.filterSums(sums, 2020)
    val0 = filteredSums[0][0][0]
    val1 = filteredSums[0][0][1]
    val2 = filteredSums[0][0][2]
    assert (val0 * val1 * val2) == 287730716
