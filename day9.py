import numpy as np
#fn='input/test9.txt'
fn='input/day9.txt'

def readinfile(fn):
    #reads in and pads with 9s
    seafloor=[]
    scanline=[]
    with open(fn) as fp:
        for line in fp:
            scanline=[9]
            scanline+=[int(c) for c in line.strip()]
            scanline.append(9)
            seafloor.append(scanline)
    pad=[9]*(len(scanline))
    seafloor.append(pad)
    seafloor.insert(0,pad)
    s=np.array(seafloor)
    return(s)


def find_minima(f):
    minima=[]
    minlocs=[]
    for y,line in enumerate(f):
        if y>0 and y<(len(f)-1):
            for x in range(1,len(line)):
                if (f[y][x]<f[y-1][x]):
                    if (f[y][x]<f[y+1][x]):
                        if (f[y][x]<f[y][x-1]):
                            if (f[y][x]<f[y][x+1]):
                                minima.append(f[y][x])
                                minlocs.append([x,y])
    return(minima,minlocs)
 
def region_grow(minima,s):
    region=np.zeros_like(s)
    # got the x and y the wrong way around
    seed_points=[[minima[1],minima[0]]]
    while len(seed_points)>0:
        p=seed_points[0]
        region[p[0]][p[1]]=1
        if s[p[0]+1][p[1]]<9:
            if region[p[0]+1][p[1]]==0:
                seed_points.append([p[0]+1,p[1]])
        if s[p[0]-1][p[1]]<9:
            if region[p[0]-1][p[1]]==0:
                seed_points.append([p[0]-1,p[1]])
        if s[p[0]][p[1]+1]<9:
            if region[p[0]][p[1]+1]==0:
                seed_points.append([p[0],p[1]+1])
        if s[p[0]][p[1]-1]<9:
            if region[p[0]][p[1]-1]==0:
                seed_points.append([p[0],p[1]-1])
        seed_points.pop(0)
    size=sum([sum(l) for l in region])
    return(size)

def partone():
    f=readinfile(fn)
    mins,minlocs=find_minima(f)
    risk=[x+1 for x in mins]
    print(mins)
    print(minlocs)
    print(risk)
    print(sum(risk))

def parttwo():
    f=readinfile(fn)
    mins,minlocs=find_minima(f)
    basin_sizes=[]
    for m in minlocs:
        s=region_grow(m,f)
        basin_sizes.append(s)
    
    basin_sizes.sort()
    print(basin_sizes[-3]*basin_sizes[-2]*basin_sizes[-1])



#partone()
parttwo()
