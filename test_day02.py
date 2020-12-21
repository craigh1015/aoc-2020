import main


def test_part1():
    assert main.parsePolicyAndPassword('1-3 a: abcde') == [1, 3, 'a', 'abcde']
    assert main.isValidPolicyAndPassword([1, 3, 'a', 'abcde']) == True
    assert main.isValidPolicyAndPassword([1, 3, 'b', 'cdefg']) == False
    assert main.isValidPolicyAndPassword([2, 9, 'c', 'ccccccccc']) == True


def test_solve_part1():
    policyAndPasswords = main.readPolicyAndPasswords('day02_input')
    assert len(list(filter(main.isValidPolicyAndPassword, policyAndPasswords))) == 582


def test_part2():
    assert main.isValidPolicyAndPasswordOfficial([1, 3, 'a', 'abcde']) == True
    assert main.isValidPolicyAndPasswordOfficial([1, 3, 'b', 'cdefg']) == False
    assert main.isValidPolicyAndPasswordOfficial([2, 9, 'c', 'ccccccccc']) == False


def test_solve_part1():
    policyAndPasswords = main.readPolicyAndPasswords('day02_input')
    assert len(list(filter(main.isValidPolicyAndPasswordOfficial, policyAndPasswords))) == 729
