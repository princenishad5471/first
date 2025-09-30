#def x(area,circumferance):
#    return area and circumferance
#r=10
#pi=3.14
#area= pi*r**2
#circumferance=2*pi*r
#print(area)
#print(circumferance)


import math

def circle_stats(radius):
    area=math.pi* radius**2
    circumference=2*math.pi*radius
    return area,circumference
    


a=(circle_stats(int(input("circle radius:= "))))
c=(circle_stats(int(input("circle radius:= "))))
print("circle: " ,a,"circumference: ",c)



