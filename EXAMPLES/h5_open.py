#!/usr/bin/env python
#
import h5py

H5_FILE = '../DATA/h5/hdf5_test.h5'

with h5py.File(H5_FILE) as hfile:  # <1>
    pass
