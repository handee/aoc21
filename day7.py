fn='input/day7.txt'
#fn='input/test7.txt'

def brute_force(crabs):
    maxdepth=max(crabs)
    mindepth=min(crabs)
    bestfuel=(maxdepth-mindepth)*len(crabs)# initialise with worst case
    for i in range(mindepth,maxdepth):
        fuelusage=0
        for c in crabs:
            print(f"Move from {c} to {i}: {abs(i-c)} fuel")
            fuelusage+=abs(i-c)
        print(f"Total fuel={fuelusage}, best so far={bestfuel}")
        if fuelusage<bestfuel:
            bestdepth=i
            bestfuel=fuelusage
    return(bestdepth,bestfuel)

def brute_force_part_two(crabs):
    maxdepth=max(crabs)
    mindepth=min(crabs)
    bestfuel=(maxdepth-mindepth)*len(crabs)# initialise with worst case
    bestfuel=(bestfuel*(bestfuel+1))/2
    for i in range(mindepth,maxdepth):
        fuelusage=0
        #fuel_usage is now sum of integers from 1...depth_delta
        #sum of integers from 1..n = (n(n+1))/2
        for c in crabs:
            depth_delta=abs(i-c) 
            fuelusage+=int((depth_delta*(depth_delta+1))/2)
        print(f"Total fuel={fuelusage}, best so far={bestfuel}")
        if fuelusage<bestfuel:
            bestdepth=i
            bestfuel=fuelusage
    return(bestdepth,bestfuel)


def part_one():
    crabs=[]
    with open(fn) as fp:
        line=fp.readline()
        crabs=[int(i) for i in line.strip().split(',')]
    d,f=brute_force(crabs)
    print(f"{d}= best depth, {f}=fuel usage")
 
def part_two():
    crabs=[]
    with open(fn) as fp:
        line=fp.readline()
        crabs=[int(i) for i in line.strip().split(',')]
    d,f=brute_force_part_two(crabs)
    print(f"{d}= best depth, {f}=fuel usage")
    
   

    
part_two()


