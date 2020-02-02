rows = [1,2,3]
cols = [1,2,3]
table=[rows,cols]
for row in rows:
    for col in cols:
        if row == 2 and col == 3:
            print("i am in row "+str(row)+" and col "+str(col))