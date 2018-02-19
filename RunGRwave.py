#!/usr/bin/env python
"""Simple groundwave example, assuming uniform ground parameters"""
from matplotlib.pyplot import figure,show
import seaborn as sns
sns.set_context('talk',1.)
#
from pygrwave import run_grwave

wls = {'freqMHz': 0.89,
         'sigma':2e-3,
         'epslon':4,
         'dmax':400,
         'hrr':3,
         'htt':100,
         'dstep':10,
         'txwatt':50e3,}


data = run_grwave(wls)
# %%
d_km = data.index.values.astype(float)

ax = figure().gca()
ax.plot(d_km, data['fs'].values)
ax.set_xlabel('distance [km]')
ax.set_ylabel('field strength mV/m')
ax.axhline(4,color='red',linestyle='--')
ax.grid(True)
#ax.set_ylim((0,25))
show()