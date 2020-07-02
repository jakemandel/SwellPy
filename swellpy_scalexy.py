# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:10:41 2020

@author: jakem
"""


from swellpy import Monodisperse 
import numpy as np

''' 
Normal Training Cycle: No transformations applied.
'''
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
cycle_number = 500 #This is the number of shears that you do to your system.

m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)
m.train(area_frac, kick, cycle_number, noise=0)
m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)

area_frac_array = np.array(np.linspace(0,1,100))
m.tag_plot(area_frac_array, mode='count', show=True, filename=None)
m.tag_plot(area_frac_array, mode='rate', show=True, filename=None)
m.tag_plot(area_frac_array, mode='curve', show=True, filename=None)

''' 
Transformation Applied: y-axis as interaction axis, scaled by factor of 0.8, x-axis left alone.
'''
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
cycle_number = 500 #This is the number of shears that you do to your system.

# Transform 'Box' in one direction
# Tag particles that would interact
# Transform 'Box' back to original magnitude(starting scale)
# Apply kicks to particles that are tagged
     

m.train_xform(1, .8, area_frac, kick, cycle_number, noise=0)

m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)

area_frac_array = np.array(np.linspace(0,1,100))
m.tag_plot(area_frac_array, mode='count', show=True, filename=None)
m.tag_plot(area_frac_array, mode='rate', show=True, filename=None)
m.tag_plot(area_frac_array, mode='curve', show=True, filename=None)

''' 
Transformation Applied: x-axis as interaction axis, scaled by factor of 0.8, y-axis left alone.
'''
# initialize the parameters in the class of methods (N,B,seed)
# The code in the monodisperse module lays out how each method works
N = 1000 #number of particles
B = 40 #box side length
seed = 125 #inital particle placement randomization
m = Monodisperse(N,B,seed)

#Define: important variables that you need. Natasha goes over these in her paper.
area_frac = .7 # area fraction
swell = m.equiv_swell(area_frac)
kick = .035
swell = m.equiv_swell(area_frac)
cycle_number = 500 #This is the number of shears that you do to your system.

# Transform 'Box' in one direction
# Tag particles that would interact
# Transform 'Box' back to original magnitude(starting scale)
# Apply kicks to particles that are tagged


m.train_xform(.8, 1, area_frac, kick, cycle_number, noise=0)

m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)

area_frac_array = np.array(np.linspace(0,1,100))
m.tag_plot(area_frac_array, mode='count', show=True, filename=None)
m.tag_plot(area_frac_array, mode='rate', show=True, filename=None)
m.tag_plot(area_frac_array, mode='curve', show=True, filename=None)

''' 
Transformation Applied: x and y axis scaled by factor of 0.8.
'''
# initialize the parameters in the class of methods (N,B,seed)
# The code in the monodisperse module lays out how each method works
N = 1000 #number of particles
B = 40 #box side length
seed = 125 #inital particle placement randomization
m = Monodisperse(N,B,seed)

#Define: important variables that you need. Natasha goes over these in her paper.
area_frac = .7 # area fraction
swell = m.equiv_swell(area_frac)
kick = .035
swell = m.equiv_swell(area_frac)
cycle_number = 500 #This is the number of shears that you do to your system.

# Transform 'Box' in one direction
# Tag particles that would interact
# Transform 'Box' back to original magnitude(starting scale)
# Apply kicks to particles that are tagged

m.train_xform(.8, .8, area_frac, kick, cycle_number, noise=0)

m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)

area_frac_array = np.array(np.linspace(0,1,100))
m.tag_plot(area_frac_array, mode='count', show=True, filename=None)
m.tag_plot(area_frac_array, mode='rate', show=True, filename=None)
m.tag_plot(area_frac_array, mode='curve', show=True, filename=None)














#Memory Detection
# start = 0
# end = 1000
# incr = 5
# memory = m.detect_memory(start, end, incr)



def scale_x(self, x_ratio):
    for i in self.centers:
        i[0] = i[0]*x_ratio

def scale_y(self, y_ratio):
    for i in self.centers:
        i[1] = i[1]*y_ratio 