import main

# byr 0 (Birth Year)
# iyr 1 (Issue Year)
# eyr 2 (Expiration Year)
# hgt 3 (Height)
# hcl 4 (Hair Color)
# ecl 5 (Eye Color)
# pid 6 (Passport ID)
# cid 7 (Country ID)

def test_part1():
    assert main.parsePassportLine('ecl:gry pid:860033327 eyr:2020 hcl:#fffffd') == [[5,'gry'], [6,'860033327'], [2,'2020'], [4,'#fffffd']]
    assert main.parsePassportLine('byr:1937 iyr:2017 cid:147 hgt:183cm') == [[0,'1937'], [1,'2017'], [7,'147'], [3,'183cm']]
    assert main.readPassports('day04_test', main.passportRulesPresent)[0] == [1, 1, 1, 1, 1, 1, 1, 1]
    assert main.readPassports('day04_test', main.passportRulesPresent)[1] == [1, 1, 1, 0, 1, 1, 1, 1]
    assert main.readPassports('day04_test', main.passportRulesPresent)[2] == [1, 1, 1, 1, 1, 1, 1, 0]
    assert main.readPassports('day04_test', main.passportRulesPresent)[3] == [0, 1, 1, 1, 1, 1, 1, 0]


def test_solve_part1():
    passports = main.readPassports('day04_input', main.passportRulesPresent)
    assert len(list(filter(lambda x: sum(x[:7]) == 7, passports))) == 250


def test_part2():
    assert main.passportRulesValid[0]('2002') == True
    assert main.passportRulesValid[0]('2003') == False

    assert main.passportRulesValid[3]('60in') == True
    assert main.passportRulesValid[3]('190cm') == True
    assert main.passportRulesValid[3]('190in') == False
    assert main.passportRulesValid[3]('190') == False

    assert main.passportRulesValid[4]('#123abc') == True
    assert main.passportRulesValid[4]('#123abz') == False
    assert main.passportRulesValid[4]('123abc') == False

    assert main.passportRulesValid[5]('brn') == True
    assert main.passportRulesValid[5]('wat') == False

    assert main.passportRulesValid[6]('000000001') == True
    assert main.passportRulesValid[6]('0123456789') == False

    assert main.readPassports('day04_test2', main.passportRulesValid)[0] == [1, 1, 0, 0, 1, 1, 0, 1]
    assert main.readPassports('day04_test2', main.passportRulesValid)[1] == [1, 1, 0, 1, 1, 1, 1, 0]
    assert main.readPassports('day04_test2', main.passportRulesValid)[2] == [1, 1, 1, 1, 0, 1, 1, 1]
    assert main.readPassports('day04_test2', main.passportRulesValid)[3] == [0, 0, 0, 0, 0, 0, 0, 0]

    assert main.readPassports('day04_test2', main.passportRulesValid)[4] == [1, 1, 1, 1, 1, 1, 1, 0]
    assert main.readPassports('day04_test2', main.passportRulesValid)[5] == [1, 1, 1, 1, 1, 1, 1, 1]
    assert main.readPassports('day04_test2', main.passportRulesValid)[6] == [1, 1, 1, 1, 1, 1, 1, 1]
    assert main.readPassports('day04_test2', main.passportRulesValid)[7] == [1, 1, 1, 1, 1, 1, 1, 0]


def test_solve_part2():
    passports = main.readPassports('day04_input', main.passportRulesValid)
    assert len(list(filter(lambda x: sum(x[:7]) == 7, passports))) == 158
