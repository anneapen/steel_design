import math

def edge_distance (do:float,t:float,fy:float)->tuple[float,float]:
    """
    Returns the maximum and minimum edge/end distance
    """
    emin=1.5*do
    eps=(250/fy)**(1/2)
    emax=12*t*eps

    return emin,emax

def class_of_bolt(grade:float)->tuple[float,float]:
    """
    Returns ultimate strength of the bolt,fub and yield strength,fyb for the given grade of bolt
    """
    fub=int(grade)*100
    dec=grade-int(grade)
    fyb=dec*fub
    return fub,round(fyb,1)

def net_area_of_bolt(d:float):
    """
    Returns the net area of the bolt,Anb(mm2)
    where d- diameter of the bolt,mm 
    """
    Asb=math.pi/4*(d**2)
    Anb=0.78*Asb

    return round(Anb,2)