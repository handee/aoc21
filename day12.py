#fn='input/test12.txt'
#fn='input/test12b.txt'
#fn='input/test12c.txt'
fn='input/day12.txt'

from collections import defaultdict
def readinfile(fna):
    p=defaultdict(list)
    with open(fna) as fp:
        for line in fp:
            s,f=line.strip().split('-')
            p[s].append(f)
            if (f != 'end'):
                p[f].append(s)
    return p

def follow(cs,c,psf,op):
    p=list(op)
    #print(f"Following paths from {c}, paths so far={psf}, current_path={p}")
    if (c=='end'):
        print(f"Path end")
        p.append(c)
        psf.append(p)
    elif c.islower():
        #print(f"It's lowercase")
        if (c in p) :
            print(f"{c} is lowercase and already in {p}: don't follow path")
        else:
            p.append(c)
            for cave in cs[c]:
                follow(cs,cave,psf,p)
    else:
        p.append(c)
        for cave in cs[c]:
            follow(cs,cave,psf,p)

def follow2(cs,c,psf,op):
    p=list(op)
    #print(f"Following paths from {c}, paths so far={psf}, current_path={p}")
    if (c=='end'):
        #print(f"Path end")
        p.append(c)
        psf.append(p)
    elif c.islower():
        #print(f"It's lowercase")
        v=p.count(c) # how many times have we visited this cave?
        if c=='start' and v==1:
            ds=True
            #print("o no double starty")
        elif v<1:
            #we have not visited it before so that is fine
            p.append(c)
            for cave in cs[c]:
                follow2(cs,cave,psf,p)
        elif v<2:
            lc_cavenames=[]
            for k in cs.keys():
                if k.islower():
                    lc_cavenames.append(k)
            doublevisits=0
            for lc in lc_cavenames:
                lcv=p.count(lc) # how many times have we visited this cave?
                if (lcv==2):
                    doublevisits+=1
            if doublevisits<1:
                p.append(c)
                for cave in cs[c]:
                    follow2(cs,cave,psf,p)
       
            
    else:
        p.append(c)
        for cave in cs[c]:
            follow2(cs,cave,psf,p)


def partone():
    cavesystem=readinfile(fn)
    print(cavesystem)
    paths=[]
    cave=('start')
    follow(cavesystem,cave,paths,[])
    print(f"done")
    print(paths)
    print(len(paths))

def parttwo():
    cavesystem=readinfile(fn)
    print(cavesystem)
    paths=[]
    cave=('start')
    follow2(cavesystem,cave,paths,[])
    print(f"done")
    lc_cavenames=[]
    for k in cavesystem.keys():
        if k.islower():
            lc_cavenames.append(k)
    actual_paths=[]
    for p in paths:
        doublevisits=0
        for c in lc_cavenames:
            v=p.count(c) # how many times have we visited this cave?
            if (v==2):
                doublevisits+=1
#            print(f"{c} was visited {v} times")
        if doublevisits<=1:
            actual_paths.append(p)
    for p in paths:
        print(p, end="")
        for c in lc_cavenames:
            v=p.count(c) # how many times have we visited this cave?
            print(f"c {c} v {v};",end="")
        print()
    print(len(paths))


parttwo()
