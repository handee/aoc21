import numpy as np
import matplotlib.pyplot as plt

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

def point_inside_array(p,a):
    rv=True
    if p[0] < 0 or p[1] < 0 or p[0] >= a.shape[0] or p[1] >= a.shape[1]:
        rv=False
    return rv

def calc_cost_4w(a):
    # array to hold points we've seen before
    pts=[]
    logical_max=a.shape[0]*a.shape[1]*9
    costs=np.ones_like(a)*logical_max
    costs[0,0]=0
    done=np.zeros_like(costs) #array to work out which we've done
    done[0,:]+=1
    done[:,0]+=1
    pts.append([0,1])
    pts.append([1,0]) 
    while len(pts)>0:
        #cp = current_point
        cp=pts[0]
        # get neighbours
        pn=[[cp[0]-1,cp[1]],[cp[0],cp[1]-1],[cp[0]+1,cp[1]],[cp[0],cp[1]+1]]
        # prune neighbour list if they're outside of the array
        # also look up the cost of valid ones whilst we're looping
        min_cost_neighbour=logical_max
        vpn=[]
        while len(pn)>0:
            p=pn.pop()
            if point_inside_array(p,a):
                if costs[p[0],p[1]]<min_cost_neighbour:
                    min_cost_neighbour=costs[p[0],p[1]]
                vpn.append(p)
        #the best cost of the current point so far is...
        done[cp[0],cp[1]]+=1
        costs[cp[0],cp[1]]=min(costs[cp[0],cp[1]],min_cost_neighbour+a[cp[0],cp[1]])
        # then add each valid neighbour to our point search list
        for p in vpn:
            if (done[p[0],p[1]]<4):
                if p not in pts: # if it's not on our list already add it
                    pts.append(p)
        pts.pop(0)
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



def save_visualisation(manual):
    framen='output/cave.png'
    scale=2
    manual_large= np.zeros(np.array(manual.shape) * scale)

    for j in range(manual.shape[0]):
        for k in range(manual.shape[1]):
            manual_large[j * scale: (j+1) * scale, k * scale: (k+1) * scale] = manual[j, k]
    plt.imsave(framen, manual_large, cmap='inferno')



def parttwo():
    caves=readinfile(fn)
    newc=scale_cave(caves,5)
    save_visualisation(newc)
    print(newc[0,:])
    costs=calc_cost_4w(newc)
    print(costs[-1,-1])
    print(costs[0,:])
    print(costs[-1,:])


parttwo()
