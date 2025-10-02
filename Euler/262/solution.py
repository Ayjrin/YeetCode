# Problem 262
# ===========
#
# The following equation represents the continuous topography of a
# mountainous region, giving the elevation h at any point (x,y):
#
# [Image: 262_formula1.gif]
#
# A mosquito intends to fly from A(200,200) to B(1400,1400), without leaving
# the area given by 0 ≤ x, y ≤ 1600.
#
# Because of the intervening mountains, it first rises straight up to a
# point A', having elevation f. Then, while remaining at the same elevation
# f, it flies around any obstacles until it arrives at a point B' directly
# above B.
#
# First, determine f[min] which is the minimum constant elevation allowing
# such a trip from A to B, while remaining in the specified area.
# Then, find the length of the shortest path between A' and B', while flying
# at that constant elevation f[min].
#
# Give that length as your answer, rounded to three decimal places.
#
# Note: For convenience, the elevation function in the image above can be
# written as the following in Python (the math module must be imported):
#
# def elevation(x, y):
#     first = 5000.0 - ((x**2 + y**2 + x*y)/200.0) + (12.5*(x+y))
#     second = (0.000001 * (x**2 + y**2)) - (0.0015*(x+y)) + 0.7
#     return first * math.exp(-abs(second))

