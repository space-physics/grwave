#!/usr/bin/env python
import pytest
import grwave
from pytest import approx


def test_grwave():
    wls = {'freqMHz': 0.89,
           'sigma': 2e-3,
           'epslon': 4,
           'dmax': 400,
           'hrr': 3,
           'htt': 100,
           'dstep': 10,
           'txwatt': 50e3, }

    data = grwave.grwave(wls)

    assert data.loc[100., 'fs'] == approx(119.996021)


if __name__ == '__main__':
    pytest.main(['-x', __file__])
