#Fibonacci Sequence
def fibSeq(condition):
    firstNum = 1
    second = 1
    print (firstNum)
    print(second)
    
    while (second < condition):
        third = firstNum + second
        if (third < condition):
            print(third)
        firstNum=second
        second=third

if __name__ == "__main__":
    fibSeq(10)