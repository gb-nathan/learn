numbers = int(input("Until what number would you like to print: "))
for n in range(1, numbers+1):
    print(n)

str1= " "
for n in range (numbers,0,-1):
    str1 = str1 + str(n)
for n in range (2,numbers+1):
    str1 = str1 + str(n)

print(str1)
