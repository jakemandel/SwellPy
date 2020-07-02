#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 11:53:30 2020

@author: jkwak
"""

from swellpy import Monodisperse
import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib.patches import Ellipse


#initialize the parameters in the class of methods (N,B,seed)
# The code in the monoddisperse module lays out how each method works
N = 1000 #number of particles
B = 40 #box side length
m = Monodisperse(N,B,125)


#np.size ndim=1

#define important variables that you need. Natasha goes over these in her paper.
area_frac = 0.7 # area fraction
swell = m.equiv_swell(area_frac)
kick = 0.05

#gives the initial plot of a particle system 
m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)


#print(m.centers)

def morph(self, ratioX, ratioY):    
    #this uses numpy arrays to multiply each x,y of centers
    particles = self.centers.tolist()
    x = []
    y = []
    for particle in particles:
        i = particle[0]
        x.append(i)
        j = particle[1]
        y.append(j)    
    x=np.array([x])
    y=np.array([y])
    dX = ratioX * x
    dY = ratioY * y
    for a in range(len(dX)):
        point = [dX[a], dY[a]]
        self.centers = []
        self.centers.append(point)
    return(self.centers)
    
def morphTake2(self, ratio):
    '''
    attempt has been sucessful
    '''
    newY = self.centers[:,1] * ratio #gives new Y value for centers
    self.centers[:,1] = newY
    print(self.centers)
    
morphTake2(m, .8)

#gives the adjusted plot of a particle system 
m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)

 
m.tag(area_frac)

d = np.array(swell, ndmin=1)

#morph(m, 1, .8)

#print(m.centers)


# This is the number of shears that you do to your system.
cycle_number = 50

# this is how you train the system. This method is what trains the system.
training = m.train(area_frac, kick, cycles= cycle_number)

print('after')

#particleElliptical_plot(m, area_frac, show=True, extend = True, figsize = (7,7), filename=None)

#creates an a plot of the count_plots
#numpy array of area fraction which it tests a set particle system
area_frac_array = np.array(np.linspace(0,1,100))
m.tag_plot(area_frac_array, mode='count', show=True, filename=None)
m.tag_plot(area_frac_array, mode='rate', show=True, filename=None)
m.tag_plot(area_frac_array, mode='curve', show=True, filename=None)



# This is how we detect memory
start = 0
end = 1000
incr = 10
m.detect_memory(start, end, incr)


#gives the final plot of a particle system 
m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)

