""" this module aims to run some unit test"""

import pandas
def inc(x):
    """adds 1 to the inputs parameter"""
    return x+1
def test_answer():
    """Run a unit test of the inc function"""
    assert inc(4)==5
