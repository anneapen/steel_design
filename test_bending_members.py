import bending_members as bending_members

def test_design_shear_strength():
    Vd=bending_members.design_shear_strength(2800,250,1.1)
    assert Vd==367.4