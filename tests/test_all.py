#!/usr/bin/env python
import unittest
from pygrwave import run_grwave
import numpy.testing

class BasicTests(unittest.TestCase):

    def test_grwave(self):
        wls = {'freqMHz': 0.89,
         'sigma':2e-3,
         'epslon':4,
         'dmax':400,
         'hrr':3,
         'htt':100,
         'dstep':10,
         'txwatt':50e3,}

        data = run_grwave(wls)

        numpy.testing.assert_allclose(data.loc[100.,'fs'],119.996021)


if __name__ == '__main__':
    unittest.main()
