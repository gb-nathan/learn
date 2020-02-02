#upto 10 find primenumber
primeNum = []
for number in range(2, 200):
    for x in range(2, number):
        if ((number % x) == 0 and number != x):
            break
    else:
        primeNum.append(number)

print(primeNum)
