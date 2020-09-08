if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    y=list(integer_list)
    y.sort()
    a=max(y)
    while max(y)==a:
        y.remove(max(y))
    print(max(y))
