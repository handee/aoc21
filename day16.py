h2d = {
'0' : '0000',
'1' : '0001',
'2' : '0010',
'3' : '0011',
'4' : '0100',
'5' : '0101',
'6' : '0110',
'7' : '0111',
'8' : '1000',
'9' : '1001',
'A' : '1010',
'B' : '1011',
'C' : '1100',
'D' : '1101',
'E' : '1110',
'F' : '1111',
}
t0='C200B40A82'
t1='04005AC33890'
t2='9C0141080250320F1802104A08'
#fn='input/test16.txt'
fn='input/day16.txt'

def read_in_file():
    with open(fn) as fp:
        s=fp.readline().strip()
    return(h2bin(s))

def h2bin(h):
    o=""
    for c in h:
       o=o+h2d[c]

    return(o)

def string2dec(binstring):
    decimal=0
    for char in binstring:
        if char=='1':
            decimal=decimal*2+1
        else:
            decimal=decimal*2
    return(decimal)
            

def decode_packet(pstr,vers,vals):
    ans=[]
    v=string2dec(pstr[0:3])
    vers.append(v)
    t=string2dec(pstr[3:6])
    print(f"type {t}")
    if t==4:
        print("literal")
        n=""
        cptr=6
        unfinished=True
        while (unfinished):
            if (pstr[cptr]=='0'):
                n=n+pstr[cptr+1:cptr+5]
                unfinished=False
                ostr=pstr[cptr+5:]
            elif (pstr[cptr]=='1'):
                n=n+pstr[cptr+1:cptr+5]
                cptr+=5
        number=string2dec(n)
        vals.append(number)
        ans.append(number)
        if '1' in ostr:
            v,va=decode_packet(ostr,vers,vals)
            ans=ans+va
        
    else :
        print("operator")

        id=pstr[6]
        if (id=='0'):
            length_of_sub_packs=string2dec(pstr[7:21])
            v,va=decode_packet(pstr[22:],vers,vals)
        else:
            no_of_sub_packs=string2dec(pstr[7:17])
            v,va=decode_packet(pstr[18:],vers,vals)
        print(f"OK we are in opreator land vals={vals}")
        print(f"va={va}")
        if t==0:
            print("sum")
            ans=sum(va)
        elif t==1:
            print("product")
            ans=1
            for n in va:
                ans*=n
        elif t==2:
            print("min")
            ans=min(va)
        elif t==3:
            print("max")
            ans=max(va)
        elif t==5:
            print("gt")
            ans=0
            if va[0]>va[1]:
                ans=1
        elif t==6:
            print("lt")
            ans=0
            if va[0]<va[1]:
                ans=1
        elif t==7:
            print("eq")
            ans=0
            if va[0]==va[1]:
                ans=1
        ans=[ans]
    return(vers,ans)

def partone():
    b0=h2bin(t0)
    b1=h2bin(t1)
    b2=h2bin(t2)
    print(b0)
    vers=[]
    vals=[]
    vd,a=decode_packet(b0,vers,vals)
    print(a)
    vers=[]
    vals=[]
    vd,a=decode_packet(b1,vers,vals)
    print(a)
    print("That was the first one")
    vers=[]
    vals=[]
    vd,a=decode_packet(b2,vers,vals)
    print(a)
    print("That was the second one")

    p=read_in_file()
    vers=[]
    vals=[]
#    vd,a=decode_packet(p,vers,vals)
#    print(a)


partone()
