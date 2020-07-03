# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:09:24 2020

@author: jakem
"""


from monodisperse_box_xform import Monodisperse2
import numpy as np

# initialize the parameters in the class of methods (N,B,seed)
# The code in the monodisperse module lays out how each method works
N = 1000 #number of particles
Bx = 40 #box length (x)
By = 40 #box length (y)
seed = 125 #inital particle placement randomization
m = Monodisperse2(N,Bx,By,seed)

#Define: important variables that you need. Natasha goes over these in her paper.
area_frac = 0.5 # area fraction
kick = .25
swell = m.equiv_swell(area_frac)
cycle_number = 150 #This is the number of swells  you do to your system.

m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)

m.train_xform(.8, 1, area_frac, kick, cycle_number, noise=0)

m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)

#Actual Area Fraction = 
#Read out
area_frac_array = np.array(np.linspace(0,1,100))
m.tag_plot(area_frac_array, mode='count', show=True, filename=None)
m.tag_plot(area_frac_array, mode='rate', show=True, filename=None)
m.tag_plot(area_frac_array, mode='curve', show=True, filename=None)

for i in m.centers: # Transform
    i[0] = i[0]*.8
    i[1] = i[1]*1
area_frac_array = np.array(np.linspace(0,1,100))
m.tag_plot(area_frac_array, mode='count', show=True, filename=None)
m.tag_plot(area_frac_array, mode='rate', show=True, filename=None)
m.tag_plot(area_frac_array, mode='curve', show=True, filename=None)
for i in m.centers: # Transform back and to read on y axis
    i[0] = i[0]*(1/.8)
    i[1] = i[1]*.8
    area_frac_array = np.array(np.linspace(0,1,100))
m.tag_plot(area_frac_array, mode='count', show=True, filename=None)
m.tag_plot(area_frac_array, mode='rate', show=True, filename=None)
m.tag_plot(area_frac_array, mode='curve', show=True, filename=None)