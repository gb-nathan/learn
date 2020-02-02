lst = [1,2,343,55, 5,66, 6]
for x in lst:
    if (x%2==0):
        print (x)
    else:
        print (x+1)
        
for cnt in range(1,10):
    print (cnt)

colors = ["blue", "red", "green"]
for color in colors:
    print (color)
    print (colors)

for index in range(0,3):
    print(colors[index])
    
for index in range(0,len(colors)):
    print(colors[index])

print("end")
index=0
while(index < len(colors)):
    print (colors[index])
    index += 1

val = "i am guru"
#print (val)

for x in val:
    if (x=="a"):
        print (x)