# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 16:06:20 2020

@author: sunge
"""

class Tank:
    total_volume = 1
    oxi_volume = 1
    init_temp = 1
    tank_mass = 1
    pipe_radius = 1
    
    pressure = 1
    mass_flow_rate = 1
    current_temp = 1

    def __init__(self,a,b,c,d,e):
        self.total_volume = a
        self.oxi_volume = b
        self.init_temp = c
        self.tank_mass = d
        self.pipe_radius = e
        