hippos = 0
answer = "y"
while answer == "y":
    hippos = hippos + 1
    if hippos == 1:
        print(str(hippos) + " balancing hippo!")
    else:
        print(str(hippos) + " balancing hippos!")
    answer = input("Add another hippo? (y/n)")