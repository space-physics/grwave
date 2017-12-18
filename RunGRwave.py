#!/usr/bin/env python
"""Simple groundwave example, assuming uniform ground parameters"""
import subprocess
from pathlib import Path

wls = {'freqMHz': 0.89,
         'sigma':8e-3,
         'epslon':12,
         'dmax':500,
         'hrr':3,}

fin = Path('wls.asc')

fin.write_text(
       f'freq {wls["freqMHz"]}\n'
       f'sigma {wls["sigma"]}\n'
       f'epslon {wls["epslon"]}\n'
       f'dmax {wls["dmax"]}\n'
       f'hrr {wls["hrr"]}\n'
       'GO')

fout = fin.with_suffix('.out')

with fin.open('r') as i, fout.open('w') as o:
    subprocess.check_call('./grwave',stdin=i,stdout=o)