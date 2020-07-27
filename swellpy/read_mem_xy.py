# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 10:45:35 2020

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


area_frac_x = 0.5
kick = .05
#swell = m.equiv_swell(area_frac)
cycle_number_x = 25
xform = .9

#m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)


count = m.train_xform(xform, 1/xform, area_frac_x, kick, cycle_number_x, noise=0)
print('Cycles:',count)
m.particle_plot(area_frac_x, show=True, extend = True, figsize = (7,7), filename=None)


area_frac_array = np.array(np.linspace(0,1,100))

func_count_iso = m.tag_count_xform
func_rate_iso = m.tag_rate_xform
func_curve_iso = m.tag_curve_xform
data_count_iso = func_count_iso(area_frac_array, 1, 1)
data_rate_iso = func_rate_iso(area_frac_array, 1, 1)
data_curve_iso = func_curve_iso(area_frac_array, 1, 1)

mem1 = m.detect_memory_xform(0, 1, .005, 1,1)
print('Isotropic:',mem1)

scale_x = xform
scale_y = 1/xform
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
    
scale_x = 1/xform
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


# Transform y axis
area_frac_y = 0.3
cycle_number_y = 5000

count = m.train_xform(1, xform, area_frac_y, kick, cycle_number_y, noise=0)
print('Cycles:',count)
m.particle_plot(area_frac_y, show=True, extend = True, figsize = (7,7), filename=None)
area_frac_array = np.array(np.linspace(0,1,100))

func_count_iso = m.tag_count_xform
func_rate_iso = m.tag_rate_xform
func_curve_iso = m.tag_curve_xform
data_count_iso = func_count_iso(area_frac_array, 1, 1)
data_rate_iso = func_rate_iso(area_frac_array, 1, 1)
data_curve_iso = func_curve_iso(area_frac_array, 1, 1)

mem1 = m.detect_memory_xform(0, 1, .005, 1,1)
print('Isotropic:',mem1)

scale_x = xform
scale_y = 1/xform
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
    
scale_x = 1/xform
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