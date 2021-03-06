# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 08:54:28 2020

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

area_frac = 0.5
kick = .05
swell = m.equiv_swell(area_frac)
cycle_number = 30000 
xform = .6

#m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)


count = m.train_xform(xform, 1, area_frac, kick, cycle_number, noise=0)
print(count)
m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)


area_frac_array = np.array(np.linspace(0,1,150))

func_count_iso = m.tag_count_xform
func_rate_iso = m.tag_rate_xform
func_curve_iso = m.tag_curve_xform
data_count_iso = func_count_iso(area_frac_array, 1, 1)
data_rate_iso = func_rate_iso(area_frac_array, 1, 1)
data_curve_iso = func_curve_iso(area_frac_array, 1, 1)

mem1 = m.detect_memory_xform(0, 1, .005, 1,1)
print('Isotropic:',mem1)

scale_x = xform
scale_y = 1
for i in m.centers: #Transform centers along readout axis
    i[0] = i[0]*(scale_x/scale_y)
    i[1] = i[1]*(scale_y/scale_x)
func_count_x = m.tag_count_xform 
func_rate_x = m.tag_rate_xform
func_curve_x = m.tag_curve_xform
data_count_x = func_count_x(area_frac_array, scale_x, scale_y)
data_rate_x = func_rate_x(area_frac_array, scale_x, scale_y)
data_curve_x = func_curve_x(area_frac_array, scale_x, scale_y)
for i in m.centers: #Transform centers back
    i[0] = i[0]*(scale_y/scale_x)
    i[1] = i[1]*(scale_x/scale_y)
    
mem2 = m.detect_memory_xform(0, 1, .005, scale_x,scale_y)
print('x-axis:', mem2)
    
scale_x = 1
scale_y = xform
for i in m.centers: #Transform centers along readout axis
    i[0] = i[0]*(scale_x/scale_y)
    i[1] = i[1]*(scale_y/scale_x)    
func_count_y = m.tag_count_xform
func_rate_y = m.tag_rate_xform
func_curve_y = m.tag_curve_xform
data_count_y = func_count_y(area_frac_array, scale_x, scale_y)
data_rate_y = func_rate_y(area_frac_array, scale_x, scale_y)
data_curve_y = func_curve_y(area_frac_array, scale_x, scale_y)
for i in m.centers: #Transform centers back
    i[0] = i[0]*(scale_y/scale_x)
    i[1] = i[1]*(scale_x/scale_y)

mem3 = m.detect_memory_xform(0, 1, .005, scale_x,scale_y)
print('y-axis:',mem3)

plt.plot(area_frac_array, data_count_iso)
plt.plot(area_frac_array, data_count_x)
plt.plot(area_frac_array, data_count_y)
plt.ylabel('Count')
plt.xlabel('Area Fraction')
plt.legend(['Isotropic', 'X-axis', 'Y-axis'])
plt.show()
plt.plot(area_frac_array, data_rate_iso)
plt.plot(area_frac_array, data_rate_x)
plt.plot(area_frac_array, data_rate_y)
plt.ylabel('Rate')
plt.xlabel('Area Fraction')
plt.legend(['Isotropic', 'X-axis', 'Y-axis'])
plt.show()
plt.plot(area_frac_array, data_curve_iso)
plt.plot(area_frac_array, data_curve_x)
plt.plot(area_frac_array, data_curve_y)
plt.ylabel('Curve')
plt.xlabel('Area Fraction')
plt.legend(['Isotropic', 'X-axis', 'Y-axis'])
plt.show()


#%%

af_written = [.11,.22,.3,.41,.51,.61,.7,.79]  
af_read_iso = [.08,.17,.2,.29,.33,.42,.45,.51]
af_read_x = [.05,.09,.12,.18,.22,.26,.29,.32]
af_read_y = [.11,.22,.3,.41,.51,.61,.7,.78]

plt.plot(af_read_iso,af_written)
plt.plot(af_read_x,af_written)
plt.plot(af_read_y,af_written)
plt.ylabel('AF Written')
plt.xlabel('AF Read-Out')
plt.legend(['Isotropic', 'X-axis', 'Y-axis'])
plt.show()

#%% Test function

from monodisperse_box_xform import Monodisperse2
import numpy as np
import matplotlib.pyplot as plt
N = 1000 
Bx = 40 #box length (x)
By = 40 #box length (y)
seed = 125 
m = Monodisperse2(N,Bx,By,seed)


