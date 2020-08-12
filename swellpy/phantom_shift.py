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
seed = 7
m = Monodisperse2(N,Bx,By,seed)


area_frac = [.2,.3,.4,.5,.6,.7,.8]
kick = .05
#swell = m.equiv_swell(area_frac)
cycle_number = 30000
xform = .90
area_frac_array = np.array(np.linspace(0,1,100))

#Read along y axis(wrote along x)
for a in area_frac:
    m = Monodisperse2(N,Bx,By,seed)
    m.train_xform(xform, 1, a, kick, cycle_number, noise=0)
    #m.tag_overlay_plot2(area_frac_array, xform, 1, mode='rate', show=True)
    print('af=',a)
    mem = m.detect_memory_xform(0, 1, .001, 1, xform)
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
#%% Try again
from monodisperse_box_xform import Monodisperse2
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10,7), dpi= 80)
area_frac = [.2,.3,.4,.5,.6,.7,.8]
y1 = [x * .95**4 for x in area_frac]
y2 = [x * .9**4 for x in area_frac]
y3 = [x * .85**4 for x in area_frac]
y4 = [x * .8**4 for x in area_frac]
plt.grid()
plt.plot(area_frac,area_frac,'--')
plt.plot(area_frac,y1)
plt.plot(area_frac,y2)
plt.plot(area_frac,y3)
plt.plot(area_frac,y4)
plt.xlabel('Memory Written (area fraction)')
plt.ylabel('Memory Read (area fraction)')
plt.title('Off-Axis Read-Out')
plt.legend(['On-Axis Read-Out','Transform = 0.95','Transform = 0.90','Transform = 0.85','Transform = 0.80'])
plt.ylim([0,0.85])
plt.show()

y1 = [x * .95**2 for x in area_frac]
y2 = [x * .9**2 for x in area_frac]
y3 = [x * .85**2 for x in area_frac]
y4 = [x * .8**2 for x in area_frac]
plt.grid()
plt.plot(area_frac,area_frac,'--')
plt.plot(area_frac,y1)
plt.plot(area_frac,y2)
plt.plot(area_frac,y3)
plt.plot(area_frac,y4)
plt.xlabel('Memory Written (area fraction)')
plt.ylabel('Phantom Memory (area fraction)')
plt.title('Isotropic Read-Out')
plt.legend(['X Read-Out','Transform = 0.95','Transform = 0.90','Transform = 0.85','Transform = 0.80'])
plt.ylim([0,0.85])
plt.show()

#%% AT SMALL TRANSFORM SIZES
'''
Transform: xform = 0.95
'''
#Y-Axis
area_frac = [.2,.3,.4,.5,.6,.7,.8]
y1 = [x * .95**4 for x in area_frac]

# kick1 = 0.1
y_data1 = [.189,.279,.381,.441,.504,.605,.69]
# kick = 0.075
y_data2 = [.171,.255,.345,.432,.531,.615,.675]
# kick = 0.05
y_data3 = [.174,.266,.327,.412,.544,.581,.665]
# kick = 0.03
y_data4 = [.168,.249,.327,.414,.498,.576,.669]

plt.grid()
plt.plot(area_frac,y1,'-.')
plt.plot(area_frac,y_data1, '-o')
plt.plot(area_frac,y_data2, '-o')
plt.plot(area_frac,y_data3, '-o')
plt.plot(area_frac,y_data4, '-o')
plt.xlabel('Memory Written (area fraction)')
plt.ylabel('Phantom Memory (area fraction)')
plt.title('Y-Axis Read-Out')
plt.legend(['Transform=0.95 Theory','kick = 0.1','kick = 0.075','kick = 0.05','kick = 0.03'])
plt.ylim([0,0.85])
plt.show()

'''
Transform: xform = 0.90
'''
#Y-Axis
y2 = [x * .9**4 for x in area_frac]

# kick1 = 0.1
y_data1 = [.168,.252,.3,.348,.468,.474,.546]
# kick = 0.075
y_data2 = [.155,.2,.291,.335,.44,.494,.483]
# kick = 0.05
y_data3 = [.13,.21,.268,.33,.40,.464,.525] 
# kick = 0.03
y_data4 = [.136,.2,.264,.33,.396,.462,.528]

