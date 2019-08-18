def pat1():
    # Pattern 1,4,7, 10,13

    cnt = 0
    while cnt < 10:
        print(1+3*cnt)
        cnt=cnt+1

def pat2():
    # pattern 3,4,6,9,13

    start = 3
    cnt = 0
    while cnt <= 8:
        print(start)
        cnt = cnt + 1
        start = start + cnt
        

def pat3():
    # pattern;3,4,6,7,9

    start = 3
    cnt = 1
    while start <= 20:
        print(start)
        start += cnt
        if cnt == 1:
            cnt = 2
        else:
            cnt = 1

def pat4():
    # pattern 1 4 3 6 5 8

    start = 1
    cnt = 3
    while start <= 19:
        print(start)
        start +=cnt
        if cnt == 3:
            cnt = -1
        else:
            cnt = 3


# main program
option = int(input('Enter (1,2,3,4) : '))
if option == 1:
    pat1()
elif option == 2:
    pat2()
elif option == 3:
    pat3()
elif option == 4:
    pat4()
else:
    print('INVALID CHOICE!!!!!!')