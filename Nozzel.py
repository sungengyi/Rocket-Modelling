# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 16:20:40 2020

@author: sunge
"""

class Nozzel:
    throat_area = 1
    outlet_area = 2
    mass = 3
    def __init__(self,a,b,c):
        self.throat_area = a
        self.outlet_area = b
        self.mass = c