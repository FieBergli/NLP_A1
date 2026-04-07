#!/usr/bin/env python3

"""
NLP A0: The Basics

Usage: on the Unix command line,
  python basics.py
to run doctests. If all tests pass, the program will exit silently.

@author: Nathan Schneider, Lucia Donatelli

DO NOT SHARE/DISTRIBUTE SOLUTIONS WITHOUT THE INSTRUCTOR'S PERMISSION
"""


import re, doctest


def validate1(s):
    """
    Checks whether the string is a valid employee ID using a single regular expression.
    An employee ID is valid if and only if it consists
    only of 6-10 alphabetic characters (letters), followed by 2 numeric digits.

    (Assumes s is a string without any non-ASCII characters.
    Otherwise, does not make any assumptions about the string.)

    The lines below give example inputs and correct outputs using doctest notation,
    and can be run to test the code. Passing these tests is NOT sufficient
    to guarantee your implementation is correct. You may add additional test cases.

    >>> validate1('AbCdEf00')
    True
    >>> validate1('$0RQLpCHz49')
    False
    """
    s = s.lower()
    EMPLOYEE_RE = r"^[a-z]{6,10}[0-9]{2}$"
    if re.search(EMPLOYEE_RE, s):
        return True
    return False


def validate2(s):
    """
    >>> validate2('AbCdEf00')
    True
    >>> validate2('$0RQLpCHz49')
    False
    """

    letters = s[:-2]
    digits = s[-2:]
    if len(s) <= 12 and len(s) >= 8:
        if letters.isalpha() and digits.isdigit():
            return True
    return False


def dna_prob(seq):
    """
    Given a sequence of the DNA bases {A, C, G, T},
    stored as a string, returns a conditional probability table
    in a data structure such that one base (b1) can be looked up,
    and then a second (b2), to get the probability p(b2 | b1)
    of the second base occurring immediately after the first.
    (Assumes the length of seq is >= 3, and that the probability of
    any b1 and b2 which have never been seen together is 0.
    Ignores the probability that b1 will be followed by the
    end of the string.)

    >>> tbl = dna_prob('ATCGATTGAGCTCTAGCG')
    >>> tbl['T']['T']
    0.2
    >>> tbl['G']['A']
    0.5
    >>> tbl['C']['G']
    0.5
    """
    dna_dict = {}

    for base in "ACGT":
        dna_dict[base] = {"A": 0, "C": 0, "G": 0, "T": 0, "num_pairs": 0}

    for i in range(len(seq) - 1):
        b1 = seq[i]
        b2 = seq[i + 1]

        dna_dict[b1][b2] += 1
        dna_dict[b1]["num_pairs"] += 1

    for base in dna_dict:
        num_pairs = dna_dict[base]["num_pairs"]
        for next_base in "ACGT":
            if num_pairs > 0:
                dna_dict[base][next_base] = dna_dict[base][next_base] / num_pairs
            else:
                dna_dict[base][next_base] = 0

    return dna_dict


def dna_bp(seq):
    """
    Given a string representing a sequence of DNA bases,
    returns the paired sequence, also as a string,
    where A is always paired with T and C with G.

    >>> dna_bp('ATCGATTGAGCTCTAGCG')
    'TAGCTAACTCGAGATCGC'
    """

    return (seq.replace("A", "x").replace("T", "A").replace("x", "T").replace("C", "y").replace("G", "C").replace("y", "G"))


if __name__ == "__main__":
    doctest.testmod()  # This runs the doctests and prints any failures.


# ------------ Claud Generated solutions: --------------------------


def validate1(s):
    """
    >>> validate1('AbCdEf00')
    True
    >>> validate1('$0RQLpCHz49')
    False
    """

    EMPLOYEE_RE = r"^[A-Za-z]{6,10}\d{2}$"
    if re.search(EMPLOYEE_RE, s):
        return True
    return False


# Exactly similar to my solution, except I made all characters lower case for an easier regex pattern matching. I do not think this step decreases
# readability as the regex [a-z] is easier to understand than [A-Za-z]. I think the efficiency is very similar. Both are correct.


def validate2(s):
    """
    >>> validate2('AbCdEf00')
    True
    >>> validate2('$0RQLpCHz49')
    False
    """
    if len(s) < 8 or len(s) > 12:
        return False

    if not s[-2:].isdigit():
        return False

    alpha_part = s[:-2]
    if len(alpha_part) < 6 or len(alpha_part) > 10:
        return False

    if not alpha_part.isalpha():
        return False

    return True


# My version is more concise, but the claude version could be considered more readable because it checks each condition separately with early returns. 
# So it's an easier step-by-step solution. However, I think claude's code is a bit over-bloated, and with good variable names, my solution is very readable. 
# Efficiency is similar. Both should be correct on valid and invalid ID lengths and variants.


def dna_prob(seq):
    """
     >>> tbl = dna_prob('ATCGATTGAGCTCTAGCG')
    >>> tbl['T']['T']
    0.2
    >>> tbl['G']['A']
    0.5
    >>> tbl['C']['G']
    0.5
    """

    counts = {}
    for i in range(len(seq) - 1):
        b1, b2 = seq[i], seq[i + 1]
        if b1 not in counts:
            counts[b1] = {}
        counts[b1][b2] = counts[b1].get(b2, 0) + 1

    table = {}
    for b1, successors in counts.items():
        total = sum(successors.values())
        table[b1] = {b2: count / total for b2, count in successors.items()}

    return table

# My solution is more correct on hidden cases because unseen base pairs still map to 0. Claude's version would fail on some cases because missing pairs are not included.
# My solution is less concise and could be considered more readable since every base pair is stored explicitly. Claude's version is shorter and slightly more efficient in space. 

def dna_bp(seq):
    """
    Given a string representing a sequence of DNA bases,
    returns the paired sequence, also as a string,
    where A is always paired with T and C with G.
    >>> dna_bp('ATCGATTGAGCTCTAGCG')
    'TAGCTAACTCGAGATCGC'
    """
    return seq.translate(str.maketrans("ATCG", "TAGC"))


# I think Claude's solution is cleaner and faster, using maketrans().  My version is correct, but awkward, and less efficient because it replaces characters several times.