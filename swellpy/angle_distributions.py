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

m.train_xform(.8, 1, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
theta = m.find_angle2(pairs)
x = pd.Series(theta, name="Theta")
sns.set_style('darkgrid')
ax = sns.distplot(x, kde=True, norm_hist=True,)

m.train_xform(.8, 1, area_frac, kick, cycle_number, noise=0) 

pairs = m._tag(swell)
theta = m.find_angle2(pairs)
x = pd.Series(theta, name="Theta")
sns.set_style('darkgrid')
ax = sns.distplot(x, kde=True, norm_hist=True,)

m.train_xform(.8, 1, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
theta = m.find_angle2(pairs)
x = pd.Series(theta, name="Theta")
sns.set_style('darkgrid')
ax = sns.distplot(x, kde=True, norm_hist=True,)

m.train_xform(.8, 1, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
theta = m.find_angle2(pairs)
x = pd.Series(theta, name="Theta")
sns.set_style('darkgrid')
ax = sns.distplot(x, kde=True, norm_hist=True,)

m.train_xform(.8, 1, area_frac, kick, cycle_number, noise=0) 

pairs = m._tag(swell)
theta = m.find_angle2(pairs)
x = pd.Series(theta, name="Theta")
sns.set_style('darkgrid')
ax = sns.distplot(x, kde=True, norm_hist=True,)

m.train_xform(.8, 1, area_frac, kick, cycle_number, noise=0)
'''

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
cycle_number = 15 #This is the number of shears that you do to your system.



pairs = m._tag(swell)
theta = m.find_angle2(pairs)
x = pd.Series(theta, name="Theta")
sns.set_style('darkgrid')
ax = sns.distplot(x, kde=True, norm_hist=True,)

m.train_xform(1, .8, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
theta = m.find_angle2(pairs)
x = pd.Series(theta, name="Theta")
sns.set_style('darkgrid')
ax = sns.distplot(x, kde=True, norm_hist=True,)

m.train_xform(1, .8, area_frac, kick, cycle_number, noise=0) 

pairs = m._tag(swell)
theta = m.find_angle2(pairs)
x = pd.Series(theta, name="Theta")
sns.set_style('darkgrid')
ax = sns.distplot(x, kde=True, norm_hist=True,)

m.train_xform(1, .8, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
theta = m.find_angle2(pairs)
x = pd.Series(theta, name="Theta")
sns.set_style('darkgrid')
ax1 = sns.distplot(x, kde=True, norm_hist=True,)

m.train_xform(1, .8, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
theta = m.find_angle2(pairs)
x = pd.Series(theta, name="Theta")
sns.set_style('darkgrid')
ax = sns.distplot(x, kde=True, norm_hist=True,)

m.train_xform(1, .8, area_frac, kick, cycle_number, noise=0) 

pairs = m._tag(swell)
theta = m.find_angle2(pairs)
x = pd.Series(theta, name="Theta")
sns.set_style('darkgrid')
ax = sns.distplot(x, kde=True, norm_hist=True,)

m.train_xform(1, .8, area_frac, kick, cycle_number, noise=0)



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

