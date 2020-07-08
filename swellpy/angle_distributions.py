# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 10:15:36 2020

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
cycle_number = 10 #This is the number of shears that you do to your system.

kwargs = dict(hist_kws={'alpha':.6}, kde_kws={'linewidth':2})
plt.figure(figsize=(10,7), dpi= 80)
sns.set_style('darkgrid')

pairs = m._tag(swell)
theta1 = m.find_angle2(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
ax = sns.distplot(x, bins=10, kde=True, norm_hist=True, label="initial", **kwargs)

m.train_xform(.95, 1, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
theta1 = m.find_angle2(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta")
ax = sns.distplot(x, bins=10, kde=True, norm_hist=True, label="after 10 cycles", **kwargs)

m.train_xform(.95, 1, area_frac, kick, cycle_number, noise=0) 

pairs = m._tag(swell)
theta1 = m.find_angle2(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta")
ax = sns.distplot(x, bins=10, kde=True, norm_hist=True, label="after 20 cycles", **kwargs)

m.train_xform(.95, 1, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
theta1 = m.find_angle2(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta")
ax = sns.distplot(x, bins=10, kde=True, norm_hist=True, label="after 30 cycles", **kwargs)

m.train_xform(.95, 1, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
theta1 = m.find_angle2(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta (radians)")
ax = sns.distplot(x, bins=10, kde=True, norm_hist=True, label="after 40 cycles", **kwargs)

#m.train_xform(.95, 1, area_frac, kick, cycle_number, noise=0) 

# pairs = m._tag(swell)
# theta1 = m.find_angle2(pairs)
# theta = [value for value in theta1 if value > 0]
# x = pd.Series(theta, name="Theta(radians)")
# ax = sns.distplot(x, bins=10, kde=True, norm_hist=True, label="after 50 cycles", **kwargs)

plt.ylim(0,.9)
plt.legend();


'''
Write Memory on y-axis
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
cycle_number = 10 #This is the number of shears that you do to your system.

kwargs = dict(hist_kws={'alpha':.6}, kde_kws={'linewidth':2})
plt.figure(figsize=(10,7), dpi= 80)
sns.set_style('darkgrid')


pairs = m._tag(swell)
theta1 = m.find_angle2(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta")
ax = sns.distplot(x, bins=10, kde=True, norm_hist=True, label="initial", **kwargs)

m.train_xform(1, .95, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
theta1 = m.find_angle2(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta")
ax = sns.distplot(x, bins=10, kde=True, norm_hist=True, label="after 10 cycles", **kwargs)

m.train_xform(1, .95, area_frac, kick, cycle_number, noise=0) 

pairs = m._tag(swell)
theta1 = m.find_angle2(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta")
ax = sns.distplot(x, bins=10, kde=True, norm_hist=True, label="after 20 cycles", **kwargs)

m.train_xform(1, .95, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
theta1 = m.find_angle2(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta")
ax1 = sns.distplot(x, bins=10, kde=True, norm_hist=True, label="after 30 cycles", **kwargs)

m.train_xform(1, .95, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
theta1 = m.find_angle2(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta (radians)")
ax = sns.distplot(x, bins=10, kde=True, norm_hist=True, label="after 40 cycles", **kwargs)

#m.train_xform(1, .95, area_frac, kick, cycle_number, noise=0) 

# pairs = m._tag(swell)
# theta1 = m.find_angle2(pairs)
# theta = [value for value in theta1 if value > 0]
# x = pd.Series(theta, name="Theta")
# sns.set_style('darkgrid')
# ax = sns.distplot(x, kde=True, norm_hist=True,)

plt.ylim(0,.9)
plt.legend();



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



pairs = m._tag(swell)
theta = m.find_angle2(pairs)
x = pd.Series(theta, name="Theta")
sns.set_style('darkgrid')
ax = sns.distplot(x, kde=True, norm_hist=True,)

m.train_xform(.8, .8, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
theta = m.find_angle2(pairs)
x = pd.Series(theta, name="Theta")
sns.set_style('darkgrid')
ax = sns.distplot(x, kde=True, norm_hist=True,)

m.train_xform(.8, .8, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
theta = m.find_angle2(pairs)
x = pd.Series(theta, name="Theta")
sns.set_style('darkgrid')
ax = sns.distplot(x, kde=True, norm_hist=True,)

m.train_xform(.8, .8, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
theta = m.find_angle2(pairs)
x = pd.Series(theta, name="Theta")
sns.set_style('darkgrid')
ax1 = sns.distplot(x, kde=True, norm_hist=True,)

m.train_xform(.8, .8, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
theta = m.find_angle2(pairs)
x = pd.Series(theta, name="Theta")
sns.set_style('darkgrid')
ax = sns.distplot(x, kde=True, norm_hist=True,)

m.train_xform(.8, .8, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
theta = m.find_angle2(pairs)
x = pd.Series(theta, name="Theta")
sns.set_style('darkgrid')
ax = sns.distplot(x, kde=True, norm_hist=True,)

m.train_xform(.8, .8, area_frac, kick, cycle_number, noise=0)
'''

