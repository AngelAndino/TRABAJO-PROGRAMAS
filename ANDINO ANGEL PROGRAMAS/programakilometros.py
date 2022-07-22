# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 11:31:20 2022

@author: Dell
"""

def l100kmtompg(liters):
    miles=(100*1000)/1609.344
    gallons= liters/3.785411784
    return miles/gallons

def mpgtol100km(miles):
    liters=3.785411784
    kilometers=(miles*1609.344)/1000
    km=kilometers/100 
    return liters/km
print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))