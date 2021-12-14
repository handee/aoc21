import numpy as np
import matplotlib.pyplot as plt
#fn='input/test11.txt'
fn='input/day11.txt'

def readinfile(fn):
    #reads in and pads with 9s
    dat=[]
    with open(fn) as fp:
        for line in fp:
            dat.append([int(c) for c in line.strip()])
    return(dat)

def get_neighbours(y,x,octopi):
    neighbours=[]
    for i in range(-1,2):
        for j in range(-1,2):
            y1=y+i
            x1=x+j
            if y1>=0 and x1>=0 and y1<octopi.shape[0] and x1<octopi.shape[1]:
                if not ((y==y1) and (x==x1)):
                    if octopi[y1,x1]<10:
                        neighbours.append([y1,x1])
    return(neighbours)


def energystep(o):
    o+=1
    locs=np.where(o>9)
    potentialflashers=[]
    for i,v in enumerate(locs[0]):
        a=get_neighbours(v,locs[1][i],o)
        potentialflashers+=a
    while len(potentialflashers)>0:
        [y,x]=potentialflashers.pop(0)
        o[y,x]+=1
        if o[y,x]==10:
            a=get_neighbours(y,x,o)
            potentialflashers+=a
    o2=np.where(o>9,0,o)

    return(o2)

def partone():
    a=readinfile(fn)
    octopi=np.array(a)
    print(octopi)
    generations=100
    counts=0
    for i in range(generations):
        octopi=energystep(octopi)
        counts+=(octopi==0).sum()
    print(octopi)
    print(counts)

def save_visualisation(octopi,c):
    framen='output/frame'+str(c).zfill(4)+'.png'
    scale=50
    octopi_large= np.zeros(np.array(octopi.shape) * scale)

    for j in range(octopi.shape[0]):
        for k in range(octopi.shape[1]):
            octopi_large[j * scale: (j+1) * scale, k * scale: (k+1) * scale] = octopi[j, k]
    octopi_large=np.where(octopi_large==0,15,octopi_large)
    plt.imsave(framen, octopi_large, cmap='inferno',vmin=0, vmax=15)

def parttwo():
    a=readinfile(fn)
    octopi=np.array(a)
    counter=0
    while(counter<400):
    #while((octopi==0).sum()<100):
        counter+=1
        octopi=energystep(octopi)
        print((octopi==0).sum())
        save_visualisation(octopi,counter)
    print(octopi)
    print(counter)

parttwo()
