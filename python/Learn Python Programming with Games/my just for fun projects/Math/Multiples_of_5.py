def findMultiples(start, end, increment):
    x = start
    while (x < end + 1):
        print(x)
        x = x + increment

if __name__ == "__main__":
    findMultiples(4,100,4)