import solution


def test_parse_no_input():
    assert solution.parse_tokens("") == []


def test_parse_2_add_3_times_5():
    assert solution.parse_tokens("2 + 3 * 5") == [2, "+", 3, "*", 5]


# def test_evaluate_parentheses():


def test_2_add_3_times_5_gives_25():
    assert solution.evaluate("2 + 3 * 5") == 25


def test_example_0():
    assert solution.evaluate("1 + 2 * 3 + 4 * 5 + 6") == 71


def test_example_1():
    assert solution.evaluate("2 * 3 + (4 * 5)") == 26


def test_example_2():
    assert solution.evaluate("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437


def test_example_3():
    assert solution.evaluate("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240


def test_example_4():
    assert solution.evaluate("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632