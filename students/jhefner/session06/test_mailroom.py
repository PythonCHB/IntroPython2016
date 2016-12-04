#!/Users/jhefner/python_dev/uw_python/bin/python

from mailroom_for_testing import check_if_donor
from mailroom_for_testing import create_a_report

def test_check_if_not_donor():
    assert not check_if_donor('Jack Hefner')
    assert not check_if_donor('012345')
    assert not check_if_donor(12345)

def test_check_if_donor():
    assert check_if_donor('Zapp Brannigan')

def test_create_a_report_completion():
    assert create_a_report({
        "Zapp Brannigan": [50, 73, 10],
        "Philip J Fry": [5],
        "Bender Bending Rodriguez": [500],
        "Turanga Leela": [7, 20, 96],
        "Hermes Conrad": [11, 14, 22],
        "Amy Wong": [8, 27, 34],
        })

