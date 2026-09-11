import bending_members as bending_members

def test_bending_strengh_laterally_supported():
    Md=bending_members.bending_strengh_laterally_supported('compact',700000,800000,250,1.1)
    assert Md==181.82

def test_design_shear_strength():
    Vd=bending_members.design_shear_strength(2800,250,1.1)
    assert Vd==367.4