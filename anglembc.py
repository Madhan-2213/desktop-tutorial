import math

length_ab = int(input())
length_bc = int(input())

# applying pythagorean theorem
length_ac = math.sqrt(length_ab ** 2 + length_bc ** 2)
length_mc = length_ac / 2

# applying definition of tangent in right angled triangle
angle_mcb = math.atan(length_ab / length_bc)

# applying cosine theorem
length_mb = math.sqrt(length_bc ** 2 + length_mc ** 2 - 2 * length_bc * length_mc * math.cos(angle_mcb))

# applying sine theorem
angle_mbc = math.asin(length_mc * math.sin(angle_mcb) / length_mb)

# coverting from radian to degree
print(str(round(angle_mbc * 180 / math.pi)) + u'\N{DEGREE SIGN}')
