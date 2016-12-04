#!/usr/bin/env/python3
"""
LAB: pytest
November 1, 2016
"""

from myfunctions import monkey_trouble, squirrel_play

def test_monkey_true_true1():
    assert monkey_trouble(True, True)

def test_monkey_false_false2():
    assert monkey_trouble(False, False)

def test_monkey_true_false3():
    assert not monkey_trouble(True, False)

def test_squirrel_play1():
    assert squirrel_play(70, False) is True

def test_squirrel_play2():
    assert squirrel_play(95, False) is False

def test_squirrel_play3():
    assert squirrel_play(95, True) is True

def test_squirrel_play4():
    assert squirrel_play(90, False) is True

def test_squirrel_play5():
    assert squirrel_play(90, True) is True

def test_squirrel_play6():
    assert squirrel_play(50, False) is False

def test_squirrel_play7():
    assert squirrel_play(50, True) is False

def test_squirrel_play8():
    assert squirrel_play(100, False) is False

def test_squirrel_play9():
    assert squirrel_play(100, True) is True

def test_squirrel_play10():
    assert squirrel_play(105, True) is False

def test_squirrel_play11():
    assert squirrel_play(59, False) is False

def test_squirrel_play12():
    assert squirrel_play(59, True) is False

def test_squirrel_play13():
    assert squirrel_play(60, False) is True