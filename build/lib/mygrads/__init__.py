#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This is a collection of functions implemented in python that replicate
their implementation in GrADS.
Content:
1. Centered Differences (cdifof)
2. Horizontal Divergence (hdivg)
3. Vertical component of the relative vorticity (hcurl)
4. Horizontal Advection (hadv) 

Only requires Numpy.
'''

import numpy as np

def cdiff(scalar,axis=0):
    '''
    Performs the same as GrADS function cdiff()
    http://cola.gmu.edu/grads/gadoc/gradfunccdiff.html
    The scalar quantity must by 2D.
    The finite differences calculation ignores the borders, where np.nan is returned.
    '''
    # Check if 2D
    dimScalar=np.size(np.shape(scalar))
    if dimScalar != 2:
        print("Pystuff Error: scalar must have only 2 dimensions, but it has %d." %dimScalar)
        return
    
    # Length of each dimension
    lendim0=np.shape(scalar)[0]
    lendim1=np.shape(scalar)[1]
    
    # Initialize output var
    out=np.zeros(np.shape(scalar))
    out.fill(np.nan)
    
    # Centered finite differences
    for x in np.arange(1,lendim0-1):
        for y in np.arange(1,lendim1-1):
            if axis==0:
                out[x,y]=scalar[x+1,y]-scalar[x-1,y]
            elif axis==1:
                out[x,y]=scalar[x,y+1]-scalar[x,y-1]
            else:
                print("Pystuff Error: Invalid axis option. Must be either 0 or 1.")
                return
    return out    

def hdivg(u,v,lat,lon):
    '''
    Calculates the horizontal divergence (du/dx+dv/dy) exactly like GrADS. 
    lat and lon are 1D arrays.
    http://cola.gmu.edu/grads/gadoc/gradfunccdiff.html
    '''
    latv, lonv = np.meshgrid(lat, lon, indexing='ij')
    r  = 6.371*(10**6)
    dtr = np.pi/180
    dudx = cdiff(u, axis=1)/cdiff(lonv*dtr, axis=1)
    dvdy = cdiff(v*np.cos(latv*dtr), axis=0)/cdiff(latv*dtr, axis=0)
    out  = (dudx + dvdy)/(r*np.cos(latv*dtr))
    return out

def hcurl(u,v,lat,lon):
    '''
    Calculates the vertical component of the relative vorticity (dv/dx-du/dy) exactly like GrADS. 
    lat and lon are 1D arrays.
    http://cola.gmu.edu/grads/gadoc/gradfunccdiff.html
    '''
    latv, lonv = np.meshgrid(lat, lon, indexing='ij')
    r  = 6.371*(10**6)
    dtr = np.pi/180
    dvdx = cdiff(v, axis=1)/cdiff(lonv*dtr, axis=1)
    dudy = cdiff(u*np.cos(latv*dtr), axis=0)/cdiff(latv*dtr, axis=0)
    out  = (dvdx - dudy)/(r*np.cos(latv*dtr))
    return out

def hadv(u,v,t,lat,lon):
    '''
    Calculates the advection of a scalar variable. 
    lat and lon are 1D arrays.
    http://cola.gmu.edu/grads/gadoc/gradfunccdiff.html
    '''
    latv, lonv = np.meshgrid(lat, lon, indexing='ij')
    dtr = np.pi/180 
    r   = 6.371*(10**6)
    dtx = cdiff (t, axis=1)
    dty = cdiff (t, axis=0)
    dx  = cdiff(lonv, axis=1)*dtr 
    dy  = cdiff(latv, axis=0)*dtr
    out = -( (u*dtx)/(np.cos(latv*dtr)*dx) + v*dty/dy )/r 
    return out


