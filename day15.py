import numpy as np

fn='input/test15.txt'
def readinfile(fn):
    l=[]
    c=[]
    with open(fn) as fp:
        for line in fp:
            l=[int(c) for c in line.strip()]
            c.append(l)
    s=np.array(c)
    return(s)

def calc_cost(arr):
    #fill in top row
    print(f"and here we do the work")
    #fill in left side

def partone():
    caves=readinfile(fn)
    print(caves)
    costs=calc_cost(caves)

partone()
