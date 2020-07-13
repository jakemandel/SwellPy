# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 12:25:02 2020

@author: jakem
"""


from monodisperse_box_xform import Monodisperse2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

'''
Write Memory on x-axis
'''

# initialize the parameters in the class of methods (N,B,seed)
# The code in the monodisperse module lays out how each method works
N = 1000 #number of particles
Bx = 40 #box side length
By = 40
seed = 115 #inital particle placement randomization
m = Monodisperse2(N,Bx,By,seed)

#Define: important variables that you need. Natasha goes over these in her paper.
area_frac = 0.5 # area fraction
swell = m.equiv_swell(area_frac)
kick = .05
cycle_number = 15 #This is the number of shears that you do to your system.
scale_x = .9
scale_y = 1


kwargs = dict(hist_kws={'alpha':.6}, kde_kws={'linewidth':2})
plt.figure(figsize=(10,7), dpi= 80)
sns.set_style('darkgrid')

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
ax = sns.distplot(x, bins=10, kde=True, norm_hist=True, label="initial", **kwargs)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)


pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta")
ax = sns.distplot(x, bins=10, kde=True, norm_hist=True, label="after 15 cycles", **kwargs)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta (radians)")
ax = sns.distplot(x, bins=10, kde=True, norm_hist=True, label="after 30 cycles", **kwargs)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta (radians)")
ax = sns.distplot(x, bins=10, kde=True, norm_hist=True, label="after 45 cycles", **kwargs)


plt.ylim(0,1)
plt.legend();