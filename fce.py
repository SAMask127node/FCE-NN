import math
import numpy as np
import matplotlib.pyplot as plt
import pdb
import pandas as pd

global distance
distance = 0
global height
height = 2.4956
global m
m = 0.141748
global R_l
R_l = 0.0508
global R_u
R_u = 0.03175
global R_b
R_b = 0.0889
global A
A = 0.0248286665
global interval
interval = 0.001
global run
run = True
global show
show = False
colorer = 'goldenrod'
c_l = 0.06
c_d = 0.91

def iterate():
    global run
    for w_r in range(200,600,2): #6380 rpm in rps
        for theta in range(15,75):
            if(run):
                trajectory(w_r, theta*math.pi/180)
    #print("done")
    run = True

def trajectory(w, theta):
    v = (w*R_l + 9/16*w*R_u)/2
    #print(v)
    s = (w*R_l - 9/16*w*R_u)/(2*math.pi*R_b)
    return runPath(w,v,s,theta)

def runPath(w,v_i,s,theta_i):
    v_x = v_i*math.cos(theta_i)
    v_y = v_i*math.sin(theta_i)
    theta = theta_i
    x_dist = distance
    y_dist = 0.4826
    through = True
    x = [distance]
    y = [0.4826]
    while(through): 
        x_dist -= v_x*interval
        y_dist += v_y*interval
        x.append(x_dist)
        y.append(y_dist)
        v_n = math.sqrt(v_x*v_x + v_y*v_y)
        theta = angle(v_x,v_y)
        magnus = magnusF(s, v_n)
        drag = dragF(v_n)
        v_x -= (magnus*math.sin(theta) + drag*math.cos(theta))*interval
        v_y -= (drag*math.sin(theta) + 9.8 - magnus*math.cos(theta))*interval
        if(x_dist <= 0):
            through = False            
        if(y_dist < 0 or y_dist > 3.3):
            through = False
    global show
    global colorer
    if(show):
        plt.plot(x,y,lw = 1.5, ls = '--',color = colorer, alpha = 0.85)
        return 0;
    offset = np.absolute(height-y_dist)
    if(offset < 0.25):
        if(offset < 0.06):
            print(w/600,theta_i*180/math.pi)
            plt.plot(x[0] ,y[0],'k*', lw = 2)
            plt.plot(x,y, 'm--', lw = 1.5)
            global run
            run = False

global c_l
global c_d
def magnusF(s,v):
    return c_l*(16/3)*(math.pi*math.pi)*1.225*(R_b**3)*s*v/m
def dragF(v):
    return c_d*(1.225/2)*A*(v**2)/m
def angle(x,y):
    return math.atan(y/x)