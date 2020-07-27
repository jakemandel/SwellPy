# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 09:00:03 2020

@author: jakem
"""


from monodisperse_box_xform import Monodisperse2
import numpy as np
import matplotlib.pyplot as plt

N = 1000 
B = 40
Bx = 40 #box length (x)
By = 40 #box length (y)
seed = 125 
m = Monodisperse2(N,Bx,By,seed)


area_frac = 0.5
kick = .05
cycle_number = 10000
xform = .95

count = m.train_xform(xform, 1/xform, area_frac, kick, cycle_number, noise=0)
print('Cycles:',count)
m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)


area_frac_array = np.array(np.linspace(0,1,100))

m.tag_overlay_plot2(area_frac_array, xform, mode='count', show=True)
m.tag_overlay_plot2(area_frac_array, xform, mode='rate', show=True)
m.tag_overlay_plot2(area_frac_array, xform, mode='curve', show=True)

mem1 = m.detect_memory_xform(0, 1, .005, 1,1)
print('Isotropic:', mem1)
mem2 = m.detect_memory_xform(0, 1, .005, xform, 1/xform)
print('x-axis:', mem2)
mem3 = m.detect_memory_xform(0, 1, .005, 1/xform, xform)
print('y-axis:', mem3)

#%%

# axis = m.find_axis()
axis = 'y'
written_memory = m.find_written_memory(N, B, 'y', .215, .9)

