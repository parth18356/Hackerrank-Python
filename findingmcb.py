import math 
a= int(input())
b= int(input())
c= math.sqrt(a*a+b*b)
an = math.acos(b/c )
d=math.degrees(an)
print(round(d),chr(176),sep='' )
