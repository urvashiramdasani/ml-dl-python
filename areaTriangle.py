#Practical 2.a Date 9 January 2020
import math
def areaTriangle():
    s1 = int(input('Enter first side: '))
    s2 = int(input('Enter second side: '))
    s3 = int(input('Enter third side: '))
    s = float((s1 + s2 +s3)/2)
    area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
    print("Area of triangle is {0}".format(area))
areaTriangle()