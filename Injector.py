# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 16:13:36 2020

@author: sunge
"""

class Injector:
    area = 1
    length = 1
    mass = 1
    pressure = 1
    mass_flow_rate = 1
    temp = 1
    def __init__(self,a,b,c):
        self.area = a
        self.length = b
        self.mass = c