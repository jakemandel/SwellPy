# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 13:18:57 2020

@author: jakem
"""


from swellpy import Monodisperse 
import numpy as np
import matplotlib.pyplot as plt


def rot_xform(self, degrees, scale):
    theta = np.radians(degrees)
    r = np.array(( (np.cos(theta), -np.sin(theta)),
               (np.sin(theta),  np.cos(theta)) ))
    print(r)
    for i in self.centers:
        [i[0], i[1]] = np.dot(r, [i[0], i[1]])
    for i in self.centers: #scale
        i[1] = i[1]*scale
    for i in self.centers:
        i[0] = i[0]*(1/scale) # Scale perp axis to keep area the same
        
def rot_invxform(self, degrees, scale):
    theta = np.radians(degrees)
    r1 = np.array(( (np.cos(theta), -np.sin(theta)),
               (np.sin(theta),  np.cos(theta)) ))
    r = np.linalg.inv(r1)
    print(r)
    for i in self.centers: #scale
        i[1] = i[1]*(1/scale)
    for i in self.centers:
        i[0] = i[0]*(scale) # Scale perp axis to keep area the same
    for i in self.centers:
        [i[0], i[1]] = np.dot(r, [i[0], i[1]])
    
    
# def gen_scale(self, scale, theta):
#     for i in self.centers: # Transform
#         i[0] = i[0]*(1-(scale*np.cos(theta*np.pi/180)))
#     for i in self.centers:
#         i[1] = i[1]*(1-(scale*np.sin(theta*np.pi/180)))
        
    
    
    
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
cycle_number = 1 #This is the number of shears that you do to your system.





m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)
     
rot_xform(m, 45, .8)
m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)
rot_invxform(m, 45, .8)

m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)

# m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)

# m.train_rotxform(45, .8, area_frac, kick, cycle_number, noise = 0)

# m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)
        
        
        
        
        
# theta = np.radians(45)
# cent = [[5,5],[4,4],[6,6]]
# r = np.array(( (np.cos(theta), -np.sin(theta)),
#                (np.sin(theta),  np.cos(theta)) ))

# new_cent = []
# for xy_coords in cent:
#     new_xy = np.dot(r, [xy_coords[0], xy_coords[1]])
#     new_cent.append(new_xy)
#     print(new_xy)
# print(new_cent)