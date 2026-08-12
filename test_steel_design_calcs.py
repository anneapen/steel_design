import steel_design_calcs as steel_design_calcs

def test_class_of_bolt():
    fub,fyb=steel_design_calcs.class_of_bolt(4.6)
    assert fub,fyb==(400,240.0)

def test_net_area_of_bolt():
    Anb=steel_design_calcs.net_area_of_bolt(12)[0]
    assert Anb==88.22

def test_hole_diameter():
    do=steel_design_calcs.hole_diameter(20)
    assert do==22

def test_edge_distance():
    emin,emax=steel_design_calcs.edge_distance(20,10,250)
    assert emin,emax==(33.0, 120.0)

def test_pitch():
    p_min,p_max=steel_design_calcs.pitch(20,10,'compression')
    assert p_min,p_max==(50.0,120)

def test_tensile_strength_of_bolt():
    T_db=steel_design_calcs.tensile_strength_of_bolt(4.6,20)
    assert T_db==70.57

def test_bearing_strength_of_bolt():
    V_dpb=steel_design_calcs.bearing_strength_of_bolt(20,410,4.6,14)
    assert V_dpb==114.8

def test_shear_strength_of_bolt():
    V_dsb=steel_design_calcs.shear_strength_of_bolt(4.6,20,1,0,150,50,5)
    assert V_dsb==45.27

def test_design_strength_of_butt_weld():
    T_dw=steel_design_calcs.design_strength_of_butt_weld(150,12,240,250,'shop weld','single')[0]
    assert T_dw==225.0

def test_design_strength_of_fillet_weld():
    V_dw=steel_design_calcs.design_strength_of_fillet_weld(6,216,'shop weld',410)[1]
    assert V_dw==171.8