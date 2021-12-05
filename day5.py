import math
import numpy as np

fn='input/day5.txt'
#fn='input/test5.txt'

        

def part_one():
    vecs=[]
    max_x=0
    max_y=0
    with open(fn) as fp:
        for line in fp:
            tvecs=line.strip().split(' -> ') 
            print(tvecs)
            p1,p2=[p.split(',') for p in tvecs]
            if p1[0]==p2[0] or p1[1]==p2[1]:
                ip1=[int(p1[0]), int(p1[1])]
                ip2=[int(p2[0]), int(p2[1])]
                if ip1[0]>max_x:
                    max_x=ip1[0]
                if ip2[0]>max_x:
                    max_x=ip2[0]
                if ip1[1]>max_y:
                    max_y=ip1[1]
                if ip2[1]>max_y:
                    max_y=ip2[1]
                vecs.append([ip1,ip2])
    print(vecs)
    print(max_x,max_y)
    seafloor=np.zeros([max_x+2,max_y+2])
    
    
    for v1,v2 in vecs:
        # need to account for which is bigger
        print(v1,v2)
        if v1[0]==v2[0]:
           print("horiz")
           y1=max(v1[1],v2[1])
           y2=min(v1[1],v2[1])
           print(y1,y2)
           for yi in range(y2,y1+1):
               
               seafloor[yi,v1[0]]+=1
        if v1[1]==v2[1]:
           x1=max(v1[0],v2[0])
           x2=min(v1[0],v2[0])
           print("vert")
           print(x1,x2)
           for xi in range(x2,x1+1):
               seafloor[v1[1],xi]+=1
    print(seafloor)

    p=np.where(seafloor>=2)
    print(len(p[0]))


part_one()


