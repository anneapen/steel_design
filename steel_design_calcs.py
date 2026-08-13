import math
import pandas as pd


def class_of_bolt(grade:float)->tuple[float,float]:
    """
    Returns ultimate strength of the bolt,fub and yield strength,fyb for the given grade of bolt
    """
    fub=int(grade)*100
    dec=grade-int(grade)
    fyb=dec*fub
    return fub,round(fyb,1)

def net_area_of_bolt(d:float)->float:
    """
    Returns the net area of the bolt,Anb(mm2)
    where d- diameter of the bolt,mm 
    """
    Asb=math.pi/4*(d**2)
    Anb=0.78*Asb

    return round(Anb,2),round(Asb,2)

def hole_diameter(d:float)->float:
    """
    IS 800:2007 (Clause 10.2.1), the diameter of a standard bolt hole (d₀) is larger than the nominal diameter of the bolt (d) 
    to allow easy insertion and account for minor misalignments. For standard clearance holes, the extra clearance added to the bolt 
    diameter depends on the bolt size: 1.0 mm extra for 12 to 14 mm bolts, 2.0 mm extra for 16 to 24 mm bolts, and 3.0 mm extra for bolts 
    larger than 24 mm.
    """
    if d>12 and d<14:
        do=d+1
    elif d>16 and d<24:
        do=d+2
    elif d>24:
        do=d+3

    return do

def edge_distance (d:float,t:float,fy:float)->tuple[float,float]:
    """
    Returns the maximum and minimum edge/end distance
    """
    do=hole_diameter(d)
    emin=1.5*do
    eps=(250/fy)**(1/2)
    emax=12*t*eps

    return emin,emax

def pitch(d:float,t:float,type:str)->tuple[float,float]:
    """
    Returns the minimum pitch,p_min,mm & maximum pitch,p_max,mm
    d-diameter of the bolt,mm
    t-thickness of the thinner plate,mm
    type-type of member(tension/compression)

    IS 800:2007 (Clause 10.2.2), The distance between centre of fasteners shall not be
    less than 2.5 times the nominal diameter of the fastener.
    """
    p_min=2.5*d
    if (type=='compression'):
        p_max=min(12*t,200)
    elif (type=='tension'):
        p_max=min(16*t,200)
    return p_min,p_max

def tensile_strength_of_bolt(grade:float,d:float)->float:
    """
    returns the tensile strength of the bolt
    """
    fub=class_of_bolt(grade)[0]
    Anb=net_area_of_bolt(d)[0]
    T_db=(0.9*fub*Anb)/1.25*10**-3
    return round(T_db,2)

def bearing_strength_of_bolt(d:float,fu:float,grade:float,tmin:float)->float:
    """
    returns the bearing strength of the bolt
    """
    e=edge_distance(d,tmin,fu)[0]
    p=pitch(d,tmin,'compression')[0]
    do=hole_diameter(d)
    fub=class_of_bolt(grade)[0]
    kb=min((e/(3*do)),((p/(3*do))-0.25),(fu/fub),1)
    V_dpb=(2.5*kb*fu*(d*tmin))/1.25*10**-3
    return round(V_dpb,2)

def shear_strength_of_bolt(grade:float,d:float,nn:int,ns:int,lj:float,lg:float,tpk:float)->float:
    """
    returns the shear strength of the bolt
    """
    fub=class_of_bolt(grade)[0]
    Anb,Asb=net_area_of_bolt(d)
    if lj>(15*d):
     rf_lj=1.075-(lj/(200*d))
     rf_lj = max(0.75, min(rf_lj, 1.0))
    else:
     rf_lj=1
    if lg>(5*d):
     rf_lg=(8*d)/(lg+(3*d))
     rf_lg = min(rf_lg, rf_lj)
    else:
     rf_lg=1
    if tpk>6:
     rf_pk=1-(0.0125*tpk)
    else:
     rf_pk=1
    V_dsb=(fub/(math.sqrt(3)*1.25))*((nn*Anb)+(ns*Asb))*rf_lg*rf_lj*rf_pk*10**-3
    return round(V_dsb,2)

