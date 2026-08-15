
import compression_members as compression_members

def test_effective_length_factor():
    K=compression_members.effective_length_factor('fixed_fixed')
    assert K==0.65

def test_design_compressive_strength():
    Pcd=compression_members.design_compressive_strength('ISHB 350',710.20,4,250,1.1,'fixed_fixed')
    assert Pcd==1794.69