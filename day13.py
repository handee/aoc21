import numpy as np
import matplotlib.pyplot as plt 

fn='input/day13.txt'
#fn='input/test13.txt'


def readinfile(fna):
    with open(fna) as fp:
       pts=[line.strip().split(',') for line in fp]
    ipts=pts.index([''])
    ins=[]
    p=[]
    max_x=0
    max_y=0
    for i in range(0, len(pts)):
        if i>ipts:
            t,n=pts[i][0].split('=')
            xy=t[-1]
            ins.append([xy,int(n)])
        elif i<ipts:
            p.append([int(pts[i][0]),int(pts[i][1])])
            if p[i][0]>max_x:
                max_x=p[i][0]
            if p[i][1]>max_y:
                max_y=p[i][1]
    paper=np.zeros([max_y+1,max_x+1],dtype=int)
    for pt in p:
        paper[(pt[1],pt[0])]=1

            

    return(paper,ins)
       

def fold(paper, row, xy):
    if xy=='x':
        p2=paper[:,row+1:]
        p1=paper[:,:row]
        print(p1.shape,p2.shape)
        if p1.shape[1]>p2.shape[1]:
            print("off centre, pad with zeros at the far edge of p2")
            p2=np.pad(p2,((0,0),(0,p1.shape[1]-p2.shape[1])))
        print(p1.shape,p2.shape)
        p1+=np.flip(p2,axis=1)
        return(p1)
    else:
        p2=paper[row+1:,:]
        p1=paper[:row,:]
        print(p1.shape,p2.shape)
        if p1.shape[0]>p2.shape[0]:
            print("off centre, pad with zeros at the far edge of p2")
            p2=np.pad(p2,((0,p1.shape[0]-p2.shape[0]),(0,0)))
            print(p1.shape,p2.shape)
        p1+=np.flip(p2,axis=0)
        return(p1)

def save_visualisation(manual,i):
    framen='output/man'+str(i).zfill(4)+'.png'
    scale=2
    manual_large= np.zeros(np.array(manual.shape) * scale)

    for j in range(manual.shape[0]):
        for k in range(manual.shape[1]):
            manual_large[j * scale: (j+1) * scale, k * scale: (k+1) * scale] = manual[j, k]
    manual_large=np.where(manual_large>=1,0,255)
    plt.imsave(framen, manual_large, cmap='inferno')


def partone():
    p,ins=readinfile(fn)
    print (p)
    print (ins)
    for c,i in enumerate(ins):
        p=fold(p,i[1],i[0])
        n=np.count_nonzero(p)
        print(f"After {c} folds {n} dots are visible")
        save_visualisation(p,c)
    print (p)




partone()