plt.grid()
plt.plot(area_frac,y2,'-.')
plt.plot(area_frac,y_data1, '-o')
plt.plot(area_frac,y_data2, '-o')
plt.plot(area_frac,y_data3, '-o')
plt.plot(area_frac,y_data4, '-o')
plt.xlabel('Memory Written (area fraction)')
plt.ylabel('Phantom Memory (area fraction)')
plt.title('Y-Axis Read-Out')
plt.legend(['Transform=0.90 Theory','kick = 0.1','kick = 0.075','kick = 0.05','kick = 0.03'])
plt.ylim([0,0.85])
plt.show()

#Isotropic Reading
y_i2 = [x * .9**2 for x in area_frac]

# kick1 = 0.1
af_kick1 = [.168,.276,.366,.468,.525,.613,.669]
# kick2 = 0.075
af_kick2 = [.165,.25,.385,.455,.513,.612,.678]
# kick3 = 0.05
af_kick3 = [.165,.255,.33,.413,.498,.578,.65]
# kick4 = 0.03
af_kick4 = [.168,.275,.332,.433,.491,.576,.651]

plt.grid()
plt.plot(area_frac, y_i2,'-.')
plt.plot(area_frac,af_kick1, '-o')
plt.plot(area_frac,af_kick2, '-o')
plt.plot(area_frac, af_kick3, '-o')
plt.plot(area_frac,af_kick4, '-o')
plt.xlabel('Memory Written (area fraction)')
plt.ylabel('Phantom Memory (area fraction)')
plt.title('Isotropic Read-Out')
plt.legend(['Transform=0.90 Theory','kick = 0.1','kick = 0.075','kick = 0.05','kick = 0.03'])
plt.ylim([0,0.85])
plt.show()

'''
Transform: xform = 0.80
'''
#Y-Axis
y4 = [x * .8**4 for x in area_frac]

# kick1 = 0.1
y_data1 = [.171,.165,.225,.237,.247,.306,.378]
# kick = 0.075
y_data2 = [.099,.159,.173,.249,.285,.34,.391]
# kick = 0.05
y_data3 = [.088,.124,.196,.228,.256,.356,.39] 
# kick = 0.03
y_data4 = [.088,.18,.18,.366,.249,.309,.354]

plt.grid()
plt.plot(area_frac,y4,'-.')
plt.plot(area_frac,y_data1, '-o')
plt.plot(area_frac,y_data2, '-o')
plt.plot(area_frac,y_data3, '-o')
plt.plot(area_frac,y_data4, '-o')
plt.xlabel('Memory Written (area fraction)')
plt.ylabel('Phantom Memory (area fraction)')
plt.title('Y-Axis Read-Out')
plt.legend(['Transform=0.80 Theory','kick = 0.1','kick = 0.075','kick = 0.05','kick = 0.03'])
plt.ylim([0,0.85])
plt.show()


#%% Error Bar Plot (Concept)
# Using Y-Axis Read-out
# Transform = 0.90
# Kick = 0.05

area_frac = [.2,.3,.4,.5,.6,.7,.8]
y2 = [x * .9**4 for x in area_frac]
af_y2 = [0.13122, 0.19683, 0.26244, 0.32805, 0.39366, 0.45927, 0.52488] #theory at xform .9

# seed = 125
y_data1 = [.13,.21,.268,.33,.40,.464,.525]
# seed = 1
y_data2 = [.147,.205,.264,.335,.402,.474,.535] 
# seed = 2
y_data3 = [.176,.202,.278,.388,.4,.468,.542]
# seed = 4
y_data4 = [.162,.227,.278,.361,.43,.484,.535]
# seed = 5
y_data5 = [.141,.202,.27,.337,.399,.462,.543]
# seed = 6
y_data6 = [.197,.21,.278,.343,.41,.476,.534]
# seed = 7
y_data7 = [.159,.208,.309,.361,.401,.465,.542]

# for i in range(0,7):
#     avg = (y_data1[i]+y_data2[i]+y_data3[i]+y_data4[i]+y_data5[i]+y_data6[i]+y_data7[i])/7
#     print(avg)
    
