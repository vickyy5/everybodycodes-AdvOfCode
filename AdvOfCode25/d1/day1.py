
with open('1-1.in','r') as f:
   lines = [ line.strip() for line in f]


def part2(lines):
    dial = 50
    password=0

    for i in lines:
        direction = i[0]
        inc = int(i[1:])

        prev_dial = dial 

        t=0

        if direction == 'R':
            dial = (dial + inc)%100
            t = (prev_dial+inc)//100
        else:
            n = prev_dial - inc
            if prev_dial == 0:  # Handling edge case like the test   ->   0 - L5, -5 : it really does not pass 0, but looks like
                t = (inc//100)
            elif n < 0:
                t = (abs(n)+100)//100
            dial = (dial - inc)%100
        

        if t > 0:
            password = password + t

        if dial == 0 and t==0:
            password = password+1

        
        print(f"-> dial {prev_dial}, plusinc {dial}  times {t} and password {password}")


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
