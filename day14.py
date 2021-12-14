#fn='input/test14.txt'
fn='input/day14.txt'

import time
from collections import Counter

def readinfile(fna):
    p={}
    t=''
    with open(fna) as fp:
        for line in fp:
            if len(t)==0:
                t=list(line.strip())
            elif len(line)>1:
                s,f=line.strip().split(' -> ')
                p[s]=f
    return(t,p)


def run_generation(template,rules):
    i=0
    while i < len(template)-1: 
        pair="".join([template[i],template[i+1]])
        template.insert(i+1, rules[pair])
        i+=2
    return(template)


def run_generation_counter(pairs,lut):
    i=0
    newcount=Counter()
    for p in pairs:
        for op in lut[p]:
            newcount[op]+=pairs[p]
    return(newcount)


def gen_lut(rules):
    lut={}
    for r,p in rules.items(): 
        lut[r]=[r[0]+p,p+r[1]]
    return(lut)

def count_pair_components(pairs):
    counts=Counter()
    for p,c in pairs.items():
        counts[p[0]]+=c
        counts[p[1]]+=c
    return(counts)



def partone(gens):
    t, rules=readinfile(fn)
    tokens=[]
    counts=[]
    bigt=''
    littlet=''
    for i in range(gens):
        tic=time.perf_counter()
        t=run_generation(t,rules)
        maxc=0
        minc=len(t)
        if (i<10):
            tokens=list(set(t))
            counts.clear()
            for e in tokens:
                c=t.count(e)
                counts.append(c)
            bigt=tokens[counts.index(max(counts))]
            littlet=tokens[counts.index(min(counts))]
            # 5 gens in we know the biggest and smallest token
        toc=time.perf_counter()
        maxc=max(counts)
        minc=min(counts)
        #pt="".join(t)
        #print(pt)
        print(f"{i+1}, {maxc}, {minc}, {maxc-minc}, {toc-tic:0.4f}")
        


def parttwo(gens):
    t, rules=readinfile(fn)
    bigt=''
    littlet=''
    lut=gen_lut(rules)
    print(lut)
    lol=[item for sublist in lut.values() for item in sublist]
    tokens=list(set(lol))
    print(tokens)
    #set up initial pairs
    ps=[]
    for i in range(len(t)-1):
        p="".join([t[i],t[i+1]])
        ps.append(p)
    print(ps)
    pairs=Counter(ps)

    
    for i in range(1,gens):
        tic=time.perf_counter()
        pairs=run_generation_counter(pairs,lut)
        counts=count_pair_components(pairs)
        counts[t[0]]+=1
        counts[t[-1]]+=1
        maxc=counts.most_common()[0]
        minc=counts.most_common()[-1]
        maxn=maxc[1]/2
        minn=minc[1]/2

        toc=time.perf_counter()
        print(f"{i}, {maxn}, {minn}, {maxn-minn}, {toc-tic:0.4f}")
        #print(t)
partone(5)

parttwo(41)
