import tension_members as tension_members

def test_gross_section_yielding():
    T_dg=tension_members.gross_section_yielding(250,1200)
    assert T_dg==272.73

def test_net_section_rupture_plates():
    T_dn=tension_members.net_section_rupture_plates(410,760)
    assert T_dn==224.35

def test_net_section_rupture_angles_channels():
    T_dn=tension_members.net_section_rupture_angles_channels(60,8,410,250,448,512,100,120)
    assert T_dn==264.2

def test_block_shear_failure():
    T_db=tension_members.block_shear_failure(410,250,1600,190,1050,300)
    assert T_db==247.14

def test_design_tensile_strength():
    T_d=tension_members.design_tensile_strength(250,1500,410,1060,1800,390,1300,500)
    assert T_d==312.91