area_frac = 0.5
kick = .05
cycle_number = 1000 
xform = .9

count = m.train_xform(xform, 1/xform, area_frac, kick, cycle_number, noise=0)
print('Cycles:',count)
m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)

m.tag_overlay_plot2(area_frac_array, xform, mode='count', show=True)
m.tag_overlay_plot2(area_frac_array, xform, mode='rate', show=True)
m.tag_overlay_plot2(area_frac_array, xform, mode='curve', show=True)

#%% For presentation
from monodisperse_box_xform import Monodisperse2
import numpy as np
import matplotlib.pyplot as plt

N = 1000 
Bx = 40 #box length (x)
By = 40 #box length (y)
seed = 125 
m = Monodisperse2(N,Bx,By,seed)

area_frac = 0.5
kick = .05
swell = m.equiv_swell(area_frac)
cycle_number = 4000 
xform = .88

#m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)


count = m.train_xform(xform, 1, area_frac, kick, cycle_number, noise=0)
print(count)
m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)


area_frac_array = np.array(np.linspace(0,1,150))

func_count_iso = m.tag_count_xform
func_rate_iso = m.tag_rate_xform
func_curve_iso = m.tag_curve_xform
data_count_iso = func_count_iso(area_frac_array, 1, 1)
data_rate_iso = func_rate_iso(area_frac_array, 1, 1)
data_curve_iso = func_curve_iso(area_frac_array, 1, 1)

mem1 = m.detect_memory_xform(0, 1, .005, 1,1)
print('Isotropic:',mem1)

scale_x = xform
scale_y = 1
for i in m.centers: #Transform centers along readout axis
    i[0] = i[0]*(scale_x/scale_y)
    i[1] = i[1]*(scale_y/scale_x)
func_count_x = m.tag_count_xform 
func_rate_x = m.tag_rate_xform
func_curve_x = m.tag_curve_xform
data_count_x = func_count_x(area_frac_array, scale_x, scale_y)
data_rate_x = func_rate_x(area_frac_array, scale_x, scale_y)
data_curve_x = func_curve_x(area_frac_array, scale_x, scale_y)
for i in m.centers: #Transform centers back
    i[0] = i[0]*(scale_y/scale_x)
    i[1] = i[1]*(scale_x/scale_y)
    
mem2 = m.detect_memory_xform(0, 1, .005, scale_x,scale_y)
print('x-axis:', mem2)
    
scale_x = 1
scale_y = xform
for i in m.centers: #Transform centers along readout axis
    i[0] = i[0]*(scale_x/scale_y)
    i[1] = i[1]*(scale_y/scale_x)    
func_count_y = m.tag_count_xform
func_rate_y = m.tag_rate_xform
func_curve_y = m.tag_curve_xform
data_count_y = func_count_y(area_frac_array, scale_x, scale_y)
data_rate_y = func_rate_y(area_frac_array, scale_x, scale_y)
data_curve_y = func_curve_y(area_frac_array, scale_x, scale_y)
for i in m.centers: #Transform centers back
    i[0] = i[0]*(scale_y/scale_x)
    i[1] = i[1]*(scale_x/scale_y)

mem3 = m.detect_memory_xform(0, 1, .005, scale_x,scale_y)
print('y-axis:',mem3)


xtick = np.arange(0,1,.1)

plt.figure(figsize=(7,5), dpi= 80)
plt.plot(area_frac_array, data_count_x)
plt.plot(area_frac_array, data_count_y,'r')
plt.ylabel('Fraction of Active Particles',fontsize=15)
plt.xlabel('Area Fraction',fontsize=15)
plt.legend(['On-Axis', 'Off-Axis'])
plt.xticks(xtick,fontsize=15)
plt.show()

plt.figure(figsize=(7,5), dpi= 80)
plt.plot(area_frac_array, data_rate_x)
plt.plot(area_frac_array, data_rate_y,'r')
plt.ylabel('First Derivative',fontsize=15)
plt.xlabel('Area Fraction',fontsize=15)
plt.legend(['On-Axis', 'Off-Axis'])
plt.xticks(xtick,fontsize=15)
plt.show()

plt.figure(figsize=(10,7), dpi= 80)
plt.plot(area_frac_array, data_curve_x)
plt.plot(area_frac_array, data_curve_y)
plt.ylabel('(Frac of Active Particles)\'\'',fontsize=15)
plt.xlabel('Area Fraction',fontsize=15)
plt.legend(['On-Axis', 'Off-Axis'])
plt.xticks(xtick,fontsize=15)
plt.show()

