import numpy as np
import scipy.stats.ttest_1samp
import matplotlib.pyplot as plt

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
    uniform = np.random.random(1000)
    axs[0].hist(uniform[uniform>0.05],bins=23,facecolor='black')
    axs[0].hist(uniform[uniform<=0.05],bins=2,facecolor='steelblue')
    axs[0].set_title('Distribution of P values when null is true')

    """
    (b)
    The distribution of the minimum P value across 1,000 simulations of 10 tests when H0 is true.
    """
    multitest = np.array([min(np.random.random(10)) for _ in range(1000)])
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
    stds = np.std(samples,axis=1)

    #Confidence interval
    #CI = (x - z * s/sqrt(n), x + z * s/sqrt(n)), for z = 1.96 for 95% confidence interval
    CI = means-1.96*stds/np.sqrt(100),means+1.96*stds/np.sqrt(100) #Two lists of each end point
    CI = [[CI[0][x],CI[1][x]] for x in range(len(means))] #Reorganize to pairwise

    #Calculate pvalue of each sample


