"""
Name: Paul Briant
Date: 11/15/16
Class: Introduction to Python
Session06
LAB: Codingbat Lab

Description:

"""

# -------------------------------Imports----------------------------------------
from codingbat_lab import caught_speeding, big_diff

# -------------------------------Functions--------------------------------------


# Tests for caught_speeding
def test_60_false():
    assert caught_speeding(60, False) == 0


def test_65_false():
    assert caught_speeding(65, False) == 1


def test_65_true():
    assert caught_speeding(65, True) == 0


def test_80_false():
    assert caught_speeding(80, False) == 1


def test_85_false():
    assert caught_speeding(85, False) == 2


def test_85_true():
    assert caught_speeding(85, True) == 1


def test_70_false():
    assert caught_speeding(70, False) == 1


def test_75_false():
    assert caught_speeding(75, False) == 1


def test_75_true():
    assert caught_speeding(75, True) == 1


def test_40_false():
    assert caught_speeding(40, False) == 0


def test_40_true():
    assert caught_speeding(40, True) == 0


def test_90_false():
    assert caught_speeding(90, False) == 2


# Tests for big_diff

def test_10_3_5_6_diff8():
    assert big_diff([10, 3, 5, 6]) == 7


def test_7_2_10_9_diff8():
    assert big_diff([7, 2, 10, 9]) == 8


def test_2_10_7_2_diff8():
    assert big_diff([2, 10, 7, 2]) == 8


def test_2_10_diff8():
    assert big_diff([2, 10]) == 8


def test_10_2_diff8():
    assert big_diff([10, 2]) == 8


def test_10_0_diff10():
    assert big_diff([10, 0]) == 10


def test_2_3_diff1():
    assert big_diff([2, 3]) == 1


def test_2_2_diff0():
    assert big_diff([2, 2]) == 0


def test_2_diff0():
    assert big_diff([2]) == 0


def test_5_1_6_1_9_9_diff8():
    assert big_diff([5, 1, 6, 1, 9, 9]) == 8


def test_7_6_8_5_diff3():
    assert big_diff([7, 6, 8, 5]) == 3


def test_7_7_6_8_5_5_6_diff3():
    assert big_diff([7, 7, 6, 8, 5, 5, 6]) == 3


# ==============================================================================


def main():
    """
    Calls functions and produces output.
    """

if __name__ == '__main__':
    main()
