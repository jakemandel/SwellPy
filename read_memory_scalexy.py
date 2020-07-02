# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 10:48:46 2020

@author: jakem
"""

from swellpy import Monodisperse 
import numpy as np

# # Write Memory
# # initialize the parameters in the class of methods (N,B,seed)
# # The code in the monodisperse module lays out how each method works
# N = 1000 #number of particles
# B = 40 #box side length
# seed = 125 #inital particle placement randomization
# m = Monodisperse(N,B,seed)

# #Define: important variables that you need. Natasha goes over these in her paper.
# area_frac = 0.7 # area fraction
# swell = m.equiv_swell(area_frac)
# kick = .035
# swell = m.equiv_swell(area_frac)
# cycle_number = 100 #This is the number of shears that you do to your system.
# m.train_xform(.8, 1, area_frac, kick, cycle_number, noise=0)

# '''
# Read Memory Isotropically
# '''
# area_frac_array = np.array(np.linspace(0,1,100))
# m.tag_plot(area_frac_array, mode='count', show=True, filename=None)
# m.tag_plot(area_frac_array, mode='rate', show=True, filename=None)
# m.tag_plot(area_frac_array, mode='curve', show=True, filename=None)


# # Write Memory
# # initialize the parameters in the class of methods (N,B,seed)
# # The code in the monodisperse module lays out how each method works
# N = 1000 #number of particles
# B = 40 #box side length
# seed = 125 #inital particle placement randomization
# m = Monodisperse(N,B,seed)

# #Define: important variables that you need. Natasha goes over these in her paper.
# area_frac = 0.7 # area fraction
# swell = m.equiv_swell(area_frac)
# kick = .035
# swell = m.equiv_swell(area_frac)
# cycle_number = 100 #This is the number of shears that you do to your system.
# m.train_xform(.8, 1, area_frac, kick, cycle_number, noise=0)
# '''
# Read Memory in x-direction
# '''
# for i in m.centers: # Transform
#     i[0] = i[0]*.8
# for i in m.centers:
#     i[1] = i[1]*1
# area_frac_array = np.array(np.linspace(0,1,100))
# m.tag_plot(area_frac_array, mode='count', show=True, filename=None)
# m.tag_plot(area_frac_array, mode='rate', show=True, filename=None)
# m.tag_plot(area_frac_array, mode='curve', show=True, filename=None)


# Write Memory
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
cycle_number = 100 #This is the number of shears that you do to your system.
m.train_xform(.8, 1, area_frac, kick, cycle_number, noise=0)
'''
Read Memory in y-direction
'''
for i in m.centers: # Transform
    i[0] = i[0]*1
for i in m.centers:
    i[1] = i[1]*.8
area_frac_array = np.array(np.linspace(0,1,100))
m.tag_plot(area_frac_array, mode='count', show=True, filename=None)
m.tag_plot(area_frac_array, mode='rate', show=True, filename=None)
m.tag_plot(area_frac_array, mode='curve', show=True, filename=None)