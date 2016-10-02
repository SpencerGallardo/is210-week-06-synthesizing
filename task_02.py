#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 2 for Week 6"""


def prepare_email(appointments):
    """A list of two item tuples.
    Args:
        appointments(list): a list of tuples each containing a name and time.
    Rerturns:
        Each tuple populated into a sentence using .format()
    Examples:
        >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')])
        ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max,\nI look forward to meeting you on March 3.\nBest\nMe']
    """
    email = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    mytup = ()
    mylist = []
    for item in appointments:
        mytup = tuple(item)
        mylist.append(email.format(mytup[0], mytup[1]))
    return mylist
