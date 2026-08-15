import sections as sections

def test_rolled_steel_beam():
    Area,h,bf,tf,rzz,ryy,buckling_class=sections.rolled_steel_beam("ISHB 350", 710.20)
    assert Area ==92.21
    assert h==350
    assert bf==250
    assert tf==11.6
    assert rzz ==14.65
    assert ryy==5.22
    assert buckling_class=='b'

def test_imperfection_factor():
    alpha=sections.imperfection_factor('b')
    assert alpha==0.34
