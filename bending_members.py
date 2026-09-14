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

def bending_strengh_laterally_unsupported(section:str,Ze:float,Zp:float,fy:float,gamma_m0:float,lambda_LT: float)->float:
    """
    Returns the design bending strength for a laterally supported beam
    alpha_LT = 0.21 for rolled steel section
    """
    alpha_LT=0.21
    if section=='plastic' or section=='compact':
        beta=1
    elif section=='semi-compact':
        beta=Ze/Zp
    else:
        raise ValueError ("Section should be plastic or compact or semi compact")

    phi_LT = 0.5 * (1+ alpha_LT *(lambda_LT - 0.2)+ lambda_LT**2)

    chi_LT = 1 / (phi_LT+ (phi_LT**2- lambda_LT**2)**0.5)

    fbd = chi_LT * fy / gamma_m0

    Md = beta * Zp * fbd
 
    return round(Md * 1e-6, 2)



def design_shear_strength(h:float,tw:float,fy:float,gamma_mo:float)->float:
    """
    Returns the design shear strength
    """
    Av=h*tw
    Vd=(Av*fy)/(math.sqrt(3)*gamma_mo)*10**-3
    return round(Vd,2)

def flange_plastic_moment(h: float,bf: float,tf: float,fy: float, gamma_m0: float) -> float:
    """
    Returns the plastic moment of flange
    """
    Zpf = bf * tf * (h - tf)

    Mfd = (Zpf * fy) / gamma_m0

    return round(Mfd * 1e-6, 2)

def reduced_bending_strength(Vu: float,Vd: float,Md: float,Mfd: float) -> float:
    """
    Returns the reduced bending strength for high shear
    """

    if Vu <= 0.6 * Vd:
        return Md
    else:
        beta = ((2 * Vu / Vd) - 1) ** 2
    
        Mdv = Md - beta * (Md - Mfd)
    
        return round(Mdv, 2)

def deflection_check(actual_deflection: float,span: float,limit_ratio: float) -> bool:

    allowable_deflection = span / limit_ratio

    return actual_deflection <= allowable_deflection