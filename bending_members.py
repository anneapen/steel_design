import math
import sections as sections


def bending_strengh_laterally_supported(section:str,Ze:float,Zp:float,fy:float,gamma_m0:float)->float:
    """
    Returns the design bending strength for a laterally supported beam
    """
    if section=='plastic' or section=='compact':
        beta=1
    elif section=='semi-compact':
        beta=Ze/Zp
    else:
        raise ValueError ("Section should be plastic or compact or semi compact")

    Md=beta*Zp*fy/gamma_m0
    Md_limit=(1.2*Ze*fy)//gamma_m0
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



def design_shear_strength(h:float,tw:float,fy:float,gamma_m0:float)->float:
    """
    Returns the design shear strength
    """
    Av=h*tw
    Vd=(Av*fy)/(math.sqrt(3)*gamma_m0)*10**-3
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

def design_beam(beam:str,W:float,fy:float,Mu:float,Vu:float,laterally_supported: bool,
               actual_deflection:float,span:float,limit_ratio:float,lambda_LT:float|None=None):
    """
    Returns whether the designed beam is safe or not
    """
    section=sections.rolled_steel_beam(beam,W)
    h=section[1]
    bf=section[2]
    tf=section[3]
    tw=section[4]
    
    section_class=sections.section_classification(bf,tf,tw,h,fy)
    Ze,Zp=sections.section_modulus(beam,W)
    gamma_m0=1.1
    
    if laterally_supported:
        Md=bending_strengh_laterally_supported(section_class,Ze,Zp,fy,gamma_m0)
    else:
        if lambda_LT is None:
            raise ValueError("lambda_LT must be provided for a laterally unsupported beam")
        Md=bending_strengh_laterally_unsupported(section_class,Ze,Zp,fy,gamma_m0,lambda_LT)
        
    #Shear strength
    Vd=design_shear_strength(h,tw,fy,gamma_m0)
    
    if Vu > Vd:
        print("Revise the section")
        return False

    #Check for high shear
    if Vu>0.6*Vd:
        Mfd=flange_plastic_moment(h,bf,tf,fy,gamma_m0)
        Md=reduced_bending_strength(Vu,Vd,Md,Mfd)

    #Deflection check
    def_check=deflection_check(actual_deflection,span,limit_ratio)

    if Mu<=Md and def_check:
        print("Section is safe")
        return True
    else:
        print("Revise the section")
        return False
        