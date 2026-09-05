import pandas as pd
import math


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
    Returns the section properties of the given equal angle
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
    Returns the section properties of the given unequal angle
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

def rolled_steel_tee_bar(tee_bar:str,W:float)->float:
    """
    Returns the section properties of the given tee bar
    """
    df=pd.read_csv('rolled_steel_tee_bars.csv')
    df=df.set_index('Section')
    rolled_steel_tee_bar=df.copy()
    condition = ((rolled_steel_tee_bar.index == tee_bar) & (rolled_steel_tee_bar["W_N"] == W))
    steel_tee_bar = rolled_steel_tee_bar.loc[condition].iloc[0]
    

    Area = steel_tee_bar["Area"]
    h = steel_tee_bar["h"]
    b = steel_tee_bar["b"]
    tf = steel_tee_bar["tf"]
    tw = steel_tee_bar["tw"]
    Ixx = steel_tee_bar["Ixx"]
    Iyy = steel_tee_bar["Iyy"]
    rxx = steel_tee_bar["rxx"]
    ryy = steel_tee_bar["ryy"]    

    return Area, h,b,tf,tw,Ixx,Iyy,rxx,ryy

def section_classification(bf: float,tf: float,tw: float,d: float,fy: float) -> str:
    """
    Returns the governing class of the section as per Table 2 of IS 800:2007
    """

    epsilon = math.sqrt(250 / fy)

    # Flange outstand
    b = (bf - tw) / 2

    flange_ratio = b / tf
    web_ratio = d / tw

    # Flange classification
    if flange_ratio <= 9.4 * epsilon:
        flange_class = "plastic"
    elif flange_ratio <= 10.5 * epsilon:
        flange_class = "compact"
    elif flange_ratio <= 15.7 * epsilon:
        flange_class = "semi-compact"
    else:
        flange_class = "slender"

    # Web classification for web subjected to bending
    if web_ratio <= 84 * epsilon:
        web_class = "plastic"
    elif web_ratio <= 105 * epsilon:
        web_class = "compact"
    elif web_ratio <= 126 * epsilon:
        web_class = "semi-compact"
    else:
        web_class = "slender"

    classes = {
        "plastic": 1,
        "compact": 2,
        "semi-compact": 3,
        "slender": 4
    }

    #The governing class will be the worse of flange class and web class
    if classes[flange_class] >= classes[web_class]:
        return flange_class
    else:
        return web_class