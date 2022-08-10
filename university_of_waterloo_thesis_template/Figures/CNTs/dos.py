import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import pandas as pd
from scipy.interpolate import interp1d
from scipy.signal import savgol_filter
from scipy.ndimage.filters import uniform_filter1d
from matplotlib import image
import glob
import os

dat = np.loadtxt('dos.csv', delimiter=',')
dat = np.transpose(dat)
mapping = dat[0]
d = dat[1]*1e-1 #A to nm
energy = dat[2]
colors = colors.ListedColormap(['black', 'red'])

plt.scatter(d, energy, s=1, c=mapping, cmap=colors)
plt.xlabel('Nanotube Diameter (nm)')
plt.ylabel('Energy Gap (eV)')
plt.show()

dat = np.loadtxt('dos_76.txt')
dat = np.transpose(dat)
energy = dat[0]
dos = dat[1]

plt.plot(dos, energy, color='black')
plt.plot(dos, -energy, color='black')
plt.axhline(y=0, color='green')
plt.ylabel('Energy(eV)')
plt.xlabel('DOS')
plt.title('(7, 6)')
plt.show()

dat = np.loadtxt('dos_66.txt')
dat = np.transpose(dat)
energy = dat[0]
dos = dat[1]

plt.plot(dos, energy, color='black')
plt.plot(dos, -energy, color='black')
plt.axhline(y=0, color='green')
plt.ylabel('Energy(eV)')
plt.xlabel('DOS')
plt.title('(6, 6)')
plt.show()
