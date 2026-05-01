"""created 4/14/26"""
import math
import sys
import re

'''
Testing inputs:

Stopping Criteria:
N = 1000
TOL = -11

Polynomial:
x**4 + 2* x**2 - x - 3

Initial Points:
p_0 = -1
p_1 = -0.5
p_2 = 0

Output that should be generated:
-0.876053115817114 + 0.00000i

'''
# ** for exponents 
# stopping criteria
print("Establish stopping criteria")
N = input("Enter the maximum number of iterations: ")
TOL = 10**int(input("Enter an exponent for tolerance: "))

# specific function
poly_str = input("Type polynomial in terms of x (use ** for exponents): ")
if not re.match(r'^[0-9x\+\-\*\/\.\s\(\)]+$',poly_str):
    print("Error: Invalid characters detected.")
    sys.exit()

# Checks for polynomial input mistakes
try:
    compile(poly_str, '<string>', 'eval')
except SyntaxError:
    print("Error: Syntax issue in your math.")
    sys.exit()

f = lambda x: eval(poly_str, {"__builtins__":{}}, {"x":x})
# {"__builtins__":{}} blocks all Python functions
# {"x":x} tells eval x is the only variable

# Catches invalid math operations
VAL = -1000.0
while VAL <= 1000.0:
    try:
        f(VAL)
        VAL += 0.05 # creates more than just integer testing points
    except ZeroDivisionError:
        print(f"Note: Undefined at x = {VAL} (Division by Zero)")
    except Exception:
        print(f"Error at x = {VAL}")
        sys.exit()

# initial conditions (points) that create an approximating parabola
print("Ensure initial points are distinct values.")
try:
    p0 = float(input("Enter p_0 = "))
except ValueError:
    print(f"Error: Invalid character. Input a number.")
    sys.exit()
try:
    p1 = float(input("Enter p_1 = "))
except ValueError:
    print(f"Error: Invalid charater. Input a number.")
    sys.exit()
try:
    p2 = float(input("Enter p_2 = "))
except ValueError:
    print(f"Error: Invalid character. Input a number.")
    sys.exit()

# generates denominators 
h1 = p1 - p0
h2 = p2 - p1

# distance formulas
d1 = (f(p1) - f(p0)) / h1
d2 = (f(p2) - f(p1)) / h2
d = (d2 - d1) / (h2 + h1)

for i in range(int(N)):
    b = d2+ h2 * d
    w = (complex(b**2 - 4 * d * f(p2)))**(0.5)
    if abs(b - w) < abs(b + w):
        E = b + w
    else: 
        E = b - w

    h = ((-2) * f(p2))/E
    p = p2 + h
    if abs(h) < TOL:
        if isinstance(p,complex):
            print(f"Root: {p.real:.15f} + {p.imag:.5f}i")
        else:
            print(f"Root:{p:.15f}")
        break
    # overrides previous values with new values
    p0 = p1
    p1 = p2
    p2 = p
    h1 = p1 - p0
    h2 = p2 - p1
    d1 = (f(p1) - f(p0)) / h1
    d2 = (f(p2) - f(p1)) / h2
    d = (d2 - d1) / (h2 + h1)
print(f"Number of iterations:",i)