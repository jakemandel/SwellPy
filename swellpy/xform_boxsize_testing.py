# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:09:24 2020

@author: jakem
"""


import Monodisperse

# initialize the parameters in the class of methods (N,B,seed)
# The code in the monodisperse module lays out how each method works
N = 1000 #number of particles
Bx = 40 #box side length
By = 40
seed = 125 #inital particle placement randomization
m = Monodisperse(N,B,seed)

#Define: important variables that you need. Natasha goes over these in her paper.
area_frac = 0.5 # area fraction
swell = m.equiv_swell(area_frac)
kick = .035
swell = m.equiv_swell(area_frac)
cycle_number = 500 #This is the number of shears that you do to your system.