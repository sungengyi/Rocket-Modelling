# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 16:06:20 2020

@author: sunge
"""

#import CoolProp as cp

class Tank:
    total_volume = 1
    oxidizer_mass = 1
    initial_temp = 1
    tank_dry_mass = 1
    outlet_diameter = 1

    def __init__(self, init):
        self.total_volume = init[0]
        self.tank_dry_mass = init[1]
    '''
        self.total_volume = a
        self.oxidizer_mass = b
        self.initial_temp = c
        self.tank__dry_mass = d
        self.outlet_diameter = e
    '''

# example usage of PropsSI: PropsSI("T", "P", 101325, "Q", 0, "Water")
#finds temperature of water at pressure 101325 Pa and Quality 0 (which is equivalent to boiling temp)

    def converge(self):
        x = 10

    def update(self, dt, oxidiser_mass_flow_rate):
        #used to move timestep forward
        self.oxidizer_mass -= self.mass_flow_rate * dt


