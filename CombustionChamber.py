# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 16:15:22 2020

@author: sunge
"""

class CChamber:
    outer_radius = 1
    inner_radius = 1
    length = 1
    pressure = 1
    temp = 1
    mass_flow_rate = 1
    #two constant: defined in diff. file or
    B_C_A = 1
    B_C_N = 1
    def __init__(self,a,b,c,d):
        self.outer_radius = a