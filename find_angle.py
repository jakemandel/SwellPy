# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:18:59 2020

@author: jakem
"""


from swellpy import Monodisperse 
import numpy as np
import matplotlib.pyplot as plt

# initialize the parameters in the class of methods (N,B,seed)
# The code in the monodisperse module lays out how each method works
N = 1000 #number of particles
B = 40 #box side length
seed = 125 #inital particle placement randomization
m = Monodisperse(N,B,seed)

#Define: important variables that you need. Natasha goes over these in her paper.
area_frac = 0.7 # area fraction
swell = m.equiv_swell(area_frac)
kick = .035
swell = m.equiv_swell(area_frac)
cycle_number = 100 #This is the number of shears that you do to your system.

def scale_x(self, x_ratio):
    for i in self.centers:
        i[0] = i[0]*x_ratio

def scale_y(self, y_ratio):
    for i in self.centers:
        i[1] = i[1]*y_ratio

def gen_scale(self, scale, theta):
    for i in self.centers: # Transform
        i[0] = i[0]*(1-(scale*np.cos(theta*np.pi/180)))
    for i in self.centers:
        i[1] = i[1]*(1-(scale*np.sin(theta*np.pi/180)))
    
    
# m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)   
 
# gen_scale(m, .8, 90)
# # m.gen_train_xform(.8, 45, area_frac, kick, cycle_number, noise=0)

# m.particle_plot(area_frac, show=True, extend = True, figsize = (7,7), filename=None)



# area_frac_array = np.array(np.linspace(0,1,100))
# m.tag_plot(area_frac_array, mode='count', show=True, filename=None)
# m.tag_plot(area_frac_array, mode='rate', show=True, filename=None)
# m.tag_plot(area_frac_array, mode='curve', show=True, filename=None)

# particle_centers = []
# pairs_centers = []
# theta = []
# for i in pairs:
#     x1 = m.centers[i[0]][0] # x-coordinate of first particle
#     x2 = m.centers[i[1]][0] # x-coordinate of second particle
#     y1 = m.centers[i[0]][1] # y-coordinate of first particle
#     y2 = m.centers[i[1]][1] # y-coordinate of second particle
#     t = np.arctan((y2-y1)/(x2-x1))*(180/np.pi)
#     theta.append(t)
# #print(theta)
# rounded_theta = [ '%.1f' % elem for elem in theta ]
# print(rounded_theta)
# plt.hist(rounded_theta,80)
# plt.show()
        
# pairs = m._tag(swell)
# theta = m.find_angle(pairs)
# rounded_theta = [ '%.1f' % elem for elem in theta ]
# print(rounded_theta)
# plt.hist(rounded_theta,5)
# plt.ylabel('Count')
# plt.xlabel('Theta')
# plt.show()

theta = m.find_angle2(pairs)
print(theta)

# m.train_xform(.8, 1, area_frac, kick, cycle_number, noise=0)

# pairs = m._tag(swell)
# theta = m.find_angle(pairs)
# rounded_theta = [ '%.1f' % elem for elem in theta ]
# # print(rounded_theta)
# plt.hist(rounded_theta,15)
# plt.show()
# plt.ylabel('Count')


# # initialize the parameters in the class of methods (N,B,seed)
# # The code in the monodisperse module lays out how each method works
# N = 1000 #number of particles
# B = 40 #box side length
# seed = 125 #inital particle placement randomization
# m = Monodisperse(N,B,seed)

# #Define: important variables that you need. Natasha goes over these in her paper.
# area_frac = 0.7 # area fraction
# swell = m.equiv_swell(area_frac)
# kick = .035
# swell = m.equiv_swell(area_frac)
# cycle_number = 7 #This is the number of shears that you do to your system.

# pairs = m._tag(swell)
# theta = m.find_angle(pairs)
# rounded_theta = [ '%.1f' % elem for elem in theta ]
# # print(rounded_theta)
# plt.hist(rounded_theta,15)
# plt.show()
# plt.ylabel('Count')

# m.train_xform(.5, 1, area_frac, kick, cycle_number, noise=0)

# pairs = m._tag(swell)
# theta = m.find_angle(pairs)
# rounded_theta = [ '%.1f' % elem for elem in theta ]
# # print(rounded_theta)
# plt.hist(rounded_theta,15)
# plt.show()
# plt.ylabel('Count')