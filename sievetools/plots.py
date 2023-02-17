import matplotlib.pyplot as plt

def plot_sieve(all_nmax, all_proportions, log_scale = True):
    """
    make plots  of the proportion of prime numbers
    all_nmax (list)= list of nmax
    all_proprotions (list)= list of proportions
    log_scale (boolean)
    
    """
    plt.plot(all_nmax, all_proportions)
    plt.xlabel("N")
    plt.ylabel("Proportion of primer numbers")
    
    if log_scale == True:
        plt.xscale("log")
        plt.yscale("log")
    