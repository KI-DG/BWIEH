"""
2 7
3 5

31 35
"""


def gcd(x, y):
    while x % y != 0:
        mod = x % y
        x = y
        y = mod

    return y


a, b = map(int, input().split())
c, d = map(int, input().split())

gcd_1 = gcd(b, d)
demon = b * d // gcd_1
mole = a * (d // gcd_1) + c * (b // gcd_1)
gcd_2 = gcd(demon, mole)

print(mole // gcd_2, demon // gcd_2)
