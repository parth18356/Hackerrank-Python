nd = input().split()
n = int(nd[0])
d = int(nd[1])
a=list(map(int, input().rstrip().split()))
def leftrotation(a,d):
    print(*(a[d:]+a[:d]))
(leftrotation(a,d))
