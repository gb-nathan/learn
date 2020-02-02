import sys

def findStr(Str):
    cnt = 0
    for index in range(0, len(Str)):
        if Str[index] == 'i':
            print (Str[index])
            cnt = cnt + 1
    return(cnt)


if __name__ == "__main__":
    Str = '''I am this thing.ArithmeticError
            you are that thing.'''
    print(sys.argv[0])
    print(findStr(Str))
    print(Str[3:])