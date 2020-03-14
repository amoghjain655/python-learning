num = int(input('Enter number of stars: '))
space = int(num / 2)   +1
star = 1
loop = round(num/2)
for i in range(1 , loop):
    print(''.rjust(space,' ')+''.rjust(star,'*'))
    space = space - 1
    star = star + 2
for i in range(loop):
    print(''.rjust(space, ' ') + ''.rjust(star, '*'))
    space = space + 1
    star = star - 2yu