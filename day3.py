import numpy as np 

fn='input/day3test.txt'
#fn='input/input3.1.txt'

def bools2dec(boolarray):
    rv=boolarray.astype(int)
    t=2 ** np.flip(np.arange(len(rv)))
    return(np.sum(np.multiply(rv,t)))
        

def part_one():
    with open(fn) as fp:
        ds=[line.strip() for line in fp]
    n = len(ds[0])
    sums1=np.zeros(n)
    sums0=np.zeros(n)
    for d in ds:
        for i,c in enumerate(d):
            if c=='1':
               sums1[i]+=1
            else: # it must be 0
               sums0[i]+=1
    gamma=np.zeros(n,dtype=np.bool)
    for i,b in enumerate(sums1):
        if b>sums0[i]:
            gamma[i]=1
    epsilon=np.invert(gamma)
    e=bools2dec(epsilon)
    g=bools2dec(gamma)


    print(f"sums0 {sums0} sums1 {sums1} gamma {gamma} epsilon {epsilon} ")
    print(f"{g} {e} power {g*e}")



def part_two():
    with open(fn) as fp:
        ds=[line.strip() for line in fp]
    n = len(ds[0])
    sums1=np.zeros(n)
    sums0=np.zeros(n)
    for d in ds:
        for i,c in enumerate(d):
            if c=='1':
                sums1[i]+=1
            else: # it must be 0
                sums0[i]+=1
    gamma=np.zeros(n,dtype=np.bool)
    for i,b in enumerate(sums1):
        if b>sums0[i]:
            gamma[i]=1
    epsilon=np.invert(gamma)

    candidates=ds
    element=0

    while(len(candidates)>1):
        b=filter(lambda x: x[element]==gamma[element],candidates)
        element+=1
        candidates=list(b)
        print(candidates)


part_two()
