from Ensembles import Ensembles
from Stats import Stats
from DEF import *
def main():
    ens = Ensembles()
    ensemble,time = ens.getEnsemble(X_)
    plot = Stats(ensemble,time)
    print(plot.calcACFbetween(9,69))
    
    
if __name__ == "__main__":
    main()