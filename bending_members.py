import math

def bending_strengh_laterally_supported(section:str,Ze:float,Zp:float,fy:float,gamma_mo:float)->float:
    """
    Returns the design bending strength for a laterally supported beam
    """
    if section=='plastic' or section=='compact':
        beta=1
    elif section=='semi-compact':
        beta=Ze/Zp
    else:
        raise ValueError ("Section should be plastic or compact or semi compact")

    Md=beta*Zp*fy/gamma_mo
    Md_limit=(1.2*Ze*fy)//gamma_mo
    Md=min(Md,Md_limit)*10**-6
    
    return round(Md,2)

def design_shear_strength(Av:float,fy:float,gamma_mo:float)->float:
    """
    Returns the design shear strength
    """
    Vd=(Av*fy)/(math.sqrt(3)*gamma_mo)*10**-3
    return round(Vd,2)