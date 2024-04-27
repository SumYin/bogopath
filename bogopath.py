import random as r
import math
from collections import Counter

def bogopath(g, vertex_start, vertex_end):
    z=0
    path = []
    while check_path(path, vertex_start, vertex_end) == False:
        z+=1
        path = random_subgraph(g)
    return [path, z]

def check_path(path, vertex_start, vertex_end):
    if len(path) == 0:
        return False
    
    vertecies= [vertex for edge in path for vertex in edge]
    pvd=Counter(vertecies)

    if (len(pvd) == len(path)+1) and (vertex_start in pvd.keys()) and (vertex_end in pvd.keys()):
        if (sum(pvd.values()) == len(pvd)*2-2) and pvd[vertex_start] == 1 and pvd[vertex_end] == 1:
            return True
    return False

def random_subgraph(g):
    p = []
    l=len(g)
    a=0
    for x in range(1, l+1):
        a+=(math.comb(l, x))
    chances = [math.comb(l, x)/a for x in range(1, l+1)]
    n = r.choices(range(1, l+1), weights=chances)[0]
    e=g.copy()
    while len(p) < n:
        v = r.choice(e)
        p.append(v)
        e.remove(v)

    return p