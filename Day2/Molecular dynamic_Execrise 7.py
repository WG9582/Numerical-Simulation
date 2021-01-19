# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 18:38:37 2021

@author: wangg
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial.distance as spdist

m = 1
sigma = 0.5
eps = 1 
num_particles = 30

x_size = 10
y_size = 10  ##The size of box
h=0.005  ##time_stpes
max_value=40  ##max_time_steps

def LJ(r):  ##define LJ function
    return 24 * eps / r * (2 * (sigma / r) ** 12 - (sigma / r) ** 6)

def Calculate_acceleration(pos):
    
    r = spdist.pdist(pos, "euclidean")  ##Calculate Euclidean distance

    particle_force = spdist.squareform(LJ(r))
    r = spdist.squareform(r) 

    accel = []  ##define acceleration
    for i in range(len(pos)):  
        All_force = 0
        for j in range(len(pos)):
            if i == j:
                continue
            
            direction = pos[i] - pos[j]
            All_force += particle_force[i, j] * direction / r[i, j]  

        #The interaction between the wall and particle,change the direction of the force
        All_force += LJ(np.abs(pos[i][0])) * np.array((1, 0))  
        All_force += LJ(np.abs(pos[i][1])) * np.array((0, 1))  
        All_force += LJ(np.abs(x_size - pos[i][0])) * np.array((-1, 0))  
        All_force += LJ(np.abs(y_size - pos[i][1])) * np.array((0, -1))  

        accel.append(All_force / m)  ##a=F/m
        
    return np.array(accel)


def get_position(h,max_value):
    ang0 = np.random.rand(num_particles) * np.pi * 2
    v0=np.array([*zip(np.cos(ang0), np.sin(ang0))]) ##x,y方向上的速度
    pos0=[[0,0] for i in range(num_particles)]
    
    for i in range(num_particles):
        for j in range(2):
            pos0[i][j]=np.random.randint(1,9)
        
    i=0
    Pos=[]
    T=[]
    while i<max_value:
        Pos.append(pos0)
        T.append(i)
#        for i in range(len(pos0)):
#            for j in range(2):
#                if pos0[i][0]<0.5 or pos0[i][0]>9.5:
#                    v0[i][0]=-1*v0[i][0]
#                if pos0[i][1]<0.5 or pos0[i][1]>9.5:
#                    v0[i][1]=-1*v0[i][1]
        pos1=pos0+v0*h/2
        accel=Calculate_acceleration(pos1)
        v1=v0+accel*h
        pos2=pos1+(v1/m)*(h/2)
        v0=v1
        pos0=pos2
        i=i+h
        
    return Pos,T

Pos,T=get_position(h,max_value)

for t in range(8000):
    if t % 30 == 0:
        plt.figure()
        plt.xlim(0,10.5)
        plt.ylim(0,10.5)
        plt.xticks([])
        plt.yticks([])
        for i in range(len(Pos[t])):
            plt.scatter(Pos[t][i][0],Pos[t][i][1],s=100)
