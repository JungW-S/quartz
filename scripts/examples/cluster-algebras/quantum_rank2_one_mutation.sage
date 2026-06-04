# Sage verification for the Quantum Cluster Algebras topic.
#
# Example id: quantum-rank2-one-mutation
# This checks one quantum seed mutation for the compatible pair
#   B = [[0, 1], [-1, 0]], L = [[0, -1], [1, 0]].
# The coefficient variable v represents q^(1/2).

R = LaurentPolynomialRing(QQ, "v")
v = R.gen()

B = Matrix(ZZ, [[0, 1], [-1, 0]])
L = Matrix(ZZ, [[0, -1], [1, 0]])


class QuantumTorusElement:
    def __init__(self, terms=None):
        self.terms = {}
        for exponent, coefficient in (terms or {}).items():
            coefficient = R(coefficient)
            if coefficient != 0:
                self.terms[tuple(exponent)] = self.terms.get(tuple(exponent), R(0)) + coefficient
        self.terms = {exponent: coefficient for exponent, coefficient in self.terms.items() if coefficient != 0}

    @staticmethod
    def monomial(exponent, coefficient=1):
        return QuantumTorusElement({tuple(exponent): R(coefficient)})

    def __add__(self, other):
        out = dict(self.terms)
        for exponent, coefficient in other.terms.items():
            out[exponent] = out.get(exponent, R(0)) + coefficient
        return QuantumTorusElement(out)

    def __mul__(self, other):
        out = {}
        for left_exp, left_coeff in self.terms.items():
            for right_exp, right_coeff in other.terms.items():
                exponent = tuple(left_exp[i] + right_exp[i] for i in range(len(left_exp)))
                commutation_power = sum(left_exp[i] * right_exp[j] * L[i, j] for i in range(2) for j in range(2))
                coefficient = left_coeff * right_coeff * v**commutation_power
                out[exponent] = out.get(exponent, R(0)) + coefficient
        return QuantumTorusElement(out)

    def scale_by_q_power(self, power):
        # power is the exponent of q, so q^power = v^(2*power).
        return QuantumTorusElement({exponent: coefficient * v ** (2 * power) for exponent, coefficient in self.terms.items()})

    def __eq__(self, other):
        return self.terms == other.terms

    def __repr__(self):
        return repr(self.terms)


def mutate_matrix_pair(L, B, k):
    E = Matrix(ZZ, B.nrows(), B.nrows())
    F = Matrix(ZZ, B.ncols(), B.ncols())

    for i in range(B.nrows()):
        for j in range(B.nrows()):
            if j != k:
                E[i, j] = 1 if i == j else 0
            elif i == j == k:
                E[i, j] = -1
            else:
                E[i, j] = max(0, -B[i, k])

    for i in range(B.ncols()):
        for j in range(B.ncols()):
            if i != k:
                F[i, j] = 1 if i == j else 0
            elif i == j == k:
                F[i, j] = -1
            else:
                F[i, j] = max(0, B[k, j])

    return E.transpose() * L * E, E * B * F


def mutation_exponents(B, k):
    a_prime = []
    a_double_prime = []
    for i in range(B.nrows()):
        if i == k:
            a_prime.append(-1)
            a_double_prime.append(-1)
        else:
            a_prime.append(max(0, B[i, k]))
            a_double_prime.append(max(0, -B[i, k]))
    return tuple(a_prime), tuple(a_double_prime)


assert L * B == Matrix.identity(ZZ, 2)

L_mutated, B_mutated = mutate_matrix_pair(L, B, 0)
expected_L_mutated = Matrix(ZZ, [[0, 1], [-1, 0]])
expected_B_mutated = Matrix(ZZ, [[0, -1], [1, 0]])

assert L_mutated == expected_L_mutated
assert B_mutated == expected_B_mutated
assert L_mutated * B_mutated == Matrix.identity(ZZ, 2)

a_prime, a_double_prime = mutation_exponents(B, 0)
assert a_prime == (-1, 0)
assert a_double_prime == (-1, 1)

X1_inv = QuantumTorusElement.monomial((-1, 0))
X_minus_1_1 = QuantumTorusElement.monomial((-1, 1))
X1_mutated = X1_inv + X_minus_1_1
X2 = QuantumTorusElement.monomial((0, 1))

# The displayed ordered form of X^(-1,1) is q^(-1/2) X1^(-1) X2.
ordered_X1_inv_X2 = X1_inv * X2
assert ordered_X1_inv_X2 == QuantumTorusElement.monomial((-1, 1), v)

# The mutated cluster variables must q-commute using L'_{12}=1.
assert X1_mutated * X2 == (X2 * X1_mutated).scale_by_q_power(1)

print("quantum-rank2-one-mutation verified")
print("L * B =", L * B)
print("L' =", L_mutated)
print("B' =", B_mutated)
print("a' =", a_prime)
print("a'' =", a_double_prime)
print("X1' =", X1_mutated)
