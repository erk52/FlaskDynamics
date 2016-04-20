# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 14:30:37 2016

@author: EKish
"""

from numpy import *
import matplotlib.pyplot as plt
import mpld3

def phasePlot(Ufunc, Vfunc):
    
    def U(x,y):
        return eval(Ufunc)
    def V(x,y):
        return eval(Vfunc)
    
    x,y = meshgrid(arange(-3,3,0.1), arange(-3,3,0.1))
    
    fig, ax = plt.subplots(figsize=(8,8))
    ax.streamplot(x,y,U(x,y), V(x,y))
    return mpld3.fig_to_html(fig)