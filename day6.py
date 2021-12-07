

fn='input/day6.txt'
#fn='input/test6.txt'
from collections import Counter

def update_generation(fish):
    newfish=Counter([0,1,2,3,4,5,6,7,8]) 
    for i in range(0,8):
        newfish[i]=fish[i+1]
    newfish[6]+=fish[0]
    newfish[8]=fish[0]
    return(newfish)

def part_one(generations):
    fishes=Counter({0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0})
    with open(fn) as fp:
        line=fp.readline()
        inifish=[int(i) for i in line.strip().split(',')]
    initgen=Counter(inifish)
    print(initgen)
    fishes+=initgen
    print(fishes)
    for i in range (0, generations):
        fishes=update_generation(fishes)
        print(sum(fishes.values()))
    print(sum(fishes.values()))
    

    
    #part 2 is just part 1 with a bigger n 
part_one(256)


