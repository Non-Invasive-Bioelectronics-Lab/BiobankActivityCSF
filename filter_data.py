#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:34:09 2019

@author: mchi2cb3
"""

from scipy.signal import butter, filtfilt, lfilter
import numpy as np

def filter_coefficients(cutoff, fs, order):
    nyq = 0.5 * fs                                                              # Get nyquist frequency of signal
    normal_cutoff = cutoff / nyq                                                # Find the normalised cut-off frequency
    b, a = butter(order, normal_cutoff, btype='highpass', analog=False)         # Generate array of filter co-efficients
    return b, a

# Filter data using filtfilt command
def data_filter(data, cutoff=0.1, fs=100, order=3):
    b, a = filter_coefficients(cutoff, fs, order)                               # Call function to generate filter co-efficients
    signal_filtered = np.zeros([len(data), 3])
    for i in range(3):
        signal_filtered[:,i] = filtfilt(b, a, data[:,i])
    return signal_filtered