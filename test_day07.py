import main


def test_part1():
    assert main.parseBaggageRule('light red bags contain 1 bright white bag, 2 muted yellow bags.') == {'light red': [[1, 'bright white'], [2, 'muted yellow']]}
    baggageRules = main.readBaggageRules('day07_test')
    assert baggageRules.get('light red') == [[1, 'bright white'], [2, 'muted yellow']]
    assert baggageRules.get('dark orange') == [[3, 'bright white'], [4, 'muted yellow']]
    assert baggageRules.get('bright white') == [[1, 'shiny gold']]
    assert baggageRules.get('muted yellow') == [[2, 'shiny gold'], [9, 'faded blue']]
    assert baggageRules.get('shiny gold') == [[1, 'dark olive'], [2, 'vibrant plum']]
    assert baggageRules.get('dark olive') == [[3, 'faded blue'], [4, 'dotted black']]
    assert baggageRules.get('vibrant plum') == [[5, 'faded blue'], [6, 'dotted black']]
    assert baggageRules.get('faded blue') == []
    assert baggageRules.get('dotted black') == []


def test_solve_part1():
    baggageRules = main.readBaggageRules('day07_input')
    assert len(main.getContainers('shiny gold', baggageRules)) == 161


def test_solve_part2():
    baggageRules = main.readBaggageRules('day07_input')
    assert main.countDeepContents('shiny gold', 1, baggageRules) == 30899 + 1
