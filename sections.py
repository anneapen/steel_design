import pandas as pd


def rolled_steel_beam(beam:str,W:float)->tuple[float,float,float,float,float]:
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