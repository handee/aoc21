import math


fn='input/input1.1.txt'
#fn='input/test1.txt'

        

def part_one():
    increased=0
    pd=0
    c=0
    with open(fn) as fp:
        ds=[int(line.strip()) for line in fp]
    for d in ds:
        if c==0:
            increased=0
        else:
            if pd<d:
                increased+=1
        c+=1
        pd=d
    
    print(f"there were {c} measurements and {increased} of them were larger than the previous")

def part_two():
    increased=0
    pa=0 #previous sum 
    ca=0
    with open(fn) as fp:
        ds=[int(line.strip()) for line in fp]
    for c in range(len(ds)):
        if c<2 :
            increased=0
        else:
            ca=sum(ds[c-2:c+1]) #current sum
            if c>2:
                if pa<ca:
                    increased+=1
        c+=1
        pa=ca
    
    print(f"there were {c} measurements and taking in mind the 3 measurement moving average, {increased} of them were larger than the previous")


part_two()


