#! python3 -uOO
############################################### my resolver ;-) (backtracking)
sqr   = lambda g,x,y: g[y*9+x:y*9+x+3] + g[y*9+x+9:y*9+x+12] + g[y*9+x+18:y*9+x+21]
col   = lambda g,x:   g[x::9]
row   = lambda g,y:   g[y*9:y*9+9]
free  = lambda g,x,y: set("123456789") - set(col(g,x) + row(g,y) + sqr(g,(x//3)*3,(y//3)*3))

def resolv(g):
    i=g.find(".")
    if i>=0:
        for elem in free(g,i%9,i//9):
            ng=resolv( g[:i] + elem + g[i+1:] )
            if ng: return ng
    else:
        return g
###############################################

import time

gg = [i.strip() for i in open("g_simples.txt")][:100]

t=time.monotonic()
for g in gg:
    rg=resolv(g)
    assert rg and rg.find(".")<0, "not resolved ?!"
    print(rg)

print( "Took: ", time.monotonic() - t )