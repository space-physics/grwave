from pathlib import Path
import subprocess
import io
import pandas as pd
import numpy as np

root = Path(__file__).parents[1]
TXW0 = 1e3  # ITU assumes 1kW power
CORR = 0.5

def run_grwave(wls):

    strin = (
       f'freq {wls["freqMHz"]}\n'
       f'sigma {wls["sigma"]}\n'
       f'epslon {wls["epslon"]}\n'
       f'dmax {wls["dmax"]}\n'
       f'hrr {wls["hrr"]}\n'
       f'htt {wls["htt"]}\n'
       f'dstep {wls["dstep"]}\n'
       'GO')


    out = subprocess.check_output('./grwave', input=strin, universal_newlines=True, cwd=root)
    # %%
    data = pd.read_csv(io.StringIO(out), sep='\s+',index_col=0,
                       skiprows=31, names=['fs','pathloss'])

    data.dropna(how='all',axis=0,inplace=True)
    data = data[~data.index.duplicated(keep='last')]
    data.index = data.index.astype(float)

    data['fs'] *= np.sqrt(wls['txwatt']/TXW0) * CORR

    return data