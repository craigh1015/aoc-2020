import main

def test_part1():
    assert main.parseBoardingPass('BFFFBBFRRR') == [70, 7, 567]
    assert main.parseBoardingPass('FFFBBBFRRR') == [14, 7, 119]
    assert main.parseBoardingPass('BBFFBBFRLL') == [102, 4, 820]


def test_solve_part1():
    boardingPasses = main.readBoardingPasses('day05_input')
    assert max(list(map(lambda x: x[2], boardingPasses))) == 915


def test_part2():
    assert main.findMissing([1,2,4,5]) == [[2, 4]]


def test_solve_part2():
    boardingPasses = main.readBoardingPasses('day05_input')
    assert main.findMissing(list(map(lambda x: x[2], boardingPasses))) == [[0, 46], [698, 700]]
