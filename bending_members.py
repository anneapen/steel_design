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
    return Md

def design_shear_strength(Av:float,fy:float,gamma_mo:float)->float:
    """
    Returns the design shear strength
    """
    Vd=(Av*fy)/(math.sqrt(3)*gamma_mo)
    return Vd