#investigating the completeness prior from this paper.
#assume identical transit depth signals and a population of reported stars with identical means and standard deviations (i.e. 500 stars with R=1 and R_std=0.1, gaussian error).

import numpy as np
import matplotlib.pyplot as plt

N = 1000
std = 0.25
K = 2       #F = K*(r_p/r_*)^2

Rs = np.random.normal(1,std,N)
Rp = Rs*K           #Rp = Rs*K*sqrt(Flux) = Rs*K
Occ = np.zeros(N)   #occurrence
C = np.zeros(N)     #completeness

for i in range(N):
    SNR = (Rp[i]/Rs)**2
    C[i] = len(SNR[SNR > 1])/float(N)
    Occ[i] = 1/C[i]

#This plot shows how the prior for Silburt et al. (2015) is motivated. A-priori, if you have a set of stars with large error bars, the prior likelihood (or prior probability) that a given transit depth corresponds to a small planet is low, since it would (on average) not be detectable in context of the larger popualation.
plt.plot(Rp, C, '.')
plt.xlabel('planet radius')
plt.ylabel('Completeness in sample')
plt.show()
