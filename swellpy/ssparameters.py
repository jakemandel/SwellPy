# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 13:45:52 2020

@author: jakem
"""


from monodisperse_box_xform import Monodisperse2
import numpy as np
import matplotlib.pyplot as plt



area_fraction = [.5,.51,.52,.53,.54,.55,.56,.57,.58,.59,.6]
for area_frac in area_fraction:
    N = 1000 
    Bx = 40 #box length (x)
    By = 40 #box length (y)
    seed = 125 
    m = Monodisperse2(N,Bx,By,seed)
    kick = .05
    swell = m.equiv_swell(area_frac)
    cycle_number = 10000 
    xform = .2
    
    count = m.train_xform(xform, 1, area_frac, kick, cycle_number, noise=0)
    #m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)
    
    print('Area Fraction:',area_frac)
    print('At steady state after 10,000 cycles?')
    if count < cycle_number:
        print('YES')
    else:
        print('NO')
    
    
    
    
    
    
#%%
from monodisperse_box_xform import Monodisperse2
import numpy as np
import matplotlib.pyplot as plt
#transform on x axis:
    #Points that reached steady state:

xform1 = [.1,.1,.1,.1,.1] 
xform2 = [.2,.2,.2,.2,.2]
xform3 = [.3,.3,.3,.3,.3] 
xform4 = [.4,.4,.4,.4]
xform5 = [.5,.5,.5,.5]
xform6 = [.6,.6,.6,.6,.6,.6]
xform7 = [.7,.7,.7,.7,.7,.7]
xform8 = [.8,.8,.8,.8,.8,.8,.8]
xform9 = [.9,.9,.9,.9,.9,.9,.9,.9]
  
af_x1 = [.1,.2,.3,.4,.5]
af_x2 = [.1,.2,.3,.4,.5]
af_x3 = [.1,.2,.3,.4,.5]
af_x4 = [.1,.2,.3,.4]
af_x5 = [.1,.2,.3,.4]
af_x6 = [.1,.2,.3,.4,.5,.6]
af_x7 = [.1,.2,.3,.4,.5,.6]
af_x8 = [.1,.2,.3,.4,.5,.6,.7]
af_x9 = [.1,.2,.3,.4,.5,.6,.7,.8]

plt.scatter(xform1,af_x1,marker="*")
plt.scatter(xform2,af_x2,marker="*")
plt.scatter(xform3,af_x3,marker="*")
plt.scatter(xform4,af_x4,marker="*")
plt.scatter(xform5,af_x5,marker="*")
plt.scatter(xform6,af_x6,marker="*")
plt.scatter(xform7,af_x7,marker="*")
plt.scatter(xform8,af_x8,marker="*")
plt.scatter(xform9,af_x9,marker="*")
plt.ylabel('Area Fraction')
plt.xlabel('Transform')
plt.show()
