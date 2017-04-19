#This macro is for showing how Hybarid works - how it switches from global to mini. It *REQUIRES* one planet, one star, two planetesimals, one planetesimal having a close encounter

import glob
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cmx
import matplotlib.colors as colors
import sys
import re

def natural_key(string_):
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)]

names = ['planet 2', 'planetesimal 1', 'planetesimal 2']
ms = [7,7,7]
mew = [2,2,2]
points = ['v','D','o']
cmap = ['red','green','blue']

dirhybarid = 'CE_fig/'
filesh = glob.glob(dirhybarid+'*.txt')
filesh = sorted(filesh, key = natural_key)
N_files = len(filesh)

fh = open(filesh[0],'r')
t,id,xh,yh,zh,mini = np.loadtxt(fh, delimiter=',', unpack='True')
Nbods = len(xh)

dr = np.zeros((N_files,Nbods))
time = np.zeros(N_files)

for i in xrange(0,N_files):
    fh = open(filesh[i],'r')
    t,id,xh,yh,zh,mini = np.loadtxt(fh, delimiter=',', unpack='True')
    Nbods = len(xh)
    for j in xrange(2,Nbods):
        dx = xh[j] - xh[1]
        dy = yh[j] - yh[1]
        dz = zh[j] - zh[1]
        dr[i,j] = (dx*dx + dy*dy + dz*dz)**0.5
    time[i] = t[0]

for i in xrange(2,Nbods):
    for j in xrange(0,len(dr[:,i])):
        if dr[j,i] == 0:
            continue
        else:
            if j==0:
                plt.plot([time[j]],[dr[j,i]], points[i-2], color=cmap[i-2], markersize = ms[i-2], markeredgecolor=cmap[i-2], mew = mew[i-2], label=names[i-2],mfc='white')
            else:
                plt.plot([time[j]],[dr[j,i]], points[i-2], color=cmap[i-2], markersize = ms[i-2], markeredgecolor=cmap[i-2], mew = mew[i-2], mfc='white')
plt.axvspan(0.2, 0.75, alpha=0.5, color='grey',label='mini simulation active')
#plt.plot([0.2,0.2],[0.01,10],'--',color='black',linewidth = 3, label='close encounter boundaries')
#plt.plot([0.75,0.75],[0.01,10],'--',color='black',linewidth = 3)
#plt.plot(time, dr[:,0], 'o', markeredgecolor='none', color='black', label='Total Error')
plt.legend(loc='upper left',prop={'size':10}, numpoints=1, markerscale=1)
plt.ylabel('distance from planet 1 (AU)', fontsize=13)
plt.xlabel('time (years)', fontsize=13)
plt.yscale('log')
#plt.xlim([0.5,time[-1]])
plt.savefig('CE_fig.pdf')
plt.show()