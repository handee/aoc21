

fn='input/day10.txt'
#fn='input/test10.txt'
def partone():
    openers=['{','[','(','<']
    closers=['}',']',')','>']
    scores=[1197,57,3,25137]
    with open(fn) as fp:
        score=0
        
        for line in fp:
            line=line.strip()
            stack=[]
            unclosed_pointer=-1
            for c in line: 
                if c in openers:
                    stack.append(c)
                else:
                    brackettype=closers.index(c)
                    if stack[-1]==openers[brackettype]:
                        stack.pop()
                    else:
                        print(f'{line} wrong type of bracket: expected {stack[-1]} got {c} ')
                        score+=scores[brackettype]
                        break
    print(score)
def parttwo():
    openers=['{','[','(','<']
    closers=['}',']',')','>']
    scores=[1197,57,3,25137]
    completescores=[3,2,1,4]
    autocompletescores=[]
    with open(fn) as fp:
        score=0
        
        for line in fp:
            line=line.strip()
            stack=[]
            unclosed_pointer=-1
            corrupt=False
            for c in line: 
                if c in openers:
                    stack.append(c)
                else:
                    brackettype=closers.index(c)
                    if stack[-1]==openers[brackettype]:
                        stack.pop()
                    else:
                        print(f'{line} wrong type of bracket: expected {stack[-1]} got {c} ')
                        score+=scores[brackettype]
                        corrupt=True
                        break
            if not corrupt:
                thisscore=0
                stack.reverse()
                for a in stack:
                    brackettype=openers.index(a)
                    thisscore*=5
                    thisscore+=completescores[brackettype]
                    line=line+closers[brackettype]
                print(f'{line} {thisscore}') 
                autocompletescores.append(thisscore)
    autocompletescores.sort()
    print(autocompletescores)
    print(autocompletescores[int(len(autocompletescores)/2)])


                    
 
#partone()
parttwo()
