# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 13:16:31 2020

@author: jakem
"""


from monodisperse_box_xform import Monodisperse2
import numpy as np

transform_size_1 = []
transform_size_2 = []
transform_size_3 = []
transform_size_4 = []
transform_size_5 = []
af_dev_1 = []
af_dev_2 = []
af_dev_3 = []
af_dev_4 = []
af_dev_5 = []
test_kicks = [0.001, 0.01, 0.05, 0.1, 0.2]

for kick in test_kicks:
    
    for xform in range(1,.05,-.05):
        N = 1000 
        Bx = 40 
        By = 40 
        seed = 115 
        m = Monodisperse2(N,Bx,By,seed)
        area_frac = 0.5 
        kick = .05
        swell = m.equiv_swell(area_frac)
        cycle_number = 1
        m.train_xform(xform, 1, area_frac, kick, cycle_number, noise=0)
        area_frac_array = np.array(np.linspace(0,1,100))
        memory = m.detect_memory(0, 1, .01)
        transformsize = 1-xform
        af_deviation = memory - area_frac
        if test_kicks.index(kick) == 0:
            transform_size_1.append(transformsize)
            af_dev_1.append(af_deviation)
        elif test_kicks.index(kick) == 1:
            transform_size_2.append(transformsize)
            af_dev_1.append(af_deviation)
        elif test_kicks.index(kick) == 2:
            transform_size_3.append(transformsize)
            af_dev_1.append(af_deviation)
        elif test_kicks.index(kick) == 3:
            transform_size_4.append(transformsize)
            af_dev_1.append(af_deviation)
        elif test_kicks.index(kick) == 4:
            transform_size_5.append(transformsize)
            af_dev_5.append(af_deviation)
        else: 
            print('index of test_kicks is out of range')
            break
print(transform_size_1)
print(af_dev_1)
        
        
