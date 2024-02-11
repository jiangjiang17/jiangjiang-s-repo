import h5py
import numpy as np
filenama="/home/s2499902/OOSE/week4/OOSA-code-public/week4/ILVIS1B_AQ2015_1014_R1605_070717.h5"
f=h5py.File(filenama, 'r')

list(f)
LAT0=np.array(f['LON0'])
Z0=np.array(f['Z0'])[0:100]
print(Z0.shape)