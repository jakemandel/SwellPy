# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:33:03 2020

@author: jakem
"""


from swellpy import Monodisperse 
import numpy as np
# initialize the parameters in the class of methods (N,B,seed)
# The code in the monodisperse module lays out how each method works
N = 8#number of particles
B = 40 #box side length
seed = 100 #inital particle placement randomization
m = Monodisperse(N,B,seed)

#Define: important variables that you need. Natasha goes over these in her paper.
area_frac = 0.7 # area fraction
swell = m.equiv_swell(area_frac)
kick = 4
swell = m.equiv_swell(area_frac)
cycle_number = 1 #This is the number of shears that you do to your system.

m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)
pairs1 = m._tag(swell)
print(pairs1)

# training = m.train(area_frac, kick, cycles= cycle_number)

# m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)
# pairs2 = m._tag(swell)
# print(pairs2)