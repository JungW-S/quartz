# Sage verification for the Cluster Algebras topic.
#
# Example id: rank2-a2-one-mutation
# This checks the one-step mutation example for the rank-two skew-symmetric seed
# with exchange matrix [[0, 1], [-1, 0]].

R = PolynomialRing(QQ, ("x1", "x2"))
x1, x2 = R.gens()
F = FractionField(R)
x1 = F(x1)
x2 = F(x2)

B = Matrix(ZZ, [[0, 1], [-1, 0]])


def mutate_matrix(B, k):
    """Mutate an exchange matrix at zero-based index k."""
    rows = B.nrows()
    cols = B.ncols()
    out = Matrix(ZZ, rows, cols)
    for i in range(rows):
        for j in range(cols):
            if i == k or j == k:
                out[i, j] = -B[i, j]
            else:
                correction = max(B[i, k], 0) * max(B[k, j], 0)
                correction -= max(-B[i, k], 0) * max(-B[k, j], 0)
                out[i, j] = B[i, j] + correction
    return out


def mutate_variable(xs, B, k):
    """Return the mutated variable at zero-based index k."""
    positive = F(1)
    negative = F(1)
    for i, x in enumerate(xs):
        exponent = B[i, k]
        if exponent > 0:
            positive *= x**exponent
        elif exponent < 0:
            negative *= x**(-exponent)
    return (positive + negative) / xs[k]


xs = [x1, x2]
x1_mutated = mutate_variable(xs, B, 0)
B_mutated = mutate_matrix(B, 0)

expected_x1_mutated = (1 + x2) / x1
expected_B_mutated = Matrix(ZZ, [[0, -1], [1, 0]])

assert x1_mutated == expected_x1_mutated
assert B_mutated == expected_B_mutated

print("rank2-a2-one-mutation verified")
print("x1' =", x1_mutated)
print("B' =", B_mutated)
