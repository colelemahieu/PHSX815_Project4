# Cole Le Mahieu Project 4 - decay.py

# import packages
from __future__ import print_function
import sys
import numpy as np
import matplotlib.pyplot as plt
from math import *
from fractions import Fraction
from Random import Random

# instantiate Random class
random = Random()

# default values for number of experiments and number of Higgs decays measured
Nexp = 12
Ndecays = 20

# user can input values for number of experiments and number of Higgs decays measured
if "-Nexp" in sys.argv:
    p = sys.argv.index("-Nexp")
    Ne = int(sys.argv[p+1])
    if Ne > 0:
        Nexp = Ne
if "-Ndecays" in sys.argv:
    p = sys.argv.index("-Ndecays")
    Nt = int(sys.argv[p+1])
    if Nt > 0:
        Ndecays = Nt

# output decays
for i in range(0,Nexp):

    # get the SM branching fractions from posterior distributions based on their uncertainty
    # the total fraction must add to one
    mumu = random.box_muller(0.00022, 0.00001)
    while (mumu>1 and mumu<0):
        mumu = random.box_muller(0.00022, 0.00001)

    Zgamma = random.box_muller(0.00155, 0.00014)
    while ((mumu+Zgamma)>1 and Zgamma<0):
        Zgamma = random.box_muller(0.00155, 0.00014)

    gamma = random.box_muller(0.00228, 0.00011)
    while ((mumu+Zgamma+gamma)>1 and gamma<0):
        gamma = random.box_muller(0.00228, 0.00011)

    zz = random.box_muller(.0267, 0.0011)
    while ((mumu+Zgamma+gamma+zz)>1 and zz<0):
        zz = random.box_muller(.0267, 0.0011)

    cc = random.box_muller(.0290, 0.0035)
    while ((mumu+Zgamma+gamma+zz+cc)>1 and cc<0):
        cc = random.box_muller(.0290, 0.0035)

    tautau = random.box_muller(.0630, 0.0036)
    while ((mumu+Zgamma+gamma+zz+cc+tautau)>1 and tautau<0):
        tautau = random.box_muller(.0630, 0.0036)

    gg = random.box_muller(.0856, 0.0086)
    while ((mumu+Zgamma+gamma+zz+cc+tautau+gg)>1 and gg<0):
        gg = random.box_muller(.0856, 0.0086)

    ww = random.box_muller(.216, 0.009)
    while ((mumu+Zgamma+gamma+zz+cc+tautau+gg+ww)>1 and ww<0):
        ww = random.box_muller(.216, 0.009)

    
    for i in range(0,Ndecays):
        print(random.HiggsDecay(mumu, Zgamma, gamma, zz, cc, tautau, gg, ww), end=" ")
    print(" ")
