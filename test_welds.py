import welds as welds

def test_design_strength_of_butt_weld():
    T_dw=welds.design_strength_of_butt_weld(150,12,240,250,'shop weld','single')[0]
    assert T_dw==225.0

def test_angle_of_fusion():
    K=welds.angle_of_fusion(60)
    assert K==0.7

def test_design_strength_of_fillet_weld():
    V_dw=welds.design_strength_of_fillet_weld(6,216,'shop weld',410,60)[1]
    assert V_dw==171.8