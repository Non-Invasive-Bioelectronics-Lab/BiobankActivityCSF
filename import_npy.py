#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 13:28:47 2019

@author: mchi2cb3
"""

import numpy as np

def import_npy(file):
    data_object = np.load(file[:-4]+'.npy')
    time = data_object['time']
    data = np.zeros([len(data_object), 3])
    data[:,0] = data_object['x']
    data[:,1] = data_object['y']
    data[:,2] = data_object['z']
    return data, time