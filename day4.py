import math


fn='input/day4.txt'
#fn='input/test4.txt'

class bingocard:
    def __init__ (self):
        self.rows=[]
        self.seen=[]
        self.winner=False
    def print_card(self):
        for i,line in enumerate(self.rows):
            print(line)
            print(self.seen[i])
    def clear_card(self):
        rows=[]
        seen=[]
    def add_line(self,line):
        self.rows.append(line)
        self.seen.append([False,False,False,False,False])
    def check_number(self,num):
        print(f"Checking {num}")
        if self.winner:
            board_score=-2
        else: 
            board_score=0
            for j,row in enumerate(self.rows):
                for i,e in enumerate(row):
                    if e==num:
                        # we've seen one
                        self.seen[j][i]=True
                        # check the row and col
                        truecount=0
                        for ii in range(0,5):
                            if self.seen[j][ii]==True:
                               truecount+=1
                        if truecount==5:
                            print("******gotarow*******")
                            self.winner=True
                        truecount=0
                        for jj in range(0,5):
                            if self.seen[jj][i]==True:
                                truecount+=1
                        if truecount==5:
                            print("******gotacol*******")
                            self.winner=True
                    if not self.seen[j][i]:
                        board_score+=self.rows[j][i]

        if (self.winner):
            ret_val=board_score*num
        else:
            ret_val=-1
        return(ret_val)



    
def part_one():
    first=True;
    second=False;
    numbers=[]
    cards=[]
    with open(fn) as fp:
        for line in fp:
            if (first):
                print('got numbers')
                numbers=[int(i) for i in line.strip().split(',')]
                first=False
                second=True
            elif len(line)<2:
                current_card=bingocard()
                cards.append(current_card)
                print('adding card')
            else:
                print('adding line')
                cards[-1].add_line([int(i) for i in line.strip().split()])
    i=0
    while i < len(numbers):
        for c in cards:
            a=c.check_number(numbers[i])
            print (a)
            if (a>0):
                print("we have a winner")
                i=len(numbers)
        i+=1
    
     
def part_two():
    first=True;
    second=False;
    numbers=[]
    cards=[]
    with open(fn) as fp:
        for line in fp:
            if (first):
                print('got numbers')
                numbers=[int(i) for i in line.strip().split(',')]
                first=False
                second=True
            elif len(line)<2:
                current_card=bingocard()
                cards.append(current_card)
                print('adding card')
            else:
                print('adding line')
                cards[-1].add_line([int(i) for i in line.strip().split()])
    i=0
    winners=[]
    while i < len(numbers):
        for e,c in enumerate(cards):
            a=c.check_number(numbers[i])
            print (a)
            if (a>0):
                print(f"we have a winner at card number {e}")
                winners.append([e,a])

        i+=1
    print(winners)
                   
part_two()


