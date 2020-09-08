from re import compile
data, pattern = input(), compile( input() )
m = pattern.search(data)
if not m : print( "(-1, -1)" )
while m: 
    print( f"({m.start()}, {m.end()-1})" )
    m = pattern.search( data, m.start()+1 )