avg1 = 0.15885714285714286
avg2 = 0.20914285714285713
avg3 = 0.27785714285714286
avg4 = 0.3507142857142857
avg5 = 0.40599999999999997
avg6 = 0.47042857142857136
avg7 = 0.5365714285714286
avg = [0.15885714285714286,0.20914285714285713,0.27785714285714286,0.3507142857142857,0.40599999999999997,0.47042857142857136,0.5365714285714286]

std1 = 0.02087670315672179
std2 = 0.0079359682356178
std3 = 0.013736589007137845
std4 = 0.018994091455083642
std5 = 0.010378549306829228
std6 = 0.0073262179456903154
std7 = 0.00592469752952221
std = [0.02087670315672179,0.0079359682356178,0.013736589007137845,0.018994091455083642,0.010378549306829228,0.0073262179456903154,0.00592469752952221]

# for i in range(0,7):
#     new_list = []
#     new_list.append(y_data1[i])
#     new_list.append(y_data2[i])
#     new_list.append(y_data3[i])
#     new_list.append(y_data4[i])
#     new_list.append(y_data5[i])
#     new_list.append(y_data6[i])
#     new_list.append(y_data7[i])
#     std = np.std(new_list)
#     print(std)
    
y_data_err = [.04478,.03017,.01556,.05995,.03634,.02473,.01712]

plt.grid()
plt.plot(area_frac,y2, '-.')
plt.errorbar(area_frac,avg,yerr=std,fmt='ko', markersize=3, capsize=4)
plt.xlabel('Memory Written (area fraction)')
plt.ylabel('Phantom Memory (area fraction)')
plt.title('Y-Axis Read-Out')
plt.legend(['Transform=0.90 Theory', 'Kick = 0.05'])
plt.ylim([0,0.85])
plt.show()

#%% Error bar code 2
from monodisperse_box_xform import Monodisperse2
import numpy as np
import matplotlib.pyplot as plt
import statistics

N = 1000 
Bx = 40 #box length (x)
By = 40 #box length (y)
seed = [1,2,3,4,5,6,7,8,9,10]
m = Monodisperse2(N,Bx,By,seed)


area_frac = [.2,.3,.4,.5,.6,.7,.8]
kick1 = .1  #0.1,.05,.03
kick2 = 0.05
kick3 = 0.03
kick_vals = [.1]
#swell = m.equiv_swell(area_frac)
cycle_number = 30000
xform = .90
area_frac_array = np.array(np.linspace(0,1,100))


# for kick in kick_vals:
#     print('-----------------------')
#     print('->kick: ', kick)
#     for af in area_frac:
#         print('->af=',af)
#         for val in seed:
#             print('Seed: ', val)
#             m = Monodisperse2(N,Bx,By,val)
#             m.train_xform(xform, 1, af, kick, cycle_number, noise=0)
#             #m.tag_overlay_plot2(area_frac_array, xform, 1, mode='rate', show=True)
#             mem1 = m.detect_memory_xform(0, 1, .005, 1, xform)
#             mem2 = m.detect_memory_xform(0, 1, .003, 1, xform)
#             mem3 = m.detect_memory_xform(0, 1, .001, 1, xform)
#             print(mem1)
#             print(mem2)
#             print(mem3)

y2 = [x * .9**4 for x in area_frac]

#Each list contains 10 seeds, for kick2
# af = 0.2
af2 = [.14,.135,.186,.135,.161,.167,.151,.174,.17]
# af = 0.3
af3 = [.252,.24,.221,.321,.228,.263,.216,.206,.251]
# af = 0.4
af4 = [.28,.292,.279,.2265,.274,.28,.283,.277,.31]
# af = 0.5
af5 = [.341,.359,.339,.405,.36,.343,.372,.3343,.341]
# af = 0.6
af6 = [.415,.402,.495,.41,.423,.448,.423,.425,.435]
# af = 0.7
af7 = [.469,.48,.475,.471,.462,.469,.469,.476,.495,.496]
# af = 0.8
af8 = [.532,.558,.573,.533,.537,.541,.543,.538,.533,.531]

