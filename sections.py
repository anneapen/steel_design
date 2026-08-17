import pandas as pd


def rolled_steel_beam(beam:str,W:float)->tuple[float,float,float,float,float]:
    """
    """
    df=pd.read_csv('rolled_steel_beams.csv')
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

    return Area, h, bf, tf, rzz, ryy

def buckling_class(beam:str,W:float)->str:
    """
    Returns the buckling class of the member
    """   
    section=rolled_steel_beam(beam,W)
    h=section[1]
    bf=section[2]
    tf=section[3]
    rzz,ryy=section[4],section[5]
        
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

    return buckling_class

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

def rolled_steel_channel(channel:str,W:float)->float:
    """
    Returns the section properties of the given channel
    """
    df=pd.read_csv('rolled_steel_channels.csv')
    df=df.set_index('Section')
    rolled_steel_channel=df.copy()
    condition = ((rolled_steel_channel.index == channel) & (rolled_steel_channel["W_N"] == W))
    steel_channel = rolled_steel_channel.loc[condition].iloc[0]
    

    Area = steel_channel["Area"]
    h = steel_channel["h"]
    b = steel_channel["b"]
    tf = steel_channel["tf"]
    tw = steel_channel["tw"]
    rxx = steel_channel["rxx"]
    ryy = steel_channel["ryy"]

    return Area, h, b, tf,tw, rxx, ryy

def rolled_steel_equal_angle(equal_angle:str,W:float)->float:
    """
    """
    df=pd.read_csv('rolled_steel_equal_angles.csv')
    df=df.set_index('Section')
    rolled_steel_equal_angle=df.copy()
    condition = ((rolled_steel_equal_angle.index == equal_angle) & (rolled_steel_equal_angle["W_N"] == W))
    steel_equal_angle = rolled_steel_equal_angle.loc[condition].iloc[0]
    

    Area = steel_equal_angle["Area"]
    t = steel_equal_angle["t"]
    Ixx = steel_equal_angle["Ixx_Iyy"]
    rxx = steel_equal_angle["rxx_ryy"]   

    return Area, t,Ixx,rxx

def rolled_steel_unequal_angle(unequal_angle:str,W:float)->float:
    """
    """
    df=pd.read_csv('rolled_steel_unequal_angles.csv')
    df=df.set_index('Section')
    rolled_steel_unequal_angle=df.copy()
    condition = ((rolled_steel_unequal_angle.index == unequal_angle) & (rolled_steel_unequal_angle["W_N"] == W))
    steel_unequal_angle = rolled_steel_unequal_angle.loc[condition].iloc[0]
    

    Area = steel_unequal_angle["Area"]
    t = steel_unequal_angle["t"]
    Ixx = steel_unequal_angle["Ixx"]
    Iyy = steel_unequal_angle["Iyy"]
    rxx = steel_unequal_angle["rxx"]
    ryy = steel_unequal_angle["ryy"]    

    return Area, t,Ixx,Iyy,rxx,ryy
