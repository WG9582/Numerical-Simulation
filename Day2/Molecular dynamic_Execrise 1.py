# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

X=[]
T=[]
x0=1
V0=0
k=1
m=1
A=(x0*x0+V0*V0*m/k)**0.5
e0=0.5*k*A*A

#Euler algorithm solve the harmonic oscillator question
def Harmonic_Euler(h,V0,x0,m,k,max_value):
    i=0
    X=[]
    T=[]
    E=[]
    while i<max_value:
        e=(0.5*k*x0*x0+0.5*m*V0*V0)/e0
        E.append(e)
        T.append(i)
        X.append(x0/A)
        x1=x0+V0*h
        V1=V0-(k*x0)/m*h
        V0=V1
        x0=x1
        i=i+h
    return X,T,E
#
Time_step=[0.001,0.005,0.01,0.05]
plt.figure()
plt.subplot(121)
for h in Time_step:
    X,T,E=Harmonic_Euler(h,V0,x0,m,k,40) ##h is the value of delt(t)
    plt.plot(T,X)

plt.subplot(122)
for h in Time_step:
    X,T,E=Harmonic_Euler(h,V0,x0,m,k,40) ##h is the value of delt(t)
    plt.plot(T,E)
#
##Half_timestep algorithm solve the harmonic oscillator question
def Harmonic_half_timestep(h,V0,x0,m,k,max_value):
    i=0
    X=[]
    T=[]
    E=[]
    while i<max_value:
        e=(0.5*k*x0*x0+0.5*m*V0*V0)/e0
        E.append(e)
        T.append(i)
        X.append(x0/A)
        x1=x0+V0*h/2
        V1=V0-(k*x1)/m*h
        x2=x1+0.5*V1*h/m
        x0=x2
        V0=V1
        i=i+h
    return X,T,E
#    
#Time_step=[0.001,0.005,0.01,0.05]
#plt.figure()
#plt.subplot(121)
#for h in Time_step:
#    X,T,E=Harmonic_half_timestep(h,V0,x0,m,k,40) ##h为delt(t)的数值
#    plt.plot(T,X)  
##
#plt.subplot(122)
#for h in Time_step:
#    X,T,E=Harmonic_half_timestep(h,V0,x0,m,k,40) ##h为delt(t)的数值
#    plt.plot(T,E)


#Euler algorithm solve the harmonic oscillator question
#X=[]
#T=[]
#x0=1
#V0=0
#k=1
#m=1
#A=(x0*x0+V0*V0*m/k)**0.5
#e0=0.5*k*A*A
#b=0.05
#def Harmonic_Euler(h,V0,x0,m,k,max_value):
#    i=0
#    X=[]
#    T=[]
#    E=[]
#    while i<max_value:
#        e=(0.5*k*x0*x0+0.5*m*V0*V0)/e0
#        E.append(e)
#        T.append(i)
#        X.append(x0/A)
#        x1=x0+V0*h
#        V1=V0*(1-b*h/m)-(k*x0)/m*h
#        V0=V1
#        x0=x1
#        i=i+h
#    return X,T,E
#
###Half_timestep algorithm solve the harmonic oscillator question
#def Harmonic_half_timestep(h,V0,x0,m,k,max_value):
#    i=0
#    X=[]
#    T=[]
#    E=[]
#    while i<max_value:
#        e=(0.5*k*x0*x0+0.5*m*V0*V0)/e0
#        E.append(e)
#        T.append(i)
#        X.append(x0/A)
#        x1=x0+V0*h/2
#        V1=V0*(1-b*h/m)-(k*x0)/m*h
#        x2=x1+0.5*V1*h/m
#        x0=x2
#        V0=V1
#        i=i+h
#    return X,T,E
#
#Time_step=[0.002,0.005,0.01,0.02]
#plt.figure()
##plt.subplot(221)
##for h in Time_step:
##    X,T,E=Harmonic_Euler(h,V0,x0,m,k,40) ##h is the value of delt(t)
##    plt.plot(T,X)
#
##plt.subplot(222)
##for h in Time_step:
##    X,T,E=Harmonic_Euler(h,V0,x0,m,k,40) ##h is the value of delt(t)
##    plt.plot(T,E)
##
##plt.subplot(223)
#for h in Time_step:
#    X,T,E=Harmonic_half_timestep(h,V0,x0,m,k,40) ##h is the value of delt(t)
#    plt.plot(T,X)
###
#plt.subplot(224)
#for h in Time_step:
#    X,T,E=Harmonic_half_timestep(h,V0,x0,m,k,40) ##h is the value of delt(t)
#    plt.plot(T,E)



#ra=14.71  ##(10^7km)
#rb=15.21  ##(10^7km)
#vp=29.29  ##(km/s)
#va=30.29  ##（km/s)
#M=1.989 ##(10^30 kg)
#m=5.965 ##(10^24kg)
#G=6.67 ##(10^-11 N*m^2*kg^(-2))
#
#def Earth_orbiting_around_the_Sun(h,Vx0,Vy0,x0,y0,G,M,m,max_value):
#    i=0
#    X=[]
#    Y=[]
#    T=[]
#    E=[]
#    while i<max_value:
#        r0=(x0*x0+y0*y0)**0.5
#        e=0.5*m*Vx0*Vx0+0.5*m*Vy0*Vy0-G*m*M/(r0)
#        E.append(e)
#        T.append(i)
#        X.append(x0)
#        Y.append(y0)
#        x1=x0+Vx0*h/2
#        y1=y0+Vy0*h/2
#        r1=(x1*x1+y1*y1)**0.5
#        Vx1=Vx0-(G*M*m)/(r1)*(x1/r1)/m*h
#        Vy1=Vy0-(G*M*m)/(r1)*(y1/r1)/m*h
#        x2=x1+(Vx1/m)*(h/2)
#        y2=y1+(Vy1/m)*(h/2)
#        x0=x2
#        y0=y2
#        Vx0=Vx1
#        Vy0=Vy1
#        
#    return X,Y,E
#
#x0=ra
#y0=0
#Vx0=0
#Vy0=va

    