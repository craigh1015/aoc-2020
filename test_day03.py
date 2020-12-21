import main


def test_part1():
    assert main.parseMapLine('..##.......') == [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    assert main.countTreeAt(0, [0, 1, 0]) == 0
    assert main.countTreeAt(1, [0, 1, 0]) == 1
    assert main.countTreeAt(3, [0, 1, 0]) == 0
    assert main.countTreeAt(7, [0, 1, 0]) == 1


def test_solve_part1():
    mapLines = main.readMap('day03_input')
    assert main.treesInSlope(3, 1, mapLines) == 250

def test_solve_part2():
    mapLines = main.readMap('day03_input')
    assert main.treesInSlope(1, 1, mapLines) == 55
    assert main.treesInSlope(3, 1, mapLines) == 250
    assert main.treesInSlope(5, 1, mapLines) == 54
    assert main.treesInSlope(7, 1, mapLines) == 55
    assert main.treesInSlope(1, 2, mapLines) == 39
    assert (55 * 250 * 54 * 55 * 39) == 1592662500
