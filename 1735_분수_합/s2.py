"""
2 7
3 5

31 35
"""
import math

a, b = map(int, input().split())
c, d = map(int, input().split())

demon = a * d + c * b
mole = b * d

gcd = math.gcd(demon, mole)
demon = demon // gcd
mole = mole // gcd

print(demon, mole)