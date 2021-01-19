# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:52:18 2021

@author: wangg
"""
import math
import numpy as np
import matplotlib.pyplot as plt

d0=1
L0=0.5
A=0.2
w=2*math.pi/25
h=0.05
max_value=40
k=300
m=1
N=10
steps=int(max_value/h)+1
    
X=[[0 for i in range(N)] for i in range(steps)]

for j in range(N):
    X[0][j]=j*d0
    
Y=[[0 for i in range(N)] for i in range(steps)]
V_x=[[0 for i in range(N)] for i in range(steps)]
V_y=[[0 for i in range(N)] for i in range(steps)]
    
i=1
while i<steps:
    
    Y[i][0]=A*np.sin(w*(i+1)) 
    Y[i][N-1]=0
    
    X[i][0]=0
    X[i][N-1]=(N-1)*d0
        ##临时的参数
    x1=[0 for k in range(N)]
    y1=[0 for k in range(N)]
        
    d_left=[0 for k in range(N)]
    u_left_x=[0 for k in range(N)]
    u_left_y=[0 for k in range(N)]
        
    d_right=[0 for k in range(N)]
    u_right_x=[0 for k in range(N)]
    u_right_y=[0 for k in range(N)]
        
    F_x=[0 for k in range(N)]
    F_y=[0 for k in range(N)]
    
        
    for j in range(1,N-1):
        x1[j]=X[i-1][j]+V_x[i][j]*h/2
        y1[j]=Y[i-1][j]+V_y[i][j]*h/2
        
    y1[0]=A*np.sin(w*(i+1)) 
    y1[N-1]=0
    x1[0]=0
    x1[N-1]=(N-1)*d0
          
    for j in range(1,N-1):
        d_left[j]=((x1[j-1]-x1[j])**2+(y1[j-1]-y1[j])**2)**0.5
        u_left_x[j]=(x1[j-1]-x1[j])/d_left[j]
        u_left_y[j]=(y1[j-1]-y1[j])/d_left[j]
#        ##前一个对后一个的相互作用
#        
        d_right[j]=((x1[j+1]-x1[j])**2+(y1[j+1]-y1[j])**2)**0.5
        u_right_x[j]=(x1[j+1]-x1[j])/d_right[j]
        u_right_y[j]=(y1[j+1]-y1[j])/d_right[j]
            
        F_x[j]=k*(d_left[j]-L0)*u_left_x[j]+k*(d_right[j]-L0)*u_right_x[j]
        F_y[j]=k*(d_left[j]-L0)*u_left_y[j]+k*(d_right[j]-L0)*u_right_y[j]
            
    for j in range(1,N-1):
        V_x[i][j]=V_x[i][j]+(F_x[j]/m)*h
        V_y[i][j]=V_y[i][j]+(F_y[j]/m)*h
        X[i][j]=(V_x[i][j]/m)*(h/2)+x1[j]
        Y[i][j]=(V_y[i][j]/m)*(h/2)+y1[j]
    
        
    i=i+1
  

for i in range(800):
    if i % 10==0:
        plt.figure()
        plt.ylim(-0.3, 0.3)
        for j in range(len(X[i])):
            plt.scatter(X[i][j],Y[i][j],color='red')
#for i in range(1,len(X[t])-1):
        plt.plot(X[i],Y[i],color='black')