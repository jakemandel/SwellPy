# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:20:05 2020

@author: jakem
"""

def scale_x(self, x_ratio):
    for i in self.centers:
        i[0] = i[0]*x_ratio

def scale_y(self, y_ratio):
    for i in self.centers:
        i[1] = i[1]*y_ratio 