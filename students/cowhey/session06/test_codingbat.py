#!/usr/bin/env python

"""
test file for codingbat module

This version can be run with nose or py.test
"""

from codingbat import sleep_in, monkey_trouble, not_string, parrot_trouble


# tests for sleep_in
def test_false_false():
    assert sleep_in(False, False)


def test_true_false():
    assert not (sleep_in(True, False))


def test_false_true():
    assert sleep_in(False, True)


def test_true_true():
    assert sleep_in(True, True)


# put tests for monkey_trouble here
def test_monkey_true_true():
    assert monkey_trouble(True, True)


def test_monkey_false_false():
    assert monkey_trouble(False, False)


def test_monkey_false_true():
    assert monkey_trouble(False, True) is False


# tests for not_string
def test_not_string_candy():
    assert not_string("candy") == "not candy"


def test_not_string_x():
    assert not_string("x") == "not x"


def test_not_string_not_x():
    assert not_string("not x") == "not x"


def test_not_string_not_bad():
    assert not_string("not bad") == "not bad"


def test_not_string_bad():
    assert not_string("bad") == "not bad"


def test_not_string_not():
    assert not_string("not") == "not"


def test_not_string_is_not():
    assert not_string("is not") == "not is not"


def test_not_string_no():
    assert not_string("no") == "not no"


# tests for parrot_trouble
def test_parrot_early_talking():
    assert parrot_trouble(6, True)


def test_parrot_early_quiet():
    assert parrot_trouble(5, False) is False


def test_parrot_day_talking():
    assert parrot_trouble(10, True) is False


def test_parrot_day_quiet():
    assert parrot_trouble(12, False) is False


def test_parrot_night_talking():
    assert parrot_trouble(20, True)


def test_parrot_night_quiet():
    assert parrot_trouble(22, False) is False
