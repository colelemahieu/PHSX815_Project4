# Cole Le Mahieu Project 4 - analyze.py

# import packages
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm
from math import *
from fractions import Fraction
from Random import Random

# instantiate random class
random = Random()

# get file input
p = sys.argv.index("-input")

# initialize number of experiments
nexp = 0

# count the number of experiments, file0
with open(sys.argv[p+1], "r") as file0:
    for line in file0:
        nexp +=1

# get the file data, file0
with open(sys.argv[p+1], "r") as file0:
    filestring = file0.read()
    filelist = filestring.split(" ")

# get rid of the \n symbols
filelist_b = []
for x in filelist:
    filelist_b.append(x.strip())

# delete empty spaces in the list
filelist_clean = [x for x in filelist_b if x]

# calculate number of rolls per experiment
decays = len(filelist_clean)/nexp

# get arrays of float dice rolls
data = []
for i in range(0, len(filelist_clean)):
    data.append(float(filelist_clean[i]))

# make an array divided into subarrays for each experiment
array = np.array(data)
data_arr = np.reshape(array, (-1, decays))

# loop through the experiments and count the decay modes
digamma = []
bb_decays = []
w_decays = []
gg_decays = []
mu_decays = []
tau_decays = []
cc_decays = []
zz_decays = []
zg_decays = []

for i in range(0, nexp):
    mumu = 0
    zgamma = 0
    gamgam = 0
    zz = 0
    cc = 0
    tautau = 0
    gg = 0
    ww =0
    bb = 0
    
    for j in range(0, decays):
        if (data_arr[i][j]==9):
            bb = bb + 1
        elif (data_arr[i][j]==8):
            ww = ww + 1
        elif (data_arr[i][j]==7):
            gg = gg + 1
        elif (data_arr[i][j]==6):
            tautau = tautau + 1
        elif (data_arr[i][j]==5):
            cc = cc + 1
        elif (data_arr[i][j]==4):
            zz = zz + 1
        elif (data_arr[i][j]==3):
            gamgam = gamgam + 1
        elif (data_arr[i][j]==2):
            zgamma = zgamma + 1
        else:
            mumu = mumu + 1

    # calculate the measured branching ratios and put them into arrays
    c_mumu = float(mumu) / decays
    c_zgamma = float(zgamma) / decays
    c_gamgam = float(gamgam) / decays
    c_zz = float(zz) / decays
    c_cc = float(cc) / decays
    c_tautau = float(tautau*(random.box_muller(0.78,0.27))) / decays  # observed tau tau cross section .78 +- 0.27 the SM expectation
    c_gg = float(gg) / decays
    c_ww = (float(ww)*0.97) / decays   # .97 for signal trigger efficiency
    c_bb = float(random.box_muller(bb, 0.15*bb)) / decays   # systematic uncertainties
    digamma.append(c_gamgam)
    w_decays.append(c_ww)
    bb_decays.append(c_bb)
    gg_decays.append(c_gg)
    tau_decays.append(c_tautau)
    cc_decays.append(c_cc)
    zz_decays.append(c_zz)
    zg_decays.append(c_zgamma)
    mu_decays.append(c_mumu)
    

# match a fit to the measurements of the same values
(mu, sigma) = norm.fit(w_decays)
(mu2, sigma2) = norm.fit(digamma)
(mu3, sigma3) = norm.fit(bb_decays)
(mu4, sigma4) = norm.fit(gg_decays)
(mu5, sigma5) = norm.fit(tau_decays)
(mu6, sigma6) = norm.fit(cc_decays)
(mu7, sigma7) = norm.fit(zz_decays)
(mu8, sigma8) = norm.fit(c_zgamma)
(mu9, sigma9) = norm.fit(c_mumu)

# plotting stuff
plt.figure()
n, bins, patches = plt.hist(w_decays, normed=1)
y = mlab.normpdf(bins, mu, sigma)
l = plt.plot(bins, y, "r", linewidth=2)
leftA, rightA = plt.xlim()
bottomA, topA = plt.ylim()
plt.text(leftA+.575*(rightA-leftA), .9*topA, "$\\mu$ = %.3f" %(mu), fontweight="bold")
plt.text(leftA+.575*(rightA-leftA), .85*topA, "$\\sigma$ = %.3f" %(sigma), fontweight="bold")
plt.text(leftA+.575*(rightA-leftA), .75*topA, "Exp Number = %i" %(nexp), fontweight="bold")
plt.text(leftA+.575*(rightA-leftA), .80*topA, "Decays per exp = %i" %(decays), fontweight="bold")
plt.title("$H \\rightarrow W^{+}W^{-}$")
plt.ylabel("Relative Frequency")
plt.xlabel("Branching Ratio Measurements")

plt.figure()
n2, bins2, patches2 = plt.hist(digamma, normed=1)
y2 = mlab.normpdf(bins2, mu2, sigma2)
l2 = plt.plot(bins2, y2, "r", linewidth=2)
leftB, rightB = plt.xlim()
bottomB, topB = plt.ylim()
plt.text(leftB+.575*(rightB-leftB), .9*topB, "$\\mu$ = %.3f" %(mu2), fontweight="bold")
plt.text(leftB+.575*(rightB-leftB), .85*topB, "$\\sigma$ = %.5f" %(sigma2), fontweight="bold")
plt.text(leftB+.575*(rightB-leftB), .75*topB, "Exp Number = %i" %(nexp), fontweight="bold")
plt.text(leftB+.575*(rightB-leftB), .80*topB, "Decays per exp = %i" %(decays), fontweight="bold")
plt.title("$H \\rightarrow \\gamma \\gamma$")
plt.ylabel("Relative Frequency")
plt.xlabel("Branching Ratio Measurements")

plt.show()

# print the measured decay modes
print("Results from %i decays per experiment over %i experiments" %(decays, nexp))
print("mu-mu Channel BR + %.5f +- %.8f" %(mu9, sigma9))
print("zg Channel BR = %.5f +- %.8f" %(mu8, sigma8))
print("Photon-Photon Channel BR = %.5f +- %.5f" %(mu2, sigma2))
print("zz Channel BR = %.3f +- %.3f" %(mu7, sigma7))
print("cc Channel BR = %.3f +- %.3f" %(mu6, sigma6))
print("tau-tau Channel BR = %.3f +- %.3f" %(mu5, sigma5))
print("gg Channel BR = %.3f +- %.3f" %(mu4, sigma4))
print("WW Channel BR = %.3f +- %.3f" %(mu,sigma))
print("bb Channel BR = %.3f +- %.3f" %(mu3, sigma3))
    

