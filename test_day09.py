import main


def test_part1():
    numbers = main.readNumbers('day09_test')
    assert numbers[:5] == [35, 20, 15, 25, 47]


def test_solve_part1():
    numbers = main.readNumbers('day09_input')
    assert main.findInvalid(numbers, 25) == 542529149


def test_part1():
    numbers = main.readNumbers('day09_test')
    assert numbers[:5] == [35, 20, 15, 25, 47]
    assert main.findWeakness(numbers, 127) == [15, 25, 47, 40]

def test_solve_part2():
    numbers = main.readNumbers('day09_input')
    weakness = main.findWeakness(numbers, 542529149)
    weakness.sort()
    assert weakness[0] == 23189120
    assert weakness[-1] == 52489498
    assert weakness[0] + weakness[-1] == 75678618
