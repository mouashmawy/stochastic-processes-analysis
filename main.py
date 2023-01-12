from Ensembles import Ensembles
from Stats import Stats
from DEF import *
def main():
    ens = Ensembles()
    ensemble,time = ens.getEnsemble(X_)
    Statistics = Stats(ensemble,time)
    #print(Statistics.calcACFbetween(0,0))
    print(len(Statistics.plotPSD()))
    
    
if __name__ == "__main__":
    main()