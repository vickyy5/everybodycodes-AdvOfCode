def readInput():
    with open('test.in','r') as f:
        line = [ i for i in f]
        line = line[0].strip()
    return line




def part1(line):
    arr = line.split(",")
    for i in arr:
        low, high = i.split("-")
        print(f"{low} {high}")
        for i in range(int(low),int(high))




l = readInput()
part1(l)