mean = [statistics.mean(af2),statistics.mean(af3),statistics.mean(af4),statistics.mean(af5),statistics.mean(af6),statistics.mean(af7),statistics.mean(af8)]
print(mean)
std = [statistics.stdev(af2),statistics.stdev(af3),statistics.stdev(af4),statistics.stdev(af5),statistics.stdev(af6),statistics.stdev(af7),statistics.stdev(af8)]
print(std)

mean_1 = [0.15766666666666668, 0.24422222222222223, 0.27794444444444444, 0.35492222222222225, 0.43066666666666664, 0.47619999999999996, 0.5419] #kick1
mean_2 = [0.147, 0.2197, 0.2827, 0.3519, 0.41100000000000003, 0.473, 0.5366000000000001] #kick2
mean_3 = [0.1427, 0.2165, 0.2706, 0.3448, 0.4186, 0.46900000000000003, 0.5333] #kick3
std_1 = [0.018384776310850233, 0.03433576043201089, 0.02214503957498784, 0.022501209844016042, 0.027617928959282955, 0.011282237760696631, 0.013510900948657865] #kick1
std_2 = [0.007571877794400368, 0.011776152927750971, 0.01027456406212285, 0.016023940422588527, 0.013333333333333322, 0.009380831519646846, 0.005358275012642703] #kick2
std_3 = [0.00949912276651551, 0.010384282995630148, 0.006380525927469551, 0.014045956318061385, 0.03184755354288091, 0.005715476066494061, 0.006272515001532042] #kick3


plt.figure(figsize=(10,7), dpi= 80)
plt.grid()
plt.plot(area_frac,y2, '-.')
plt.errorbar(area_frac, mean_1, yerr=std_1, fmt='ko', markersize=5, capsize=6)
plt.xlabel('Memory Written (area fraction)')
plt.ylabel('Phantom Memory (area fraction)')
plt.title('Y-Axis Read-Out')
plt.legend(['Transform=0.90 Theory', 'kick = 0.1', 'Kick = 0.05','kick = 0.03'])
plt.ylim([0,0.85])
plt.show()
plt.figure(figsize=(10,7), dpi= 80)
plt.grid()
plt.plot(area_frac,y2, '-.')
plt.errorbar(area_frac, mean_2, yerr=std_2, fmt='ko', markersize=5, capsize=6)
plt.xlabel('Memory Written (area fraction)')
plt.ylabel('Memory Read-Out (area fraction)')
plt.title('Y-Axis Read-Out')
plt.legend(['Transform=0.90 Theory', 'Kick = 0.05'])
plt.ylim([0,0.85])
plt.show()
plt.figure(figsize=(10,7), dpi= 80)
plt.grid()
plt.plot(area_frac,y2, '-.')
plt.errorbar(area_frac, mean_3, yerr=std_3, fmt='go', markersize=5, capsize=6)
plt.xlabel('Memory Written (area fraction)')
plt.ylabel('Phantom Memory (area fraction)')
plt.title('Y-Axis Read-Out')
plt.legend(['Transform=0.90 Theory', 'kick = 0.03'])
plt.ylim([0,0.85])
plt.show()

# plt.grid()
# plt.plot(area_frac,y2, '-.')
# plt.errorbar(area_frac, mean_1, yerr=std_1, fmt='o', markersize=5, capsize=6)
# plt.errorbar(area_frac, mean_2, yerr=std_2, fmt='o', markersize=5, capsize=6)
# plt.errorbar(area_frac, mean_3, yerr=std_3, fmt='o', markersize=5, capsize=6)
# plt.xlabel('Memory Written (area fraction)')
# plt.ylabel('Phantom Memory (area fraction)')
# plt.title('Y-Axis Read-Out')
# plt.legend(['Transform=0.90 Theory', 'kick = 0.1', 'Kick = 0.05','kick = 0.03'])
# plt.ylim([0,0.85])
# plt.show()



















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
plt.grid()
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
plt.grid()
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


#%% For Presentation (Errorbar)
from monodisperse_box_xform import Monodisperse2
import numpy as np
import matplotlib.pyplot as plt
import statistics

N = 1000 
Bx = 40 #box length (x)
By = 40 #box length (y)
seed = [1,2,3,4,5,6,7,8,9,10]
m = Monodisperse2(N,Bx,By,seed)


