# Returning multiple values
#Create  a function that returns both the area and circumference of a circle given its radius.

import math
def properties(radius):
    area=math.pi*radius*radius
    perimeter=2*math.pi*radius
    return area,perimeter

a,c=properties(2)
print(f"Area: {a:.2f} Circumference: {c:.2f}")