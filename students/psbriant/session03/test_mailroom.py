"""
Name: Paul Briant
Date: 11/15/16
Class: Introduction to Python
Session: 03
Assignment: Mailroom Tests

Description:
Tests for mailroom
"""

# -------------------------------Imports----------------------------------------
import mailroom

# -------------------------------Functions--------------------------------------


def test_list_donors():
    """
    Verifies content of the list_donors output.
    """
    donor_db = mailroom.donor_dict
    listing = mailroom.list_donors(donor_db)
    assert listing.startswith('Donors:\n')
    assert "Sheryl Sandberg" in listing
    assert "Satya Nadella" in listing
    assert len(listing.split('\n')) == 6


def test_find_donor():
    """
    Checks to see if a donor exists but with varied whitespace and cases.
    """
    assert mailroom.find_donor("satYa nADella ", mailroom.donor_dict)


def test_not_donor():
    """
    Test a non-existent donor.
    """
    donor_db = mailroom.donor_dict
    donor = mailroom.find_donor("Saya Nadella", donor_db)
    assert donor is None


def test_create_letter():
    """
    Test output of letter to ensure donor name and donation are present with
    correct formatting.

    Question:
    Need to fix assert error when verifying start of letter.
    """
    # Create test donor and donation amount
    name = "Paul Briant"
    amount = 200.00
    letter = mailroom.create_letter(name, amount)
    assert letter.startswith("Dear Paul Briant,\n")
    assert letter.endswith("-The Team\n")
    assert "donation of $200.00!\n" in letter


def test_print_report():
    """
    Test to ensure report is generated.
    """
    donor_db = mailroom.donor_dict
    report = mailroom.print_report(donor_db)
    print(report)


def test_sum_d():
    """
    Test to ensure donor statistics are generated.
    """
    donor_db = mailroom.donor_dict
    stats = mailroom.sum_d(donor_db)
    print(stats)
