
import math

def gross_section_yielding(fy:float,Ag:float)->float:
    """
    """
    gamma_m0=1.1
    T_dg=(fy/gamma_m0)*Ag*10**-3
    return round(T_dg,2)

def net_section_rupture_plates(fu:float,Anet:float)->float:
    """
    """
    gamma_m1=1.25
    T_dn=(0.9*fu/gamma_m1)*Anet*10**-3
    return round(T_dn,2)

def net_section_rupture_angles_channels(w:float,t:float,fu:float,fy:float,Ago:float,Anc:float,bs:float,Lc:float)->float:
    """
    """
    gamma_m0=1.1
    gamma_m1=1.25
    beta=1.4-(0.076*(w/t)*(fy/fu)*(bs/Lc))
    T_dn=(((beta*fy/gamma_m0)*Ago)+((0.9*fu/gamma_m1)*Anc))*10**-3
    return round(T_dn,2)

def block_shear_failure(fu:float,fy:float,Avg:float,Atn:float,Avn:float,Atg:float)->float:
    """
    """
    gamma_m0=1.1
    gamma_m1=1.25
    T_db1 = ((fy * Avg) / (math.sqrt(3) * gamma_m0)+ (0.9 * fu * Atn) / gamma_m1) * 10**-3
    T_db2 = ((0.9 * fu * Avn) / (math.sqrt(3) * gamma_m1)+ (fy * Atg) / gamma_m0) * 10**-3
    T_db= min(T_db1,T_db2)
    return round(T_db,2)

def design_tensile_strength(fy:float,Ag:float,fu:float,Anet:float,Avg:float,Atn:float,Avn:float,Atg:float)->float:
    """
    Returns the design tensile strength of the member
    """
    T_dg=gross_section_yielding(fy,Ag)
    T_dn=net_section_rupture_plates(fu,Anet)
    T_db=block_shear_failure(fu,fy,Avg,Atn,Avn,Atg)
    T_d=min(T_dg,T_dn,T_db)
    return round(T_d,2)