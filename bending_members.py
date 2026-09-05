import math

def bending_strengh_laterally_supported()->float:
    """
    """
    if section=='plastic' or section=='compact':
        beta=1
    elif section=='semi-compact':
        beta=Ze/Zp
    else:
        raise ValueError print("Secction should be plastic or compact or semi compact")

    Md=beta*Zp*fy/gamma_mo
    return Md