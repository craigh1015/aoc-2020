import main

def test_part1():
    forms = main.readCustomForms('day06_test', lambda x, y: x.union(y))
    assert forms[0] == {'c', 'b', 'a'}
    assert forms[1] == {'c', 'b', 'a'}
    assert forms[2] == {'c', 'b', 'a'}
    assert forms[3] == {'a'}
    assert forms[4] == {'b'}


def test_solve_part1():
    forms = main.readCustomForms('day06_input', lambda x, y: x.union(y))
    assert sum(map(lambda x: len(x), forms)) == 6809


def test_part2():
    forms = main.readCustomForms('day06_test', lambda x, y: x.intersection(y))
    assert forms[0] == {'c', 'b', 'a'}
    assert forms[1] == set([])
    assert forms[2] == {'a'}
    assert forms[3] == {'a'}
    assert forms[4] == {'b'}

def test_solve_part2():
    forms = main.readCustomForms('day06_input', lambda x, y: x.intersection(y))
    assert sum(map(lambda x: len(x), forms)) == 3394
