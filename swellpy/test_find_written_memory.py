# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 09:00:03 2020

@author: jakem
"""


from monodisperse_box_xform import Monodisperse2
import numpy as np
import matplotlib.pyplot as plt
from scipy import random

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

count = m.train_xform(xform, 1, area_frac, kick, cycle_number, noise=0)
print('Cycles:', count)
m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)


area_frac_array = np.array(np.linspace(0,1,100))

plt.axvline(x=0.55,color='r')
m.tag_plot_xform(xform, 1, area_frac_array, mode='rate', show=True, filename=None)
plt.ylim([0, 0.55])
m.tag_plot_xform(1, xform, area_frac_array, mode='rate', show=True, filename=None)

# m.tag_overlay_plot2(area_frac_array, xform, 1, mode='count', show=True)
# m.tag_overlay_plot2(area_frac_array, xform, 1, mode='rate', show=True)
# m.tag_overlay_plot2(area_frac_array, xform, 1, mode='curve', show=True)

mem1 = m.detect_memory_xform(0, 1, .005, 1,1)
print('Isotropic:', mem1)
mem2 = m.detect_memory_xform(0, 1, .005, xform, 1)
print('x-axis:', mem2)
mem3 = m.detect_memory_xform(0, 1, .005, 1, xform)
print('y-axis:', mem3)

# Monte Carlo Area

a = .5
b = a+.05
N = 1000
xrand = random.uniform(a,b,N)

def func(x):
    scale_x = xform
    scale_y = 1
    for i in m.centers: #Transform centers along readout axis
        i[0] = i[0]*(scale_x/scale_y)
        i[1] = i[1]*(scale_y/scale_x)
    func_rate_x = m.tag_rate_xform
    data_rate_x = func_rate_x(x, scale_x, scale_y) #NEED TO EXTRAPOLATE THE RANDOM X VALUE FROM THE FUNC RATE DATA
    for i in m.centers: #Transform centers back
        i[0] = i[0]*(scale_y/scale_x)
        i[1] = i[1]*(scale_x/scale_y)
    return data_rate_x

integral = 0.0

for i in range(N):
    integral += func(xrand[i])
    
answer = (b-a)/float(N)*integral
print(answer)



#%% 
import numpy as np
import matplotlib.pyplot as plt
from scipy import random

a = .5
b = a+.05
N = 1000
xrand = random.uniform(a,b,N)

def func(x):
    return np.sin(x)

integral = 0.0

for i in range(N):
    integral += func(xrand[i])
    
answer = (b-a)/float(N)*integral
print(answer)

#%%

# axis = m.find_axis()
axis = 'y'
written_memory = m.find_written_memory(N, B, 'y', .215, .9)

