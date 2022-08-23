#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 17:33:29 2022

@author: phygmw
"""

import numpy as np

"""
import argparse

# Take the name of the .fits file as an input arguement:
parser=argparse.ArgumentParser(description='''Script to retrieve beam information from .fits files with CASA.''')
parser.add_argument("-I","--imagename",action='store',dest='imagename',default='',type=str,help="Name of .fits file") # default=''
args=parser.parse_args()

imagename = args.imagename
"""


# Open the image in CASA:
ia.open(imagename)

# Get the restoring beam dictionary:
b = ia.restoringbeam()

# Some fits files have multiple beams (i.e. one per channel), others have just one.
# Need to define the keyword so we can check for the case with multiple beams or not:
key = 'beams'


if key in b:
    # If the dictionary has the key 'beams', there are multiple beams:
        
    # Empty lists for storing parameters:
    bmaj = []
    bmin = []
    bpa = []
    
    # Number of channels:
    nchans = len(b['beams']) 
    print("A beam per channel, nbeams = ", str(nchans))
    
    # Loop over the channels, and get the major, minor and PA values:
    for i in range(0,nchans):
        # Major:
        bmaj.append(b['beams']['*'+str(i)]['*0']['major']['value'])
        # Minor:
        bmin.append(b['beams']['*'+str(i)]['*0']['minor']['value'])
        # Position angle:
        bpa.append(b['beams']['*'+str(i)]['*0']['positionangle']['value'])
        
    print("Min, max and mean of BMAJ:", np.round(np.min(bmaj),4), np.round(np.max(bmaj),4), np.round(np.mean(bmaj),4))
    print("Min, max and mean of BMIN:", np.round(np.min(bmin),4), np.round(np.max(bmin),4), np.round(np.mean(bmin),4))
    print("Min, max and mean of BPA:", np.round(np.min(bpa),4), np.round(np.max(bpa),4), np.round(np.mean(bpa),4))


        
else:
    print("Only one defined beam")

    # 'beams' is not in the dictionary, so must only be one beam in this file:
    bmaj = b['major']['value']
    # Minor:
    bmin = b['minor']['value']
    # Position angle:
    bpa = b['positionangle']['value']
    
    print("BMAJ x BMIN [BPA] = ", np.round(bmaj,4), np.round(bmin,4), np.round(bpa,4))

    
    
    
# Close the open image:
ia.close()
