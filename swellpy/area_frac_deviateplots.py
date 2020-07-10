# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 13:16:31 2020

@author: jakem
"""


from monodisperse_box_xform import Monodisperse2
import numpy as np
import matplotlib.pyplot as plt

transform_list = np.arange(1,0,-.05)
transformsize = 1-transform_list
transform_size = []
transform_size.append(transformsize)

# af_dev_1 = []
# af_dev_2 = []
# af_dev_3 = []
# af_dev_4 = []
# af_dev_5 = []
# test_kicks = [0.001, 0.01, 0.05, 0.1, 0.2]

# for kick in test_kicks:
#     print(kick)
#     for xform in np.arange(1,.05,-.1):
#         N = 1000 
#         Bx = 40 
#         By = 40 
#         seed = 115 
#         m = Monodisperse2(N,Bx,By,seed)
#         area_frac = 0.5 
#         swell = m.equiv_swell(area_frac)
#         cycle_number = 200
#         m.train_xform(xform, 1, area_frac, kick, cycle_number, noise=0)
#         area_frac_array = np.array(np.linspace(0,1,100))
#         memory = m.detect_memory(0, 1, .01)
#         af_deviation = memory - area_frac
#         if test_kicks.index(kick) == 0:
#             af_dev_1.append(af_deviation)
#         elif test_kicks.index(kick) == 1:
#             af_dev_1.append(af_deviation)
#         elif test_kicks.index(kick) == 2:
#             af_dev_1.append(af_deviation)
#         elif test_kicks.index(kick) == 3:
#             af_dev_1.append(af_deviation)
#         elif test_kicks.index(kick) == 4:
#             af_dev_5.append(af_deviation)
#         else: 
#             print('index of test_kicks is out of range')
#             break
#     print(af_dev_1)
#     print(af_dev_2)
#     print(af_dev_3)
#     print(af_dev_4)
#     print(af_dev_5)
        

for xform in np.arange(.14,0,-.02):
    print(xform)
    af_dev_1 = []
    af_dev_2 = []
    af_dev_3 = []
    af_dev_4 = []
    af_dev_5 = []
    kick = 0.001       #Vary Kick size
    N = 1000 
    Bx = 40 
    By = 40 
    seed = 115 
    m = Monodisperse2(N,Bx,By,seed)
    area_frac = 0.5 
    swell = m.equiv_swell(area_frac)
    cycle_number = 300
    m.train_xform(xform, 1, area_frac, kick, cycle_number, noise=0)
    area_frac_array = np.array(np.linspace(0,1,100))
    memory = m.detect_memory(0, 1, .01)
    af_deviation = memory - area_frac
    print(af_deviation)   
 
    
    
    
# Kick = 0.001
Ts1 = [0,.05,.1,.15,.2,.25,.3,.35,.4,.45,.5,.55,.6,.65,.75,.85,.9]    
af1 = [-.01,-.06,-.1,-.15,-.18,-.22,-.26,-.29,-.32,-.35,-.38,-.4,-.42,-.44,-.47,-.49,-.43] 

# Kick = 0.01   
Ts2 = [0,.05,.1,.15,.2,.25,.3,.35,.4,.45,.5,.55,.6,.65,.7,.75,.8]
af2 = [0,-.05,-.1,-.14,-.18,-.22,-.26,-.29,-.32,-.35,-.38,-.4,-.42,-.44,-.46,-.47,-.48]

# Kick = 0.02
Ts3 = [0,.05,.1,.15,.2,.25,.3,.35,.45,.5,.55,.6,.65,.7,.75,.8,.85]
af3 = [0,-.05,-.09,-.14,-.18,-.22,-.25,-.29,-.35,-.38,-.4,-.42,-.44,-.46,-.47,-.48,-.49]

# Kick = 0.05
Ts4 = [0,.05,.1,.15,.2,.25,.35,.45,.5,.55,.6,.65,.7,.75,.8,.85,.9]
af4 = [0,-.04,-.09,-.13,-.17,-.21,-.19,-.24,-.37,-.4,-.42,-.44,-.46,-.47,-.48,-.49,-.49]

# Kick = 0.1
Ts5 = [0,.1,.15,.25,.3,.35,.4,.47,.5,.53,.6,.65,.7,.75,.85,.9]
af5 = [0,-.07,-.12,-.14,-.08,-.11,-.07,-.35,-.13,-.38,-.41,-.43,-.45,-.38,-.46,-.49]


# fig = plt.figure()
# ax1 = fig.add_subplot(111)

# ax1.plot(Ts1,af2)
# ax1.plot(Ts2,af2)
# ax1.plot(Ts3,af3)
# ax1.plot(Ts4,af4)
# ax1.plot(Ts5,af5)

        
