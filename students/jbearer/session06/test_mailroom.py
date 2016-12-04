#!/usr/bin/env python3
"""
Excercise: Write unit tests for mailroom.py
November 2, 2016
"""

from mailroom import sort_donors, proc_donation

def test_sort_donors():
    assert sort_donors() is None

def test_proc_donation_1():
    assert proc_donation('Fred', 35) is None