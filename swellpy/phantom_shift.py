# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 15:38:12 2020

@author: jakem
"""


from monodisperse_box_xform import Monodisperse2
import numpy as np
import matplotlib.pyplot as plt

N = 1000 
Bx = 40 #box length (x)
By = 40 #box length (y)
seed = 125 
m = Monodisperse2(N,Bx,By,seed)


area_frac = [.2,.3,.4,.5,.6,.7,.8]
kick = .05
#swell = m.equiv_swell(area_frac)
cycle_number = 15000
xform = .95

#Read along y axis(wrote along x)
for a in area_frac:
    m.train_xform(xform, 1, a, kick, cycle_number, noise=0)
    print('af=',a)
    mem = m.detect_memory_xform(0, 1, .001, 1, xform)
    print(mem)




#%% Plot

area_frac = [.2,.3,.4,.5,.6,.7,.8]

#xform = 0.95
#phantom_y = 