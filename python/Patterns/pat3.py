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
