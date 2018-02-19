#!/usr/bin/env python
install_requires=['numpy','folium','pandas','matplotlib','seaborn']
tests_require=['nose','coveralls']
# %%
import subprocess
from setuptools import setup,find_packages

setup(name='pygrwave',
      packages=find_packages(),
      description='Groundwave per ITU P.368 10 kHz - 30 MHz',
      version='0.1.0',
      url='https://github.com/scivision/python-grwave',
      classifiers=[
      'Intended Audience :: Science/Research',
      'Development Status :: 3 - Alpha',
      'Programming Language :: Python :: 3',],
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'tests':tests_require,
                      'plot':['matplotlib','seaborn',],},
      python_requires='>=3.6',
   )
   
subprocess.check_call(['gfortran','fortran/grwave.for','-o','grwave'])
