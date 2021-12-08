

fn='input/day8.txt'

#fn='input/test8.txt'

        

def part_one():
    with open(fn) as fp:
        output=[line.split(' | ') for line in fp]
    known_count=0
    print(output)
    for o in output:
        c=o[1].split()
        for n in c:
            if len(n)==2:
                known_count+=1
            elif len(n)==4:
                known_count+=1
            elif len(n)==3:
                known_count+=1
            elif len(n)==7:
                known_count+=1
            else:
                print("None of the above, must be 2,3,5,6, or 9")
    
    print(f"there were {known_count} numbers i could identify")

def decoded(lookup,display):
    print(f"decoding {display}")
    decoded=[]
    for element in display:
        for k,v in lookup.items():
            if set(element)==v:
                 decoded.append(k)
    if len(decoded)==len(display):
        print(f"Input={display} Decoded={decoded}")
        a=str()
        for i in decoded:
            a=a+str(i)
        return(True,int(a))
    else:
        return(False,0)
                    
def part_two():
    with open(fn) as fp:
        output=[line.split(' | ') for line in fp]
    known_count=0
    known={}
    total=0
    for o in output:
        display=o[1].split()
        data=o[0].split()
        print(f"Processing line : {display} data:{data}")
        data+=display # use data and display as evidence 
        known.clear()
        for n in data:
            if len(n)==2:
                known[1]=set(n)
            elif len(n)==4:
                known[4]=set(n)
            elif len(n)==3:
                known[7]=set(n)
            elif len(n)==7:
                known[8]=set(n)
        a=known[7].difference(known[4]).pop()
        b='x'
        c='x'
        d='x'
        e='x'
        f='x'
        g='x'
        infournotseven=known[4].difference(known[7])
        finished=False;
        while not finished:
            print(f"known = {known}")
            print(f"lknown = {len(known)}")
            for n in data:
                sn=set(n)
                alreadyseen=False
                for s in known.values():
                    if sn==s: 
                        alreadyseen=True
                if not alreadyseen:
                    if len(sn)==5: # 2,3 or 5

                        if known[1].issubset(sn): # 1 is a subset
                           known[3]=sn
                           d=infournotseven.intersection(known[3]).pop()
                           infournotseven.remove(d)
                           b=infournotseven.pop()
                       # need to work out waht to do if not seen 
                        elif b in sn:
                           known[5]=sn
                        else:
                           if b!='x':
                               known[2]=sn
                    elif len(sn)==6: # 0, 9, or 6
                        if known[1].issubset(sn):
                            # it's 9 or 0
                            # do we know d yet?
                            if d!='x':
                                if d in sn:
                                    known[9]=sn
                                else:
                                    known[0]=sn
                        else:
                            known[6]=sn

            finished,n=decoded(known,display)
            print(n)
            total+=n

    print(total)

    



part_two()


