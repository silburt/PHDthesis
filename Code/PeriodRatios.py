#This makes the period distribution for the Kepler data, similar to Goldreich & Schlichting (2014)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#51 columns
header = ['name', 'letter', 'method', 'Npl', 'P', 'Pup', 'Pdown', 'Plim', 'a', 'aup', 'adown', 'alim', 'e', 'eup', 'edown', 'elim', 'i', 'iup', 'idown', 'ilim', 'm', 'mup', 'mdown', 'mlim', 'mprov', 'r', 'rup', 'rdown', 'rlim','rho', 'rhoup', 'rhodown', 'rholim', 'TTVflag', 'Keplerfield', 'K2field', 'Ms', 'Msup', 'Msdown', 'Mslim','Msblend', 'Rs', 'Rsup', 'Rsdown', 'Rslim', 'Rsblend','Date','RpE','RpEup','RpEdown','RpElim']
#usecols = [1,2,3,4,5,6,7,9,10,11,13,14,15,21,22,23,26,27,28,31,37,42,48]
data = pd.read_csv("planets.csv",names=header, delimiter=',',skiprows=59)
data = data[data['method']=='Transit']

systems = np.unique(data['name'])

Pratios = np.empty(0)
for n in systems:
    index = data['name']==n
    Parr = np.sort(data.loc[index,'P'].values)
    Pratio = Parr[1:]/Parr[0:-1]
    if np.all(np.isnan(Pratio)) == False:
        Pratios = np.append(Pratios, Pratio)

Pratios = np.sort(Pratios[Pratios < 4])

cdf = 0

if cdf == 1:    #cdf
    n = float(len(Pratios))
    cdf = np.arange(len(Pratios))/n
    plt.plot(Pratios, cdf)
    max = max(cdf)
    plt.ylabel('Noramlized Cumulative Distribution')
else:           #histogram
    n, bins, patches = plt.hist(Pratios, 60, normed=1, facecolor='green', alpha=0.75)
    max = max(n)
    plt.ylabel('Normalized Counts')

mmr = [2, 3./2., 4./3., 3, 5./3.]
mmr_names = ['2:1','3:2','4:3','3:1','5:3']
for i in range(len(mmr)):
    m,n = mmr[i],mmr_names[i]
    plt.plot([m,m], [0,1.11*max], 'k--')
    plt.text(m+0.01, 1.05*max, n, size=10)

plt.ylim([0,1.1*max])
plt.xlabel('Period Ratios')
plt.savefig('PeriodRatios.pdf')