def design_strength_of_butt_weld(lw:float,tmin:float,fy:float,fu:float,weld_type:str,weld_penetration:str)->tuple[float,float]:
   """
   returns the design strength of weld
   """
   if (weld_penetration=='single'):
    te=(5/8)*tmin
    f=fu
   elif (weld_penetration=='double'):
    te=tmin
    f=fy
   if (weld_type=='shop weld'):
      psf=1.25
   elif (weld_type=='field weld'):
      psf=1.5

   T_dw=(f/psf)*(lw*te)*10**-3
   V_dw=0.57*(f/psf)*(lw*te)*10**-3

   return round(T_dw,2),round(V_dw,2)

def angle_of_fusion(theta:float)->float:
    """
    """
    if 60<theta<90:
        K=0.7
    elif 91<theta<100:
        K=0.65
    elif 101<theta<106:
        K=0.6
    elif 107<theta<113:
        K=0.55
    elif 114<theta<120:
        K=0.5
    else:
        K=0.7
    return K

def design_strength_of_fillet_weld(s:float,lw:float,weld_type:str,fu:float,theta:float)->tuple[float,float]:
    """
    returns the design strength of weld
    """
    
    K=angle_of_fusion(theta)
    tt=K*s
    if (weld_type=='shop weld'):
          psf=1.25
    elif (weld_type=='field weld'):
          psf=1.5
    T_dw=(fu/psf)*(lw*tt)*10**-3
    V_dw=(fu/(math.sqrt(3)*psf))*(lw*tt)*10**-3
    return round(T_dw,2),round(V_dw,2)


def rolled_steel_beam(beam:str,W:float)->tuple[float,float,float,float,float,str]:
    """
    """
    df=pd.read_csv('steel_tables_is.csv')
    df=df.set_index('Section')
    rolled_steel_beam=df.copy()
    condition = ((rolled_steel_beam.index == beam) & (rolled_steel_beam["W_N/m"] == W))
    steel_beam = rolled_steel_beam.loc[condition].iloc[0]
    

    Area = steel_beam["Area"]
    h = steel_beam["h"]
    bf = steel_beam["bf"]
    tf = steel_beam["tf"]
    rzz = steel_beam["rzz"]
    ryy = steel_beam["ryy"]

    # Determining buckling class

    rmin=min(ryy,rzz)
    if h/bf>1.2 and tf<=40:
        if rmin==rzz:
            buckling_class='a'
        elif rmin==ryy:
            buckling_class='b'
    elif h/bf>1.2 and 40<=tf<=100:
        if rmin==rzz:
            buckling_class='b'
        elif rmin==ryy:
            buckling_class='c'
    elif h/bf<=1.2 and tf<=100:
        if rmin==rzz:
            buckling_class='b'
        elif rmin==ryy:
            buckling_class='c'
    elif h/bf<=1.2 and tf>100:
        if rmin==rzz:
            buckling_class='d'
    elif rmin==ryy:
            buckling_class='d'

    return Area, h, bf, tf, rzz, ryy,buckling_class

def imperfection_factor(buckling_class:str)->float:
    """
    Returns the imperfection factor for the given buckling class
    """
    if (buckling_class=='a'):
        alpha=0.21
    elif (buckling_class=='b'):
        alpha=0.34
    elif (buckling_class=='c'):
        alpha=0.49
    elif (buckling_class=='d'):
        alpha=0.76
        
    return alpha

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
    to determine the design compressive strength of the member
    """
    section=rolled_steel_beam(beam,W)
    Area=section[0]
    rzz,ryy=section[4],section[5]
    buckling_class=section[6]
    rmin=min(rzz,ryy)*10
    K=effective_length_factor(condition)
    E=2*10**5
    
    fcc=(math.pi**2*E)/(((K*L*1000)/rmin)**2)
    lamda=math.sqrt(fy/fcc)
    buckling_class=section[6]
    alpha=imperfection_factor(buckling_class)
    phi=0.5*(1+(alpha*(lamda-0.2))+(lamda**2))
    fcd=(fy/psf)/(phi+math.sqrt((phi**2)-(lamda**2)))
    Pcd=fcd*Area*100*10**-3

    return round(Pcd,2)

