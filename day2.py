
#fn="input/test2.txt"
fn="input/input2.1.txt"


def part_one():
    h=0 #horizontal
    d=0 #depth
    with open(fn) as fp:
        for line in fp:
            i,n=line.split() # instruction, numeric
            if i[0]=='f':
                h+=int(n)
            elif i[0]=='d':
                d+=int(n)
            elif i[0]=='u':
                d-=int(n)
            print(f"{d} is depth, {h} is horizontal position, {d*h} is their product")
            
def part_two():
    h=0 #horizontal
    d=0 #depth
    a=0
    with open(fn) as fp:
        for line in fp:
            i,n=line.split() # instruction, numeric
            if i[0]=='f':
                h+=int(n)
                d+=int(n)*a
            elif i[0]=='d':
                a+=int(n)
            elif i[0]=='u':
                a-=int(n)
            print(f"{d} is depth, {h} is horizontal position, {a} is aim, {d*h} is their product")
            
            
#part_one()
part_two()

