#Git: https://github.com/IMrMoon/numerical_analysis_homework_4.git
# Names:
# Segev Chen 322433400
# Gad Hasson 207898123
# Artiom Bondar 332692730
# Carmel Dor 316015882



import math


def f(x):
    return math.sin(x)


def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral


if __name__ == "__main__":
    a = 0
    b = math.pi
    n = 4

    # חישוב האינטגרל בשיטת הטרפזים
    integral_approximation = trapezoidal_rule(a, b, n)
    print("Approximation of the integral using trapezoidal rule:", integral_approximation)

    # חישוב השגיאה
    true_value = 2
    error = abs(true_value - integral_approximation)
    print("Error:", error)
