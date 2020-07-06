# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:14:14 2020

@author: jakem
"""


from swellpy import Monodisperse 
import numpy as np

# initialize the parameters in the class of methods (N,B,seed)
# The code in the monodisperse module lays out how each method works
N = 1000 #number of particles
B = 40 #box side length
seed = 125 #inital particle placement randomization
m = Monodisperse(N,B,seed)

#Define: important variables that you need. Natasha goes over these in her paper.
area_frac = 0.5 # area fraction
swell = m.equiv_swell(area_frac)
kick = .035
swell = m.equiv_swell(area_frac)
cycle_number = 1 #This is the number of shears that you do to your system.
# Actual Area Fraction: .78125

# Transform 'Box' in one direction
# Tag particles that would interact
# Transform 'Box' back to original magnitude(starting scale)
# Apply kicks to particles that are tagged

#m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)    

m.train_xform(1, 1, area_frac, kick, cycle_number, noise=0)


#m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)

# area_frac_array = np.array(np.linspace(0,1,100))
# m.tag_plot(area_frac_array, mode='count', show=True, filename=None)
# m.tag_plot(area_frac_array, mode='rate', show=True, filename=None)
# m.tag_plot(area_frac_array, mode='curve', show=True, filename=None)
