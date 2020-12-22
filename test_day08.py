import main

# nop 0
# acc 1
# jmp 2


def test_part1():
    assert main.parseInstruction('nop +0') == [0, 0]
    assert main.parseInstruction('acc +99') == [1, 99]
    assert main.parseInstruction('jmp -2') == [2, -2]
    program = main.readProgram('day08_test')
    assert program[0] == [0, 0]
    assert program[5] == [1, -99]
    assert main.runInstruction({'pc': 0, 'acc': 0}, [[0, 0]]) == {"pc": 1, "acc": 0}
    assert main.runInstruction({'pc': 1, 'acc': 0}, [[0, 0], [1, 2]]) == {"pc": 2, "acc": 2}
    assert main.runInstruction({'pc': 2, 'acc': 2}, [[0, 0], [1, 2], [2, -2]]) == {"pc": 0, "acc": 2}
    assert main.runProgram([[0, 0], [1, 2], [2, -2]]) == ({'pc': 0, 'acc': 2}, True)
    assert main.runProgram(program) == ({'pc': 1, 'acc': 5}, True)


def test_solve_part1():
    program = main.readProgram('day08_input')
    assert main.runProgram(program) == ({'pc': 111, 'acc': 1521}, True)


def test_part2():
    program = main.readProgram('day08_test')
    assert main.runIterations(program) == {'pc': 9, 'acc': 8}


def test_solve_part2():
    program = main.readProgram('day08_input')
    assert main.runIterations(program) == {'pc': 638, 'acc': 1016}
