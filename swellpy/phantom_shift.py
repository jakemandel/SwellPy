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
kick = .03
#swell = m.equiv_swell(area_frac)
cycle_number = 15000
xform = .9
area_frac_array = np.array(np.linspace(0,1,100))

#Read along y axis(wrote along x)
for a in area_frac:
    m = Monodisperse2(N,Bx,By,seed)
    m.train_xform(xform, 1/xform, a, kick, cycle_number, noise=0)
    #m.tag_overlay_plot2(area_frac_array, xform, mode='rate', show=True)
    print('af=',a)
    mem = m.detect_memory_xform(0, 1, .003, 1/xform, xform)
    print(mem)



#Theory curve for isotropic read-out
# for T in xform:
#     print('Transform',T)
#     af_read = []
#     for a in area_frac:
#         r_x = Bx*np.sqrt(a/(N*np.pi))
#         af_yread = (N*np.pi*(r_x*T)**2)/(Bx*By)
#         af_yread = round(af_yread,5)
#         af_read.append(af_yread)
#     print(af_read)





# Theory curve
# y-axis
# for T in xform:
#     print('Transform',T)
#     af_read = []
#     for a in area_frac:
#         r_x = Bx*np.sqrt(a/(N*np.pi))
#         af_yread = (N*np.pi*(r_x*T**2)**2)/(Bx*By)
#         af_yread = round(af_yread,5)
#         af_read.append(af_yread)
#     print(af_read)
        
        
                


#isotropic

#x-axis
#linear


#%% Plot

from monodisperse_box_xform import Monodisperse2
import numpy as np
import matplotlib.pyplot as plt

'''
Theory Curves for y-axis and isotropic memory read-outs for a written memory on the x-axis.
'''
area_frac = [.2,.3,.4,.5,.6,.7,.8]

# Y-AXIS
af_y1 = [0.1629, 0.24435, 0.3258, 0.40725, 0.4887, 0.57015, 0.65161] #xform = .95
af_y2 = [0.13122, 0.19683, 0.26244, 0.32805, 0.39366, 0.45927, 0.52488]
af_y3 = [0.1044, 0.1566, 0.2088, 0.261, 0.3132, 0.3654, 0.4176]
af_y4 = [0.08192, 0.12288, 0.16384, 0.2048, 0.24576, 0.28672, 0.32768]
af_y5 = [0.06328, 0.09492, 0.12656, 0.1582, 0.18984, 0.22148, 0.25313]
af_y6 = [0.04802, 0.07203, 0.09604, 0.12005, 0.14406, 0.16807, 0.19208]
af_y7 = [0.0357, 0.05355, 0.0714, 0.08925, 0.1071, 0.12495, 0.14281]
af_y8 = [0.02592, 0.03888, 0.05184, 0.0648, 0.07776, 0.09072, 0.10368]
af_y9 = [0.0183, 0.02745, 0.0366, 0.04575, 0.0549, 0.06405, 0.07321]    #xform = .55
af_y10 = [0.0125, 0.01875, 0.025, 0.03125, 0.0375, 0.04375, 0.05]
af_y11 = [0.0082, 0.0123, 0.0164, 0.0205, 0.0246, 0.0287, 0.03281]
af_y12 = [0.00512, 0.00768, 0.01024, 0.0128, 0.01536, 0.01792, 0.02048]
af_y13 = [0.003, 0.0045, 0.006, 0.0075, 0.009, 0.0105, 0.01201]
af_y14 = [0.00162, 0.00243, 0.00324, 0.00405, 0.00486, 0.00567, 0.00648]
af_y15 = [0.00078, 0.00117, 0.00156, 0.00195, 0.00234, 0.00273, 0.00313]
af_y16 = [0.00032, 0.00048, 0.00064, 0.0008, 0.00096, 0.00112, 0.00128] #xform = 0.2

plt.plot(area_frac,area_frac,'--')
plt.plot(area_frac,af_y1)
plt.plot(area_frac,af_y2)
plt.plot(area_frac,af_y3)
plt.plot(area_frac,af_y4)
# plt.plot(area_frac,af_y5)
# plt.plot(area_frac,af_y6)
# plt.plot(area_frac,af_y7)
# plt.plot(area_frac,af_y8)
# plt.plot(area_frac,af_y9)
plt.xlabel('Memory Written (area fraction)')
plt.ylabel('Phantom Memory (area fraction)')
plt.title('Y-Axis Read-Out')
plt.legend(['X Read-Out','Transform = 0.95','Transform = 0.90','Transform = 0.85','Transform = 0.80'])
plt.show()

# ISOTROPIC
af_i1 = [0.1805, 0.27075, 0.361, 0.45125, 0.5415, 0.63175, 0.722]  #xform = .95
af_i2 = [0.162, 0.243, 0.324, 0.405, 0.486, 0.567, 0.648]
af_i3 = [0.1445, 0.21675, 0.289, 0.36125, 0.4335, 0.50575, 0.578]
af_i4 = [0.128, 0.192, 0.256, 0.32, 0.384, 0.448, 0.512]
af_i5 = [0.1125, 0.16875, 0.225, 0.28125, 0.3375, 0.39375, 0.45]
af_i6 = [0.098, 0.147, 0.196, 0.245, 0.294, 0.343, 0.392]
af_i7 = [0.0845, 0.12675, 0.169, 0.21125, 0.2535, 0.29575, 0.338]
af_i8 = [0.072, 0.108, 0.144, 0.18, 0.216, 0.252, 0.288]
af_i9 = [0.0605, 0.09075, 0.121, 0.15125, 0.1815, 0.21175, 0.242]   #xform = .55
af_i10 = [0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2]
af_i11 = [0.0405, 0.06075, 0.081, 0.10125, 0.1215, 0.14175, 0.162]
af_i12 = [0.032, 0.048, 0.064, 0.08, 0.096, 0.112, 0.128]
af_i13 = [0.0245, 0.03675, 0.049, 0.06125, 0.0735, 0.08575, 0.098]
af_i14 = [0.018, 0.027, 0.036, 0.045, 0.054, 0.063, 0.072]
af_i15 = [0.0125, 0.01875, 0.025, 0.03125, 0.0375, 0.04375, 0.05]
af_i16 = [0.008, 0.012, 0.016, 0.02, 0.024, 0.028, 0.032] #xform = 0.2

