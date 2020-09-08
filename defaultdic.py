import re as lol
for i in range(int(input())):  
    try:
        print(bool(lol.compile(input())))
    except:
        print('False')
