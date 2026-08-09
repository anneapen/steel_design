import steel_design_calcs as steel_design_calcs

def test_edge_distance():
    emin,emax=steel_design_calcs.edge_distance(12,10,250)
    assert emin,emax==(18.0, 120.0)

def test_class_of_bolt():
    fub,fyb=steel_design_calcs.class_of_bolt(4.6)
    assert fub,fyb==(400,240.0)

def test_net_area_of_bolt():
    Anb=steel_design_calcs.net_area_of_bolt(12)
    assert Anb==88.22

def test_hole_diameter():
    do=steel_design_calcs.hole_diameter(20)
    assert do==22