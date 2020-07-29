# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 14:18:16 2020

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

area_frac = 0.5
kick_list = [0.5, 0.3, 0.1, 0.05,.01]
cycle_number = 30000
xform = .7
area_frac_array = np.array(np.linspace(0,1,150))


scale_x = xform
scale_y = 1
for kick in kick_list:
    m = Monodisperse2(N,Bx,By,seed)
    count = m.train_xform(xform, 1, area_frac, kick, cycle_number, noise=0)
    print('Cycles:', count)
    m.transform_centers(scale_x, scale_y) #Transform centers along readout axis
    func_count_x = m.tag_count_xform 
    func_rate_x = m.tag_rate_xform
    func_curve_x = m.tag_curve_xform
    data_count_x = func_count_x(area_frac_array, scale_x, scale_y)
    data_rate_x = func_rate_x(area_frac_array, scale_x, scale_y)
    data_curve_x = func_curve_x(area_frac_array, scale_x, scale_y)
    m.inv_transform_centers(scale_x, scale_y) #Transform centers back
    mem2 = m.detect_memory_xform(0, 1, .005, scale_x,scale_y)
    print('x-axis:', mem2)
    plt.plot(area_frac_array, data_rate_x)
    
plt.ylim([0,.9])
#plt.xlim([.4,.75])
plt.ylabel('Rate')
plt.xlabel('Area Fraction')
plt.legend(['kick = 0.5','kick = 0.3','kick = 0.1','kick = 0.05','kick = 0.01'])
plt.show()



    
# scale_x = 1
# scale_y = xform
# m.transform_centers(scale_x, scale_y) #Transform centers along readout axis  
# func_count_y = m.tag_count_xform
# func_rate_y = m.tag_rate_xform
# func_curve_y = m.tag_curve_xform
# data_count_y = func_count_y(area_frac_array, scale_x, scale_y)
# data_rate_y = func_rate_y(area_frac_array, scale_x, scale_y)
# data_curve_y = func_curve_y(area_frac_array, scale_x, scale_y)
# m.inv_transform_centers(scale_x, scale_y) #Transform centers back
# mem3 = m.detect_memory_xform(0, 1, .005, scale_x,scale_y)
# print('y-axis:',mem3)


# plt.plot(area_frac_array, data_count_x)
# plt.plot(area_frac_array, data_rate_x)
# plt.plot(area_frac_array, data_curve_x)
# plt.plot(area_frac_array, data_count_y)
# plt.ylabel('Count')
# plt.xlabel('Area Fraction')
# plt.legend(['X-axis', 'Y-axis'])
# plt.show()

# plt.plot(area_frac_array, data_rate_y)
# plt.ylabel('Rate')
# plt.xlabel('Area Fraction')
# plt.legend(['X-axis', 'Y-axis'])
# plt.show()

# plt.plot(area_frac_array, data_curve_y)
# plt.ylabel('Curve')
# plt.xlabel('Area Fraction')
# plt.legend(['Isotropic', 'X-axis', 'Y-axis'])
# plt.show()