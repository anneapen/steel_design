import sections as sections

def test_rolled_steel_beam():
    Area,h,bf,tf,rzz,ryy=sections.rolled_steel_beam("ISHB 350", 710.20)
    assert Area ==92.21
    assert h==350
    assert bf==250
    assert tf==11.6
    assert rzz ==14.65
    assert ryy==5.22

def test_buckling_class():
    buckling_class=sections.buckling_class("ISHB 350", 710.20)
    buckling_class=='b'


def test_imperfection_factor():
    alpha=sections.imperfection_factor('b')
    assert alpha==0.34

def test_rolled_steel_channel():
    Area, h, b, tf,tw, rxx, ryy=sections.rolled_steel_channel('ISJC 100',56.9)
    assert (Area,h,b,tf,tw, rxx, ryy)==(7.41, 100.0, 45.0, 5.1, 3.0, 4.09, 1.42)

def test_rolled_steel_equal_angle():
    Area, t,Ixx,rxx=sections.rolled_steel_equal_angle("ISA 2020",8.8)
    assert (Area, t,Ixx,rxx)==(1.12, 3.0, 0.4, 0.58)

def test_rolled_steel_unequal_angle():
    Area, t,Ixx,Iyy,rxx,ryy=sections.rolled_steel_unequal_angle("ISA 3020",10.8)
    assert (Area, t,Ixx,Iyy,rxx,ryy)==(1.41, 3.0, 1.2, 0.4, 0.92, 0.54)

def test_rolled_steel_tee_bar():
    Area, h,b,tf,tw,Ixx,Iyy,rxx,ryy=sections.rolled_steel_tee_bar("ISNT 20",8.8)
    assert (Area, h,b,tf,tw,Ixx,Iyy,rxx,ryy)==(1.13, 20.0, 20.0, 3.0, 3.0, 0.4, 0.2, 0.59, 0.39)

def test_section_classification():
    section_class=sections.section_classification(200,10,8,300,250)
    assert section_class=='compact'