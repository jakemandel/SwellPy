# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 13:16:31 2020

@author: jakem
"""


from monodisperse_box_xform import Monodisperse2
import numpy as np
import matplotlib.pyplot as plt

transform_list = np.arange(1,.05,-.05)
transformsize = 1-transform_list
transform_size = []
transform_size.append(transformsize)

af_dev_1 = []
af_dev_2 = []
af_dev_3 = []
af_dev_4 = []
af_dev_5 = []
test_kicks = [0.001, 0.01, 0.05, 0.1, 0.2]

for kick in test_kicks:
    print(kick)
    for xform in np.arange(1,.05,-.05):
        N = 1000 
        Bx = 40 
        By = 40 
        seed = 115 
        m = Monodisperse2(N,Bx,By,seed)
        area_frac = 0.5 
        swell = m.equiv_swell(area_frac)
        cycle_number = 500
        m.train_xform(xform, 1, area_frac, kick, cycle_number, noise=0)
        area_frac_array = np.array(np.linspace(0,1,100))
        memory = m.detect_memory(0, 1, .01)
        af_deviation = memory - area_frac
        if test_kicks.index(kick) == 0:
            af_dev_1.append(af_deviation)
        elif test_kicks.index(kick) == 1:
            af_dev_1.append(af_deviation)
        elif test_kicks.index(kick) == 2:
            af_dev_1.append(af_deviation)
        elif test_kicks.index(kick) == 3:
            af_dev_1.append(af_deviation)
        elif test_kicks.index(kick) == 4:
            af_dev_5.append(af_deviation)
        else: 
            print('index of test_kicks is out of range')
            break
print(af_dev_1)
print(af_dev_2)
print(af_dev_3)
print(af_dev_4)
print(af_dev_5)
        
# fig = plt.figure()
# ax1 = fig.add_subplot(111)

# ax1.plot(transform_size,af_dev_1)
# ax1.plot(transform_size,af_dev_2)
# ax1.plot(transform_size,af_dev_3)
# ax1.plot(transform_size,af_dev_4)
# ax1.plot(transform_size,af_dev_5)

        
