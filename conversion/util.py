AbsoluteZeroC = float(-273)
AbsoluteZeroF = float(-459.67)

def F_to_C(F):
    if F <= AbsoluteZeroF:
        return ValueError("Error: Below absolute 0");
    else:
        C = float((F-32) * (5/9))
        return C

def C_to_F(C):
    if C <= AbsoluteZeroC:
        return ValueError("Error: Below absolute 0");
    else:
        F = float((9/5)*C + 32)
        return F