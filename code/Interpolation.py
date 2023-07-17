# Interpolation
import numpy as np
from scipy.fft import fft, ifft

def interpolation(vector_x, polynomial):
    n = len(vector_x)
    OPT = [[0] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        OPT[i][i] = [evaluate_polynomial(polynomial, vector_x[i])]
        for j in range(i + 1, n):
            OPT[i][j] = ((multiply_poly(OPT[i][j - 1], np.array([0, -1]) + [vector_x[j], 0])
                         - multiply_poly(OPT[i + 1][j], np.array([0, -1]) + [vector_x[i], 0])
                          ) // (vector_x[j] - vector_x[i])).tolist()

    for i in range(n):
        print(OPT[i])

def evaluate_polynomial(polynomial, x):
    value = 0
    for i in range(len(polynomial)):
        value += polynomial[i] * (x ** i)
    return value

def multiply_poly(poly1, poly2):
    polynomial_FFT = fft(np.pad(poly1, (0, len(poly2) - 1))) * fft(np.pad(poly2, (0, len(poly1) - 1)))   # FFT multiply
    return np.round(np.real(ifft(polynomial_FFT))).astype(int)


# vector_x1 = [-2, -1, 0, 1, 2]
# polynomial1 = [0, 1, 2, 3, 4]    # 0 + x + 2x^2 + 3x^3 + 4x^4
vector_x2 = [0, 1, 2, 3]
polynomial2 = [5, 1, -5, 1]    # 5 + x - 5x^2 + x^3
interpolation(vector_x2, polynomial2)

