
"""
When squirrels get together for a party, they like to have cigars.
A squirrel party is successful when the number of cigars is between
40 and 60, inclusive. Unless it is the weekend, in which case there
is no upper bound on the number of cigars.

Return True if the party with the given values is successful,
or False otherwise.
"""
<<<<<<< HEAD
def cigar_party(cigars, weekend):
    return cigars >= 40 and (cigars <= 60 or weekend)
=======


def cigar_party(num, weekend):
    return num >= 40  and (num <= 60 or weekend)

>>>>>>> 82918d5472627037e6cfaa6846d007c78ac8ef6c
