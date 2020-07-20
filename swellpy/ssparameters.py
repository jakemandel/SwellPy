# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 13:45:52 2020

@author: jakem
"""


from monodisperse_box_xform import Monodisperse2
import numpy as np
import matplotlib.pyplot as plt



area_fraction = [.8,.81,.82,.83,.84,.85,.86,.87,.88,.89,.9]
for area_frac in area_fraction:
    N = 1000 
    Bx = 40 #box length (x)
    By = 40 #box length (y)
    seed = 125 
    m = Monodisperse2(N,Bx,By,seed)
    kick = .05
    swell = m.equiv_swell(area_frac)
    cycle_number = 10000 
    xform = .9
    
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
import seaborn as sns
#transform on x axis:
    #Points that reached steady state:

xform1 = [.1,.1,.1,.1,.1,.1] 
xform2 = [.2,.2,.2,.2,.2,.2,.2,.2,.2]
xform3 = [.3,.3,.3,.3,.3,.3,.3,.3,.3] 
xform4 = [.4,.4,.4,.4,.4,.4,.4,.4,.4,.4]
xform5 = [.5,.5,.5,.5,.5,.5,.5,.5,.5,.5,.5]
xform6 = [.6,.6,.6,.6,.6,.6,.6,.6]
xform7 = [.7,.7,.7,.7,.7,.7,.7,.7,.7,.7,.7,.7,.7]
xform8 = [.8,.8,.8,.8,.8,.8,.8,.8,.8,.8,.8,.8]
xform9 = [.9,.9,.9,.9,.9,.9,.9,.9,.9,.9,.9,.9,.9]
  
af_1 = [.1,.2,.3,.4,.5,.52]
af_2 = [.1,.2,.3,.4,.5,.51,.53,.54,.55]
af_3 = [.1,.2,.3,.4,.5,.51,.52,.53,.54]
af_4 = [.1,.2,.3,.4,.42,.45,.46,.47,.48,.49]
af_5 = [.1,.2,.3,.4,.42,.45,.46,.47,.48,.49,.53]
af_6 = [.1,.2,.3,.4,.5,.6,.61,.62]
af_7 = [.1,.2,.3,.4,.5,.6,.61,.62,.63,.64,.65,.66,.67]
af_8 = [.1,.2,.3,.4,.5,.6,.7,.71,.72,.73,.74,.75]
af_9 = [.1,.2,.3,.4,.5,.6,.7,.8,.81,.82,.83,.84,.85]

xform = xform1+xform2+xform3+xform4+xform5+xform6+xform7+xform8+xform9
af = af_1 + af_2 + af_3 + af_4 + af_5 + af_6 + af_7 + af_8 + af_9

# Points that do not reach steady state
xform1x = [.1,.1,.1]
xform2x = [.2,.2]
xform3x = [.3,.3]
xform4x = [.4,.4,.4]
xform5x = [.5,.5,.5,.5,.5]
xform6x = [.6,.6,.6]
xform7x = [.7,.7,.7]
xform8x = [.8,.8,.8]
xform9x = [.9,.9]

af_1x = [.51,.53,.54]
af_2x = [.52,.56]
af_3x = [.55,.56]
af_4x = [.5,.51,.52]
af_5x = [.5,.51,.52,.54,.55]
af_6x = [.63,.64,.65]
af_7x = [.68,.69,.7]
af_8x = [.76,.77,.78]
af_9x = [.86,.87]

xformx = xform1x+xform2x+xform3x+xform4x+xform5x+xform6x+xform7x+xform8x+xform9x
afx = af_1x+af_2x+af_3x+af_4x+af_5x+af_6x+af_7x+af_8x+af_9x

boundary_x = [.1,.2,.3,.4,.5,.6,.7,.8,.9]
boundary_y = [.52,.55,.54,.49,.49,.62,.67,.75,.85]
plt.figure(figsize=(10,7), dpi= 80)
sns.set_style("darkgrid")
plt.plot(boundary_x,boundary_y,"g")
# plt.scatter(xform1,af_1,marker="*")
# plt.scatter(xform2,af_2,marker="*")
# plt.scatter(xform3,af_3,marker="*")
# plt.scatter(xform4,af_4,marker="*")
# plt.scatter(xform5,af_5,marker="*")
# plt.scatter(xform6,af_6,marker="*")
# plt.scatter(xform7,af_7,marker="*")
# plt.scatter(xform8,af_8,marker="*")
# plt.scatter(xform9,af_9,marker="*")
plt.scatter(xform,af,color="g",marker="*")
plt.scatter(xformx,afx,color="r",marker="x")

plt.ylabel('Area Fraction')
plt.xlabel('Transform (scaling factor)')
plt.show()

