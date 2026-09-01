import math
import sections as sections

def effective_length_factor(condition: str) -> float:
    """
    Returns effective length factor K
    as per IS 800:2007 Table 11.
    """

    if condition == "fixed_fixed":
        K = 0.65

    elif condition == "fixed_pinned":
        K = 0.80

    elif condition == "pinned_pinned":
        K = 1.00

    elif condition == "fixed_guided":
        K = 1.20

    elif condition == "fixed_free":
        K = 2.00

    else:
        raise ValueError("Invalid end restraint condition")

    return K

def design_compressive_strength(beam:str,W:float,L:float,fy:float,psf:float,condition:str)->float:
    """
    Returns the design compressive strength of the member as per Cl.7.1 of IS 800:2007
    where, beam=the beam section
            W=weight of the beam
            L=length of the beam
            fy=yield stress,MPa
            psf=partial safety factor
            condition=support condition of the beam
    """
    section=sections.rolled_steel_beam(beam,W)
    Area=section[0]
    rzz,ryy=section[4],section[5]
    buckling_class=sections.buckling_class(beam,W)
    rmin=min(rzz,ryy)*10
    K=effective_length_factor(condition)
    E=2*10**5
    
    fcc=(math.pi**2*E)/(((K*L*1000)/rmin)**2)
    lamda=math.sqrt(fy/fcc)
    buckling_class=sections.buckling_class(beam,W)
    alpha=sections.imperfection_factor(buckling_class)
    phi=0.5*(1+(alpha*(lamda-0.2))+(lamda**2))
    fcd=(fy/psf)/(phi+math.sqrt((phi**2)-(lamda**2)))
    Pcd=fcd*Area*100*10**-3

    return round(Pcd,2)

