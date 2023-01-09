from Ensembles import Ensembles
from Stats import Stats
    
def main():
    ens = Ensembles()
    ensemble,time = ens.getEnsemble("y")
    plot = Stats(ensemble,time)
    plot.plotSampleN(50)
    
    
if __name__ == "__main__":
    main()