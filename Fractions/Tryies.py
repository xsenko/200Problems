from fractions import gcd

def mygcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def simplify_fraction(numer, denom):
    if denom == 0:
        return "Division by 0 - result undefined"

    common_divisor = gcd(numer, denom)
    print("cmd is: %d" %(common_divisor))
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)

    if reduced_den == 1:
        return "%d/%d is simplified to %d" % (numer, denom, reduced_num)
    elif common_divisor == 1:
        return "%d/%d is already at its most simplified state" %(numer,denom)
    else:
        return "%d/%d is simplified to %d/%d" % (numer,denom,reduced_num,reduced_den)

print(simplify_fraction(20,10))
x = mygcd(10,20)
print(x)