import steel_design_calcs as steel_design_calcs

def test_edge_distance():
    emin,emax=steel_design_calcs.edge_distance(12,10,250)
    assert emin,emax==(18.0, 120.0)
