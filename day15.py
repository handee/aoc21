import numpy as np

#fn='input/test15.txt'
fn='input/day15.txt'
def readinfile(fn):
    l=[]
    c=[]
    with open(fn) as fp:
        for line in fp:
            l=[int(c) for c in line.strip()]
            c.append(l)
    s=np.array(c)
    return(s)

def calc_cost(a):
    #fill in top row
    print(f"and here we do the work")
    costs=np.zeros_like(a)
    #fill in top side
    for i in range(1,a.shape[0]):
        costs[0,i]=costs[0,i-1]+a[0,i]
    #fill in left side
    for i in range(1,a.shape[1]):
         costs[i,0]=costs[i-1,0]+a[i,0]
    #fill in the rest
    for j in range(1,a.shape[1]):
        for i in range(1,a.shape[0]):
            costs[j,i]=min(costs[j-1,i],costs[j,i-1])+a[j,i]
    return(costs)
   
def scale_cave(a,s):
    w=a.shape[0]
    h=a.shape[1]
    newcave=np.zeros([h*s,w*s],np.int64)
    for ty in range(0,s):
        for tx in range(0,s):
            newvals=a*1+(tx+ty)
            newvals=np.where(newvals>9,newvals-9,newvals)
            newcave[ty*h:ty*h+h, tx*w:tx*w+w]=newvals
    print(newcave.shape)
    return(newcave)


def partone():
    caves=readinfile(fn)
    print(caves)
    costs=calc_cost(caves)
    print(costs[-1,-1])

def parttwo():
    caves=readinfile(fn)
    newc=scale_cave(caves,5)
    print(newc[0,:])
    costs=calc_cost(newc)
    print(costs[-1,-1])
    print(costs[0,:])
    print(costs[-1,:])


parttwo()
