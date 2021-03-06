#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astroemperor
import scipy as sp

'''
# SETUP
# files to read, format is NAME_instrument#_instrumentname.format
# They must be in the datafiles folder
stardat = sp.array(['GJ876_1_LICK.vels', 'GJ876_2_KECK.vels'])

# we set the chain parameters
setup = sp.array([2, 50, 100])  # temperatures, walkers, steps

# Constrains for the signals (k>0), they use the change of variable so don't try to make much of them!
# The format is sp.array([As_0, As_1, log(Period0), log(Period1), Ac_0, Ac_1, S_0, S_1, C_0, S_1]),
# each file is a signal! Any value set as -sp.inf gets the automatic constrain
# made by astroemperor.
# A really short test chain verify everything is working OK, so we input some boundaries
# arround the actual values we got with a longer chain.

BOUNDARY = sp.array([[4.11098843e+00, 4.11105404e+00, -1.01515928e+01, -6.33312469e+00, 1.00520806e+01,   1.35949748e+01, -1.24823254e-02,   2.27443388e-02,   4.14811179e-02, 1.38568310e-01],
                     [3.40831451e+00, 3.40863545e+00, -5.69294095e+00, 6.05896817e-02, -9.33328013e+00, -8.07370401e+00,  -2.48303912e-01,  -7.10641857e-02, 3.47811764e-02,   1.79877743e-01]])

# We initialize the code
em = astroemperor.EMPIRE(stardat, setup)  # EMPIRE(data_to_read, chain_parameters)

# We configure the settings
em.CORNER = False  # corner plot disabled as it takes some time to plot
em.betas = None #array([1.0])  # beta factor for each temperature, None for automatic
em.MOAV = 0
# em.MUSIC= True
# we actually run the chain from 0 to 2 signals
em.RAW = True
em.conquer(0, 2, BOUND=BOUNDARY)

print('Everything is working fine !! Why dont you try running a longer chain without boundaries? See bottom comments!!')

# A1, P1, ecc1 206.1, 61.0, 0.007
# A2, P2, ecc2 86.5, 30.2, 0.03


'''
# For a more real test, we will do em.conquer(0, 2), without the boundaries!!
# BOUND=BOUNDARY by default is an empty array!!: sp.array([])
# And it's equivalent to:
# sp.array([[-sp.inf, -sp.inf, -sp.inf, -sp.inf, -sp.inf, -sp.inf, -sp.inf, -sp.inf, -sp.inf, -sp.inf],
#            -sp.inf, -sp.inf, -sp.inf, -sp.inf, -sp.inf, -sp.inf, -sp.inf, -sp.inf, -sp.inf, -sp.inf])
# up to how many files you want!


#rvfiles = sp.array(['TOI193.vels', 'TOI193_terra_o25.vels'])  # same data
#rvfiles = sp.array(['TOI193.vels'])  # same data
#rvfiles = sp.array(['GJ876_1_LICK.vels', 'GJ876_2_KECK.vels'])  # same data

rvfiles = sp.array(['GJ357_1_HARPS3.dat',
                    'GJ357_2_UVES3.dat',
                    'GJ357_3_KECK3.vels'])
#pmfiles = sp.array(['shitbin1000.flux'])

setup = sp.array([5, 120, 15000])  # ntemps, nwalkers, nsteps, now real

#stardat = sp.array([rvfiles, pmfiles])
stardat = rvfiles

#stardat = sp.array(['GJ876_1_LICK.vels', 'GJ876_2_KECK.vels'])


em = astroemperor.EMPIRE(stardat, setup)  # EMPIRE(data_to_read, chain_parameters)
em.betas = sp.array([1., 0.577, 0.333, 0.192, 0.111])
#em.PACC = True
#em.STARMASS = 1.00  # known mass for this particular star GJ876
#em.HILL = True
em.CORNER = False  # corner plot disabled
em.eccprior = 0.1  # sigma for the eccentricity prior!
em.jittprior = 5.0  # sigma for the jitter prior
em.jittmean = 5.0
em.MOAV = 1  # Moving Average Order, works from 0 to the number of datapoints
#em.MOAV_pm = 1
#em.MUSIC= True  # Music ON, False for OFF
em.RAW = False
#em.PLOT = False
em.conquer(0, 5)
#'''

#
