Basically the same thing, but with **a big improvment** on the algorithm, which makes them a lot faster 

Here is the python version, it's the same algo but with a new constraint "choosing the most constrained digit each iteration" (thanks to [2e71828](https://users.rust-lang.org/u/2e71828))
:

```python

sqr   = lambda g,x,y: g[y*9+x:y*9+x+3] + g[y*9+x+9:y*9+x+12] + g[y*9+x+18:y*9+x+21]
col   = lambda g,x:   g[x::9]
row   = lambda g,y:   g[y*9:y*9+9]
free  = lambda g,x,y: set("123456789") - set(col(g,x) + row(g,y) + sqr(g,(x//3)*3,(y//3)*3))

def resolv(g):
    holes={}
    for i in range(81):
        if g[i]==".":
            holes[i]=free(g,i % 9, i // 9)
            if len(holes[i])==1: break
    if holes: 
        i,avails = sorted( holes.items() , key=lambda x: len(x[1])).pop(0)
        for c in avails:
            ng = resolv( g[:i] + c + g[i+1:] )
            if ng: return ng
    else:
        return g
```

And now, they are resolving all the grids in `g_simples.txt` : **1011 grids**

On my computer (Intel® N100 × 4 / ubuntu 23.10), I got :

```
py3.7:      0m 25s
py3.11:     0m 16s
pypy3.10:   0m 12s
codon0.16:  0m 14s

mojo0.4.0:  0m 2.4s (sudoku_strings.mojo, with simple strings)
mojo0.4.0:  0m 0.8s (sudoku.mojo, with specialized types)

rust1.71:   0m 6.5s (with ultra-specialized rust types/apis)
rust1.71:   0m 0.6s (same^ with rustc options : -C opt-level=3 -C target-cpu=native)
```