plt.plot(area_frac,area_frac,'--')
plt.plot(area_frac,af_i1)
plt.plot(area_frac,af_i2)
plt.plot(area_frac,af_i3)
plt.plot(area_frac,af_i4)
# plt.plot(area_frac,af_i5)
# plt.plot(area_frac,af_i6)
# plt.plot(area_frac,af_i7)
# plt.plot(area_frac,af_i8)
# plt.plot(area_frac,af_i9)
plt.xlabel('Memory Written (area fraction)')
plt.ylabel('Phantom Memory (area fraction)')
plt.title('Isotropic Read-Out')
plt.legend(['X Read-Out','Transform = 0.95','Transform = 0.90','Transform = 0.85','Transform = 0.80'])
plt.show()


#%%
from monodisperse_box_xform import Monodisperse2
import numpy as np
import matplotlib.pyplot as plt

#xform = 0.9
#Theory, Y-Axis Reading
area_frac = [.2,.3,.4,.5,.6,.7,.8]
af_y2 = [0.13122, 0.19683, 0.26244, 0.32805, 0.39366, 0.45927, 0.52488]
#Data (kick1 = 0.05)
af_kick1 = [.13,.21,.268,.33,.40,.464,.525]
#Data (kick2 = 0.03)
af_kick2 = [.136,.2,.264,.33,.396,.462,.528]
#Data (kick3 = 0.1)
af_kick3 = [.168,.252,.3,.348,.468,.474,.546]
#Data (kick4 = 0.075)
af_kick4 = [.155,.2,.291,.335,.44,.494,.483]


plt.plot(area_frac, af_y2,'-.')

plt.plot(area_frac,af_kick3)
plt.plot(area_frac,af_kick4)
plt.plot(area_frac, af_kick1)
plt.plot(area_frac,af_kick2)

plt.xlabel('Memory Written (area fraction)')
plt.ylabel('Phantom Memory (area fraction)')
plt.title('Y-Axis Read-Out')
plt.legend(['Transform=0.9 Theory','kick = 0.1','kick = 0.075','kick = 0.05','kick = 0.03'])
#plt.xlim([.3,.7])
plt.show()

#%%
from monodisperse_box_xform import Monodisperse2
import numpy as np
import matplotlib.pyplot as plt

#xform = 0.9
#Theory, Isotropic Reading
area_frac = [.2,.3,.4,.5,.6,.7,.8]
af_i2 = [0.162, 0.243, 0.324, 0.405, 0.486, 0.567, 0.648]

# kick1 = 0.1
af_kick1 = [.168,.276,.366,.468,.525,.613,.669]
# kick2 = 0.075
af_kick2 = [.165,.25,.385,.455,.513,.612,.678]
# kick3 = 0.05
af_kick3 = [.165,.255,.33,.413,.498,.578,.65]
# kick4 = 0.03
af_kick4 = [.168,.275,.332,.433,.491,.576,.651]

plt.plot(area_frac, af_i2,'-.')

plt.plot(area_frac,af_kick1)
plt.plot(area_frac,af_kick2)
plt.plot(area_frac, af_kick3)
plt.plot(area_frac,af_kick4)

plt.xlabel('Memory Written (area fraction)')
plt.ylabel('Phantom Memory (area fraction)')
plt.title('Isotropic Read-Out')
plt.legend(['Transform=0.9 Theory','kick = 0.1','kick = 0.075','kick = 0.05','kick = 0.03'])
#plt.xlim([.3,.7])
plt.show()

#%% 2nd test
from monodisperse_box_xform import Monodisperse2
import numpy as np
import matplotlib.pyplot as plt

#xform = 0.9
#Theory, Y-Axis Reading
area_frac = [.2,.3,.4,.5,.6,.7,.8]
af_y2 = [0.13122, 0.19683, 0.26244, 0.32805, 0.39366, 0.45927, 0.52488]

#Data (kick1 = 0.1)
af_kick1 = [.114,.18,.192,.231,.27,.336,.36]
#Data (kick2 = 0.075)
af_kick2 = [.111,.176,.22,.34,.39,.354,.372]
#Data (kick3 = 0.05)
af_kick3 = [.13,.18,.194,.222,.298,.313,.371]
#Data (kick4 = 0.03)
af_kick4 = [.093,.135,.219,.216,.27,.345,.432]




plt.plot(area_frac, af_y2,'-.')

plt.plot(area_frac,af_kick1)
plt.plot(area_frac,af_kick2)
plt.plot(area_frac, af_kick3)
plt.plot(area_frac,af_kick4)

plt.xlabel('Memory Written (area fraction)')
plt.ylabel('Phantom Memory (area fraction)')
plt.title('Y-Axis Read-Out')
plt.legend(['Transform=0.9 Theory','kick = 0.1','kick = 0.075','kick = 0.05','kick = 0.03'])
#plt.xlim([.3,.7])
plt.show()