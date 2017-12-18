#!/usr/bin/env python
"""Simple groundwave example, assuming uniform ground parameters"""
import subprocess
from pathlib import Path
import pandas as pd
import numpy as np
from matplotlib.pyplot import figure,show
import seaborn as sns
sns.set_context('talk',1.2)

TXW0 = 1e3  # ITU assumes 1kW power
CORR = 0.5

wls = {'freqMHz': 0.89,
         'sigma':2e-3,
         'epslon':4,
         'dmax':400,
         'hrr':3,
         'htt':100,
         'dstep':10,
         'txwatt':50e3,}

fin = Path('wls.asc')

fin.write_text(
       f'freq {wls["freqMHz"]}\n'
       f'sigma {wls["sigma"]}\n'
       f'epslon {wls["epslon"]}\n'
       f'dmax {wls["dmax"]}\n'
       f'hrr {wls["hrr"]}\n'
       f'htt {wls["htt"]}\n'
       f'dstep {wls["dstep"]}\n'
       'GO')

fout = fin.with_suffix('.out')

with fin.open('r') as i, fout.open('w') as o:
    subprocess.check_call('./grwave',stdin=i,stdout=o)
# %%
data = pd.read_csv(fout, sep='\s+',index_col=0,
                   skiprows=31, names=['fs','pathloss'])

data.dropna(how='all',axis=0,inplace=True)
data = data[~data.index.duplicated(keep='last')]

data['fs'] *= np.sqrt(wls['txwatt']/TXW0) * 0.5
# %%
ax = figure().gca()
data['fs'].plot(ax=ax)
ax.set_xlabel('distance [km]')
ax.set_ylabel('field strength mV/m')
ax.axhline(4,color='red',linestyle='--')
ax.grid(True)
#ax.set_ylim((0,25))
show()