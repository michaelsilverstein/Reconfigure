import numpy as np
import matplotlib.pyplot as plt

#http://www.nature.com/nmeth/journal/v14/n1/full/nmeth.4120.html

def fig1():
    #Figure 1: P values are random variables.
    #Compare distribution of pvalues for one test and the minimum pvalue from 10 test

    fig,axs = plt.subplots(ncols=2) #Two column subplot
    """
    a)
    Simulated P values from 1,000 statistical tests when H0 is true.
    The distribution is uniform and, on average, 5% of P < 0.05 (blue).
    """
    uniform = np.random.random(1000)
    axs[0].hist(uniform[uniform>0.05],bins=23,facecolor='black')
    axs[0].hist(uniform[uniform<=0.05],bins=2,facecolor='steelblue')
    axs[0].set_title('Distribution of P values when null is true')

    """
    b)
    The distribution of the minimum P value across 1,000 simulations of 10 tests when H0 is true.
    """
    multitest = np.array([min(np.random.random(10)) for _ in range(1000)])
    axs[1].hist(multitest[multitest>0.05],bins=23,facecolor='black')
    axs[1].hist(multitest[multitest<=0.05],bins=2,facecolor='steelblue')
    axs[1].set_title('Distribution of minimum P value for 10 tests when null is true')
    plt.show()
    # plt.savefig('ReconFigure1.png')
