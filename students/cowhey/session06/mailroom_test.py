#!/usr/bin/env python

import mailroom_rewrite as mr
import os

def test_donation_report():
    """test that the donation report comes out right"""
    assert ['Luuk Sinclair', '180.00', '1', '180.00'] in mr.create_reports()


def test_initial_db():
    """test that the initial database loads correctly"""
    db = mr.donors
    assert "Mahesha Diogenes" in db
    assert "Luuk Sinclair" in db
    assert db["Neoptolemus Yaropolk"] == [36.00]


def test_report_printing():
    row = ['Neoptolemus Yaropolk', '36.00', '1', '36.00']
    assert mr.format_row(row) == "Neoptolemus Yaropolk           36.00                          1                              36.00"


def test_report_writing():
    """test that report is written to disk"""
    mr.print_thank_you("Neoptolemus Yaropolk")
    assert os.path.isfile("Neoptolemus_Yaropolk.txt")
    with open("Neoptolemus_Yaropolk.txt") as f:
        file_size = len(f.read())
    assert file_size > 0


def test_total_donation_amount():
    """test that correct donation amount is returned"""
    row = ['Arthur Tjaz', '18.00', '1', '18.00']
    assert mr.total_donation_amount(row) == 18.00
