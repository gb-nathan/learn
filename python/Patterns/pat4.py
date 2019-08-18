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