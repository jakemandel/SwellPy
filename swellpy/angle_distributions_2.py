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

xform_boxsize_x = 40*scale_x
xform_boxsize_y = 40/scale_y
m.transform_centers(scale_x,scale_y)
pairs = m._tag_xform(swell, xform_boxsize_x, xform_boxsize_y)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
ax = sns.distplot(x, bins=10, kde=False, norm_hist=True, label="initial", **kwargs)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)


pairs = m._tag_xform(swell,xform_boxsize_x, xform_boxsize_y)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta")
ax = sns.distplot(x, bins=10, kde=False, norm_hist=True, label="after 15 cycles", **kwargs)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag_xform(swell,xform_boxsize_x, xform_boxsize_y)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta (radians)")
ax = sns.distplot(x, bins=10, kde=False, norm_hist=True, label="after 30 cycles", **kwargs)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag_xform(swell,xform_boxsize_x, xform_boxsize_y)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta (radians)")
ax = sns.distplot(x, bins=10, kde=False, norm_hist=True, label="after 45 cycles", **kwargs)


plt.xticks([0, 3.14/4, 3.14/2, 3*3.14/4, 3.14], ['0', '$\pi$/4', '$\pi$/2','3$\pi$/4', '$\pi$'],rotation=20)
plt.ylabel('Probability')
plt.ylim(0,1)
plt.legend();

#%% Regular Tagging
from monodisperse_box_xform import Monodisperse2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
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
cycle_number = 20 #This is the number of shears that you do to your system.
scale_x = .9
scale_y = 1

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

pairs = m._tag(swell)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)

plt.xlabel('Theta (radians)')
plt.ylabel('Count')
plt.grid(axis='both')
#%% Transform Tagging
from monodisperse_box_xform import Monodisperse2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
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
scale_x = 1
scale_y = .4

xform_boxsize_x = (m.boxsize_x*scale_x/scale_y)
xform_boxsize_y = (m.boxsize_y*scale_y/scale_x)

m.transform_centers(scale_x, scale_y)
pairs = m._tag_xform(swell,xform_boxsize_x, xform_boxsize_y)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)
m.inv_transform_centers(scale_x, scale_y)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

m.transform_centers(scale_x, scale_y)
pairs = m._tag_xform(swell,xform_boxsize_x, xform_boxsize_y)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)
m.inv_transform_centers(scale_x, scale_y)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

m.transform_centers(scale_x, scale_y)
pairs = m._tag_xform(swell,xform_boxsize_x, xform_boxsize_y)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)
m.inv_transform_centers(scale_x, scale_y)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

m.transform_centers(scale_x, scale_y)
pairs = m._tag_xform(swell,xform_boxsize_x, xform_boxsize_y)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)
m.inv_transform_centers(scale_x, scale_y)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

m.transform_centers(scale_x, scale_y)
pairs = m._tag_xform(swell,xform_boxsize_x, xform_boxsize_y)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)
m.inv_transform_centers(scale_x, scale_y)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

m.transform_centers(scale_x, scale_y)
pairs = m._tag_xform(swell,xform_boxsize_x, xform_boxsize_y)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)
m.inv_transform_centers(scale_x, scale_y)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

m.transform_centers(scale_x, scale_y)
pairs = m._tag_xform(swell,xform_boxsize_x, xform_boxsize_y)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)
m.inv_transform_centers(scale_x, scale_y)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

m.transform_centers(scale_x, scale_y)
pairs = m._tag_xform(swell,xform_boxsize_x, xform_boxsize_y)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)
m.inv_transform_centers(scale_x, scale_y)

m.train_xform(scale_x, scale_y, area_frac, kick, cycle_number, noise=0)

m.transform_centers(scale_x, scale_y)
pairs = m._tag_xform(swell,xform_boxsize_x, xform_boxsize_y)
print(len(pairs))
theta1 = m.find_angle(pairs)
theta = [value for value in theta1 if value > 0]
x = pd.Series(theta, name="Theta(radians)")
plt.hist(x, bins=12,)
m.inv_transform_centers(scale_x, scale_y)

plt.xlabel('Theta (radians)')
plt.ylabel('Count')
plt.grid(axis='both')