import numpy as np
import scipy.stats as sp
import pandas as pd
import matplotlib.pyplot as plt

#Created by Michael Silverstein
#msilvers@broadinstitute.org

#Inspired by:
#http://www.nature.com/nmeth/journal/v14/n1/full/nmeth.4120.html

def fig1():
    #Figure 1: P values are random variables.
    #Compare distribution of pvalues for one test and the minimum pvalue from 10 test
    fig,axs = plt.subplots(ncols=2) #Two column subplot
    """
    (a)
    Simulated P values from 1,000 statistical tests when H0 is true.
    The distribution is uniform and, on average, 5% of P < 0.05 (blue).
    """
    #Samples from 1000 tests
    uniform = np.random.random(1000)

    #Plot
    axs[0].hist(uniform[uniform>0.05],bins=23,facecolor='black')
    axs[0].hist(uniform[uniform<=0.05],bins=2,facecolor='steelblue')
    axs[0].set_title('Distribution of P values when null is true')

    """
    (b)
    The distribution of the minimum P value across 1,000 simulations of 10 tests when H0 is true.
    """
    #Perform random tests and keep minimum from each
    multitest = np.array([min(np.random.random(10)) for _ in range(1000)])

    #Plot
    axs[1].hist(multitest[multitest>0.05],bins=23,facecolor='black')
    axs[1].hist(multitest[multitest<=0.05],bins=2,facecolor='steelblue')
    axs[1].set_title('Distribution of minimum P value for 10 tests when null is true')
    plt.show()
    # plt.savefig('ReconFigure1.png')

def fig2():
    #Figure 2: Merely reporting 95% confidence intervals does not address selection bias.
    #Useful background: https://en.wikipedia.org/wiki/Confidence_interval

    fig,axs = plt.subplots(ncols=2)

    """
    (a)
    95% confidence intervals for 100 one-sample t-tests with samples of size n = 100,
    mean zero and s.d. = 1. Intervals are vertically sorted in increasing order of statistical
    significance.
    """
    samples = np.random.normal(size=(100,100)) #Generate 100 tests each of sample size 100
    means = np.mean(samples,axis=1) #Find average of each test
    stds = np.std(samples,axis=1) #Find standard deviation for each test

    #Confidence interval
    #CI = (x - z * s/sqrt(n), x + z * s/sqrt(n)), for z = 1.96 for 95% confidence interval
    CIs = means-1.96*stds/np.sqrt(100),means+1.96*stds/np.sqrt(100) #Two lists of each end point
    CIs = [[CIs[0][x],CIs[1][x]] for x in range(len(means))] #Reorganize to pairwise

    #Calculate pvalue of each sample
    ps = [sp.ttest_1samp(s,0)[1] for s in samples]

    #Combine all data
    data = np.array([np.append(CIs[x],1-ps[x]) for x in range(len(ps))]) #1-p value for most significant to be highest

    #Plot
    for d in data: #For each CI
        p = d[2] #1-P value
        x,y= (d[0],d[1]),(p,p) #CI at height of 1-p
        if p < 0.95:
            axs[0].plot(np.mean(x), p, 'o', color='black') #Draw midpoint of CI
            axs[0].plot(x,y,color='black') #Draw CI
        else:
            axs[0].plot(np.mean(x), p, 'o', color='steelblue') #Draw midpoint of CI
            axs[0].plot(x,y,color='steelblue') #Draw CI

    axs[0].axvline(0,color='black') #Vertical at 0
    axs[0].axhline(0.95,ls=':',color='black') #Horizontal at 0.95 (alpha = 0.05)
    axs[0].set_title('95% CI when null is true')
    axs[0].set_ylim(0,1.05)

    """
    (b)
    100 instances of the 95% confidence interval corresponding to the most significant result from a
    set of 10 one-sample t-tests of the kind performed in a.
    """
    samples = np.random.normal(size=(100,100,10))







    plt.show()
    # plt.savefig('ReconFigure2.png')
