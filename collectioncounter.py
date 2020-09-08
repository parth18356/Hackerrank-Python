import collections
p=int(input())
aa=list(map(int, input().rstrip().split()))
q=int(input())
z=0
l=[]
lo=[]
s=collections.Counter(aa)
for i in range(q):
    no,mo=map(int, input().split())
    if s[no]:
        z=z+mo
        s[no]=s[no]-1
print(z)
        

    #if no in aa:
     #   l.append(mo)
    #else:
     #   lo.append(mo)
#print(sum(l))
        
