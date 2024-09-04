import math

numberValue = 12                      # Integer
stringValue = "hallo"                 # String
doubleValue = 1.2                     # Float (double precision in other languages)
floatValue = 3.14109203               # Float
myBoolean = True                      # Boolean

def findRoot(a, b, c):
    
    # variable lokal
    d = math.sqrt(b**2 - 4*a*c)
    root1 = -b/(2*a) + d
    root2 = -b/(2*a) - d
    return root1, root2

# variable global
value_a = 1
value_b = 1
value_c = 1

akar1, akar2 = findRoot(value_a, value_b, value_c)