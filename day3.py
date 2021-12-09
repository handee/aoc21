import numpy as np 

#fn='input/test3.txt'
fn='input/day3.txt'

def bools2dec(boolarray):
   
    rv=boolarray.astype(int)
    t=2 ** np.flip(np.arange(len(rv)))
    return(np.sum(np.multiply(rv,t)))
    

def string2dec(binstring):
    decimal=0
    for char in binstring:
        if char=='1':
            decimal=decimal*2+1
        else:
            decimal=decimal*2
    return(decimal)
            

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


def workoutmostpopular(candidates,n):
    sums1=[0]*n
    sums0=[0]*n
    for d in candidates:
        for i,c in enumerate(d):
            if c=='1':
                sums1[i]+=1
            else: # it must be 0
                sums0[i]+=1
    gamma=[0]*n
    for i,b in enumerate(sums1):
        if b>=sums0[i]:
            gamma[i]=1
    return(gamma)
  
def part_two():
    with open(fn) as fp:
        ds=[line.strip() for line in fp]
    n = len(ds[0])

    candidates=ds
    candidates2=ds.copy()
    element=0

    while(len(candidates2)>1):
        
        gamma=workoutmostpopular(candidates2,n)
        epsilon=[1-i for i in gamma]
        b=[]
        for i in range(len(candidates2)):
            if int(candidates2[i][element])==epsilon[element]:
                b.append(candidates2[i])

        
        element+=1
        candidates2=b
    

    element=0
    while(len(candidates)>1):
        
        gamma=workoutmostpopular(candidates,n)
        b=[]
        for i in range(len(candidates)):
            if int(candidates[i][element])==gamma[element]:
                b.append(candidates[i])
        
        element+=1
        candidates=b
    print(f"Gamma candidate = {candidates[0]}")
    print(f"Epsilon candidate = {candidates2[0]}")
    a=string2dec(candidates[0])
    b=string2dec(candidates2[0])
    print(f"oxygen={a} co2={b} ans={a*b}")


part_two()
