if __name__ == '__main__':
    o=[]
    z=[]
    sum=0
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        o.append(name)
    query_name = input()
    for i in range(0,len(o)):
        if o[i]==query_name:
            p=student_marks[o[i]]
            for j in range(len(p)):
                sum=sum+p[j]
                l=(sum)/(len(p))
    print("{0:.2f}".format(l)) #prnting upto 2 decimal 
