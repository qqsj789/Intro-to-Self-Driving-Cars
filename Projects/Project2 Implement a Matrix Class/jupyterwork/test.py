import matrix as m

def test():
    I2 = m.Matrix([
        [1, 0],
        [0, 1]
        ])
    I2_neg = m.Matrix([
        [-1, 0],
        [0, -1]
        ])

    zero = m.Matrix([
        [0,0],
        [0,0]
        ])

    m1 = m.Matrix([
        [1,2,3],
        [4,5,6]
        ])

    m2 = m.Matrix([
        [7,-2],
        [-3,-5],
        [4,1]
        ])

    m1_x_m2 = m.Matrix([
        [ 13,  -9],
        [ 37, -27]])

    m2_x_m1 = m.Matrix([
        [ -1,   4,   9],
        [-23, -31, -39],
        [  8,  13,  18]])

    m1_m2_inv = m.Matrix([
        [1.5, -0.5],
        [2.0555556, -0.722222222]
        ])

    top_ones = m.Matrix([
        [1,1],
        [0,0],
        ])

    left_ones = m.Matrix([
        [1,0],
        [1,0]
        ])


    assert equal(-I2, I2_neg), "Error in your __neg__ function"
    assert equal(I2 + I2_neg, zero), "Error in your __add__ function"
    assert equal(m1 * m2, m1_x_m2), "Error in your __mul__ function"
    assert equal(m2 * m1, m2_x_m1), "Error in your __mul__ function"
    assert equal(m1_x_m2.inverse(), m1_m2_inv), """Error in your inverse function for the 1 x 1 case"""
    assert equal(I2.inverse(), I2), """Error in your inverse function for the 2 x 2 case"""
    assert equal(top_ones.T(), left_ones), "Error in your T function (transpose)"
    assert equal(left_ones.T(), top_ones), "Error in your T function (transpose)"
    assert equal(top_ones - left_ones.T(), m.zeroes(2,2)), "Error in your __sub__ function"
    assert (4*m.identity(5))[0][0] == 4, "Error in your __rmul__ function"
    assert (4*m.identity(5)).trace() == 20 , "Error in your trace function"

    print("Congratulations! All tests pass. Your Matrix class is working as expected.")

def equal(m1, m2):
    if len(m1.g) != len(m2.g): return False
    if len(m1.g[0]) != len(m2.g[0]): return False
    for r1, r2 in zip(m1.g, m2.g):
        for v1, v2 in zip(r1, r2):
            if abs(v1 - v2) > 0.0001:
                return False
    return True

test()