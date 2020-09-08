from collections import namedtuple
n=int(input())
m=input().split()
z=0
for i in range(n):
    sheet=namedtuple('sheet',m)
    m1,m2,m3,m4=input().split()
    sheet=sheet(m1,m2,m3,m4)
    z=z+int(sheet.MARKS)
print(float(z/n))
    
