import math

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
