"""
Name: Paul Briant
Date: 11/15/16
Class: Introduction to Python
Session06
LAB: Codingbat Lab

Description:

"""


# -------------------------------Imports----------------------------------------


# -------------------------------Functions--------------------------------------
def caught_speeding(speed, is_birthday):
    """

    """
    if is_birthday:
        if speed <= 65:
            return 0
        elif speed > 65 and speed <= 85:
            return 1
        else:
            return 2
    else:
        if speed <= 60:
            return 0
        elif speed > 60 and speed <= 80:
            return 1
        else:
            return 2


def big_diff(nums):
    """

    """
    count = len(nums)
    max_num, min_num = nums[0], nums[0]
    for i in range(1, count):
        max_num, min_num = max(max_num, nums[i]), min(min_num, nums[i])
    return max_num - min_num

# ==============================================================================


def main():
    """
    Calls functions and produces output.
    """

if __name__ == '__main__':
    main()
