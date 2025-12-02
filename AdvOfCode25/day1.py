
with open('test.in','r') as f:
   lines = [ line.strip() for line in f]


def part2(lines):
    dial = 50
    password=0

    for i in lines:
        direction = i[0]
        inc = int(i[1:])

        if direction == 'R':
            if dial + inc >= 100:
                di = (dial+inc)//100
                v =abs( (dial+inc//100) - (dial//100))
                print(f"-di {di} y v{v}")
            dial = (dial + inc)%100
        else:
            if dial - inc <= 100:
                di = (dial-inc)//100
                v =abs( (dial+inc//100) - (dial//100))
                print(f"-di {di} y v{v}")
            dial = (dial - inc)%100
        
        if dial == 0:
            password = password+1

    print(password)


def part1():
    dial = 50
    password=0

    for i in lines:
        direction = i[0]
        inc = int(i[1:])
        if direction == 'R':
            dial = (dial + inc)%100
        if direction == 'L':
            dial = (dial - inc)%100
        
        if dial == 0:
            password = password+1

    print(password)


part2(lines)
