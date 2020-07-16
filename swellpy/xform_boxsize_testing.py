# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:09:24 2020

@author: jakem
"""


from monodisperse_box_xform import Monodisperse2
import numpy as np

N = 1000 
Bx = 40 
By = 40 
seed = 115 
m = Monodisperse2(N,Bx,By,seed)

area_frac = 0.5 
kick = .05
swell = m.equiv_swell(area_frac)
cycle_number = 300 

m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)

m.train_xform(.7, 1, area_frac, kick, cycle_number, noise=0)

m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)

#Actual Area Fraction = 0.5
#Read out
#Isotropic
area_frac_array = np.array(np.linspace(0,1,100))
m.tag_plot_xform(1, 1, area_frac_array, mode='count', show=True, filename=None)
m.tag_plot_xform(1, 1, area_frac_array, mode='rate', show=True, filename=None)
m.tag_plot_xform(1, 1, area_frac_array, mode='curve', show=True, filename=None)
memory_iso = m.detect_memory_xform(0, 1, .01, 1, 1)
print("Isotropic Memory Read-out:", memory_iso)

#Read along x-axis
scale_x1 = .7
scale_y1 = 1
area_frac_array = np.array(np.linspace(0,1,100))
m.tag_plot_xform(scale_x1, scale_y1, area_frac_array, mode='count', show=True, filename=None)
m.tag_plot_xform(scale_x1, scale_y1, area_frac_array, mode='rate', show=True, filename=None)
m.tag_plot_xform(scale_x1, scale_y1, area_frac_array, mode='curve', show=True, filename=None)
memory_x = m.detect_memory_xform(0, 1, .01, scale_x1, scale_y1)
print("Memory Read-out along x-axis:", memory_x)

#Read along y-axis
scale_x2 = 1
scale_y2 = .7
area_frac_array = np.array(np.linspace(0,1,100))
m.tag_plot_xform(scale_x2, scale_y2, area_frac_array, mode='count', show=True, filename=None)
m.tag_plot_xform(scale_x2, scale_y2, area_frac_array, mode='rate', show=True, filename=None)
m.tag_plot_xform(scale_x2, scale_y2, area_frac_array, mode='curve', show=True, filename=None)
memory_y = m.detect_memory_xform(0, 1, .01, scale_x2, scale_y2)
print("Memory Read-out along y-axis:", memory_y)





