import tension_members as tension_members

def test_gross_section_yielding():
    T_dg=tension_members.gross_section_yielding(250,1200)
    assert T_dg==272.73