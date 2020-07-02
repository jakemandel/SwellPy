# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 10:37:39 2020

@author: jakem
"""


from swellpy import Monodisperse 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# initialize the parameters in the class of methods (N,B,seed)
# The code in the monodisperse module lays out how each method works
N = 1000 #number of particles
B = 40 #box side length
seed = 125 #inital particle placement randomization
m = Monodisperse(N,B,seed)

#Define: important variables that you need. Natasha goes over these in her paper.
area_frac = 0.7 # area fraction
swell = m.equiv_swell(area_frac)
kick = .035
swell = m.equiv_swell(area_frac)
cycle_number = 5 #This is the number of shears that you do to your system.

pairs = m._tag(swell)
theta = m.find_angle2(pairs)
# rounded_theta = [ '%.1f' % elem for elem in theta ]
#print(rounded_theta)

x = pd.Series(theta, name="Theta")
sns.set_style('darkgrid')
ax = sns.distplot(x, kde=True, norm_hist=True,) #








# n, bins, patches = plt.hist(rounded_theta, bins='auto', color='#0504aa',
#                             alpha=0.7, rwidth=0.85)
# plt.grid(axis='y', alpha=0.75)
# plt.xlabel('Theta')
# plt.ylabel('Count')
# maxfreq = n.max()
# # Set a clean upper y-axis limit.
# # plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
# plt.show()


