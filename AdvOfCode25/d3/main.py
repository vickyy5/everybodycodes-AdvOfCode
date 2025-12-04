def part1():
    with open('day3.in','r') as f:
        arr = [ i.strip() for i in f]


    amb=[]
    for line in arr:
        maxBat=0
        ind=0
        maxBat, ind = getMaxBat(line)
        while len(line) == ind+1:
            maxBat, ind = getMaxBat(line[:-1])

        sb, sind = getMaxBat(line[ind+1:])
        #print(f"{line[ind+1:]}")

        mb = int(str(maxBat)+str(sb))
        #print(f"{mb}")
        amb.append(mb)

    s = sum([ int(i) for i in amb])
    print(s)


def getMaxBat(line):
    mx = 0
    ind = 0
    for i,n in enumerate(line):
        if int(n) > mx:
            mx = int(n)
            ind = int(i)

    return mx,ind

    
        
    
    
    
part1()
