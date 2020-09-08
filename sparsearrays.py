N = int(input())
arr = []
for _ in range(N):
    arr.append(input().strip())
Q = int(input())
for _ in range(Q):
    query = input()
    print(arr.count(query))
