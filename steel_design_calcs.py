def edge_distance (do:float,t:float,fy:float)->tuple[float,float]:
    """
    Returns the maximum and minimum edge/end distance
    """
    emin=1.5*do
    eps=(250/fy)**(1/2)
    emax=12*t*eps

    return emin,emax