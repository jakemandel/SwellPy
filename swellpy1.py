# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 13:15:21 2020

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
area_frac = 0.7 # area fraction
swell = m.equiv_swell(area_frac)
kick = 1
swell = m.equiv_swell(area_frac)
cycle_number = 50 #This is the number of shears that you do to your system.

# Transform 'Box' in one direction
# Tag particles that would interact
# Transform 'Box' back to original magnitude(starting scale)
# Apply kicks to particles that are tagged
#       Question: Is a particle tagged multiple times in varying directions if tagged
#       by multiple particles in varying directions?

m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)
print('^Before Transformation')
tag_before = m.tag_count(area_frac)
print('tagged:',tag_before)
print(m.centers)
def scale_x(self, x_ratio):
    for i in self.centers:
        i[0] = i[0]*x_ratio

def scale_y(self, y_ratio):
    for i in self.centers:
        i[1] = i[1]*y_ratio    
        
scale_x(m,.8)
print(m.centers)
# AFTER Transformation
m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)
print('^After Transformation')
tag_after = m.tag_count(area_frac)
print('tagged:',tag_after)

tag_coords = m._tag(swell)  #tagged centers after transformation

#print('BEFORE SCALE BACK:',m.centers)
scale_x(m,1.25)
# inv_coords = []
# for i in tag_coords:
#     i[1] = i[1]*1.25
#print('AFTER SCALE BACK',m.centers)
    
m.repel(tag_coords, area_frac, kick)
m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)

# this is how you train the system. This method is what trains the system.
#training = m.train(area_frac, kick, cycles= cycle_number)

#gives the plot of a particle system 
# m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)

#creates an a plot of the count_plots
#numpy array of area fraction which it tests a set particle system
# area_frac_array = np.array(np.linspace(0,1,100))
# m.tag_plot(area_frac_array, mode='rate', show=True, filename=None)





# Memory Detection
# start = 0
# end = 1000
# incr = 5
# memory = m.detect_memory(start, end, incr)

# I had to change the memory detection module in the monodisperse module a 
#little bit to work. I changed a numpy arrange to a linspace. 
