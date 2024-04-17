#Git: https://github.com/IMrMoon/numerical_analysis_homework_4.git
# Names:
# Segev Chen 322433400
# Gad Hasson 207898123
# Artiom Bondar 332692730
# Carmel Dor 316015882


import numpy as np

def linear_interpolation(points, x):
    # פונקציה לאינטרפולציה לינארית
    x_values = [p[0] for p in points]
    y_values = [p[1] for p in points]
    return np.interp(x, x_values, y_values)

def polynomial_interpolation(points, x):
    # פונקציה לאינטרפולציה פולינומית עבור 3 נקודות
    x_values = [p[0] for p in points]
    y_values = [p[1] for p in points]
    coeffs = np.polyfit(x_values, y_values, 2)  # חישוב פולינום מדרגה 2 (פולינום ריבועי)
    return np.polyval(coeffs, x)

def lagrange_interpolation(points, x):
    # פונקציה לאינטרפולציה על פי גרנג'
    def lagrange_basis(i, x):
        basis = [(x - points[j][0]) / (points[i][0] - points[j][0]) for j in range(len(points)) if j != i]
        return np.prod(basis)

    y = sum(points[i][1] * lagrange_basis(i, x) for i in range(len(points)))
    return y


if __name__ == "__main__":
    points = []  # רשימה לאחסון נקודות

    # קליטת נקודות מהמשתמש
    num_points = int(input("Enter the number of points: "))
    for i in range(num_points):
        x = float(input(f"Enter x coordinate of point {i + 1}: "))
        y = float(input(f"Enter y coordinate of point {i + 1}: "))
        points.append((x, y))

    # הצגת הנקודות שהוקלטו
    print("Points:")
    for point in points:
        print(point)

    # קליטת הערך x שאנו רוצים למצוא עבורו ערך y
    x_value = float(input("Enter the x value for interpolation: "))

    # בחירת שיטת אינטרפולציה
    method = int(input("Choose interpolation method:\n1. Linear\n2. Polynomial (3 points)\n3. Lagrange\n"))

    # ביצוע אינטרפולציה לפי השיטה שנבחרה
    if method == 1:
        result = linear_interpolation(points, x_value)
        print(f"Linear interpolation result for x={x_value}: y={result}")
    elif method == 2:
        if len(points) < 3:
            print("Polynomial interpolation requires at least 3 points.")
        else:
            result = polynomial_interpolation(points, x_value)
            print(f"Polynomial interpolation result for x={x_value}: y={result}")
    elif method == 3:
        if len(points) < 3:
            print("Lagrange interpolation requires at least 3 points.")
        else:
            result = lagrange_interpolation(points, x_value)
            print(f"Lagrange interpolation result for x={x_value}: y={result}")
    else:
        print("Invalid method choice.")