area_frac = [.2,.3,.4,.5,.6,.7,.8]
kick1 = .1  #0.1,.05,.03
kick2 = 0.05
kick3 = 0.03
kick_vals = [.1]
#swell = m.equiv_swell(area_frac)
cycle_number = 30000
xform = .90
area_frac_array = np.array(np.linspace(0,1,100))


# for kick in kick_vals:
#     print('-----------------------')
#     print('->kick: ', kick)
#     for af in area_frac:
#         print('->af=',af)
#         for val in seed:
#             print('Seed: ', val)
#             m = Monodisperse2(N,Bx,By,val)
#             m.train_xform(xform, 1, af, kick, cycle_number, noise=0)
#             #m.tag_overlay_plot2(area_frac_array, xform, 1, mode='rate', show=True)
#             mem1 = m.detect_memory_xform(0, 1, .005, 1, xform)
#             mem2 = m.detect_memory_xform(0, 1, .003, 1, xform)
#             mem3 = m.detect_memory_xform(0, 1, .001, 1, xform)
#             print(mem1)
#             print(mem2)
#             print(mem3)

y2 = [x * .9**4 for x in area_frac]

#Each list contains 10 seeds, for kick2
# af = 0.2
af2 = [.14,.135,.186,.135,.161,.167,.151,.174,.17]
# af = 0.3
af3 = [.252,.24,.221,.321,.228,.263,.216,.206,.251]
# af = 0.4
af4 = [.28,.292,.279,.2265,.274,.28,.283,.277,.31]
# af = 0.5
af5 = [.341,.359,.339,.405,.36,.343,.372,.3343,.341]
# af = 0.6
af6 = [.415,.402,.495,.41,.423,.448,.423,.425,.435]
# af = 0.7
af7 = [.469,.48,.475,.471,.462,.469,.469,.476,.495,.496]
# af = 0.8
af8 = [.532,.558,.573,.533,.537,.541,.543,.538,.533,.531]

mean = [statistics.mean(af2),statistics.mean(af3),statistics.mean(af4),statistics.mean(af5),statistics.mean(af6),statistics.mean(af7),statistics.mean(af8)]
print(mean)
std = [statistics.stdev(af2),statistics.stdev(af3),statistics.stdev(af4),statistics.stdev(af5),statistics.stdev(af6),statistics.stdev(af7),statistics.stdev(af8)]
print(std)

mean_1 = [0.15766666666666668, 0.24422222222222223, 0.27794444444444444, 0.35492222222222225, 0.43066666666666664, 0.47619999999999996, 0.5419] #kick1
mean_2 = [0.147, 0.2197, 0.2827, 0.3519, 0.41100000000000003, 0.473, 0.5366000000000001] #kick2
mean_3 = [0.1427, 0.2165, 0.2706, 0.3448, 0.4186, 0.46900000000000003, 0.5333] #kick3
std_1 = [0.018384776310850233, 0.03433576043201089, 0.02214503957498784, 0.022501209844016042, 0.027617928959282955, 0.011282237760696631, 0.013510900948657865] #kick1
std_2 = [0.007571877794400368, 0.011776152927750971, 0.01027456406212285, 0.016023940422588527, 0.013333333333333322, 0.009380831519646846, 0.005358275012642703] #kick2
std_3 = [0.00949912276651551, 0.010384282995630148, 0.006380525927469551, 0.014045956318061385, 0.03184755354288091, 0.005715476066494061, 0.006272515001532042] #kick3




plt.figure(figsize=(10,7), dpi= 80)
plt.grid()
plt.plot(area_frac,area_frac,'--')
plt.plot(area_frac,y2, '-')
plt.errorbar(area_frac, mean_2, yerr=std_2, fmt='ko', markersize=5, capsize=6)
plt.xlabel('Memory Written (area fraction)')
plt.ylabel('Memory Read-Out (area fraction)')
#plt.title('Memory Read-Out')
plt.legend(['On-Axis Read-Out Theory', 'Off-Axis Read-out Theory','Off-Axis Read-Out Actual'])
plt.ylim([0,0.85])
plt.show()