#%% For presentation 1
from monodisperse_box_xform import Monodisperse2
import numpy as np
import matplotlib.pyplot as plt

N = 1000 
Bx = 40 #box length (x)
By = 40 #box length (y)
seed = 125 
m = Monodisperse2(N,Bx,By,seed)

area_frac = 0.5
kick = .05
swell = m.equiv_swell(area_frac)
cycle_number = 4000 
xform = .88



count = m.train_xform(xform, 1, area_frac, kick, cycle_number, noise=0)
print(count)


area_frac_array = np.array(np.linspace(0,1,150))

func_count_iso = m.tag_count_xform
func_rate_iso = m.tag_rate_xform
func_curve_iso = m.tag_curve_xform
data_count_iso = func_count_iso(area_frac_array, 1, 1)
data_rate_iso = func_rate_iso(area_frac_array, 1, 1)
data_curve_iso = func_curve_iso(area_frac_array, 1, 1)

scale_x = xform
scale_y = 1
for i in m.centers: #Transform centers along readout axis
    i[0] = i[0]*(scale_x/scale_y)
    i[1] = i[1]*(scale_y/scale_x)
func_count_x = m.tag_count_xform 
func_rate_x = m.tag_rate_xform
func_curve_x = m.tag_curve_xform
data_count_x = func_count_x(area_frac_array, scale_x, scale_y)
data_rate_x = func_rate_x(area_frac_array, scale_x, scale_y)
data_curve_x = func_curve_x(area_frac_array, scale_x, scale_y)
for i in m.centers: #Transform centers back
    i[0] = i[0]*(scale_y/scale_x)
    i[1] = i[1]*(scale_x/scale_y)
    
mem2 = m.detect_memory_xform(0, 1, .005, scale_x,scale_y)
print('x-axis:', mem2)
    
scale_x = 1
scale_y = xform
for i in m.centers: #Transform centers along readout axis
    i[0] = i[0]*(scale_x/scale_y)
    i[1] = i[1]*(scale_y/scale_x)    
func_count_y = m.tag_count_xform
func_rate_y = m.tag_rate_xform
func_curve_y = m.tag_curve_xform
data_count_y = func_count_y(area_frac_array, scale_x, scale_y)
data_rate_y = func_rate_y(area_frac_array, scale_x, scale_y)
data_curve_y = func_curve_y(area_frac_array, scale_x, scale_y)
for i in m.centers: #Transform centers back
    i[0] = i[0]*(scale_y/scale_x)
    i[1] = i[1]*(scale_x/scale_y)

mem3 = m.detect_memory_xform(0, 1, .005, scale_x,scale_y)
print('y-axis:',mem3)

xtick = np.arange(0,1,.1)
plt.figure(figsize=(7,5), dpi= 80)
plt.plot(area_frac_array, data_count_x,'-')
plt.ylabel('Fraction of Active Particles',fontsize=15)
plt.xlabel('Area Fraction',fontsize=15)
plt.title('On-Axis Read-Out',fontsize=15)
plt.xticks(xtick,fontsize=15)
plt.show()

plt.figure(figsize=(7,5), dpi= 80)
plt.plot(area_frac_array, data_count_y,'r')
plt.ylabel('Fraction of Active Particles',fontsize=15)
plt.xlabel('Area Fraction',fontsize=15)
plt.title('Off-Axis Read-out',fontsize=15)
plt.xticks(xtick,fontsize=15)
plt.show()

plt.figure(figsize=(7,5), dpi= 80)
plt.plot(area_frac_array, data_rate_x)
plt.ylabel('First Derivative',fontsize=15)
plt.xlabel('Area Fraction',fontsize=15)
plt.ylim([-.01, 0.45])
plt.xticks(xtick,fontsize=15)
plt.show()

plt.figure(figsize=(7,5), dpi= 80)
plt.plot(area_frac_array, data_rate_y,'r')
plt.ylabel('First Derivative',fontsize=15)
plt.xlabel('Area Fraction',fontsize=15)
plt.ylim([-.01, 0.45])
plt.xticks(xtick,fontsize=15)
plt.show()

# plt.figure(figsize=(10,7), dpi= 80)
# plt.plot(area_frac_array, data_curve_iso)
# plt.ylabel('(Frac of Active Particles)\'\'')
# plt.xlabel('Area Fraction')
# plt.show()
