import bending_members as bending_members

def test_bending_strengh_laterally_supported():
    Md=bending_members.bending_strengh_laterally_supported('compact',700000,800000,250,1.1)
    assert Md==181.82

def test_bending_strengh_laterally_unsupported():
    Md=bending_members.bending_strengh_laterally_unsupported('compact',1050000,1200000,250,1.1,0.8)
    assert Md==217.01

def test_design_shear_strength():
    Vd=bending_members.design_shear_strength(280,10,250,1.1)
    assert Vd==367.4

def test_flange_plastic_moment():
    MZp=bending_members.flange_plastic_moment(400,200,16,250,1.1)
    assert MZp==279.27

def test_reduced_bending_strength():
    Mdv=bending_members.reduced_bending_strength(250,350,200,150)
    assert Mdv==190.82

def test_deflection_check():
    assert bending_members.deflection_check(12.5,6000,300)==True

def test_design_beam():
    assert bending_members.design_beam(beam='ISHB 350',W=710.20,
    fy=250,
    Mu=150,
    Vu=100,
    laterally_supported=True,
    actual_deflection=12,
    span=6000,
    limit_ratio=300)==True