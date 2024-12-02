inputfilepath = r".\input2.txt"

failureslist = []

with open(inputfilepath, 'r', encoding='utf-8') as reports:
    counter= 0
    for report in reports:
        levels = report.split()
        reportresult = True
        changes = []
        for i in range(0,len(levels)-1):
            changes.append(int(levels[i])-int(levels[i+1]))

        Inc=False
        Dec=False
        Result=False
        for change in changes:
            if change == 0:
                Result = False
                break
            elif change < 0:
                Dec=True
                Result=True
            elif change > 0:
                Inc = True
                Result=True
            if Inc and Dec:
                Result = False
                break
            if abs(change)>3:
                Result=False
                break
        if Result:
            counter += 1
        else:
            failureslist.append(levels)

print(counter)

# Part 2

for list in failureslist:
    for i in range(0,len(list)):
        newlist= list[:i]
        newlist= newlist + list[i+1:]
        Inc = False
        Dec = False
        Result = False
        for i in range(0, len(newlist) - 1):
            change = int(newlist[i]) - int(newlist[i + 1])
            if change == 0:
                Result = False
                break
            elif change < 0:
                Dec = True
                Result = True
            elif change > 0:
                Inc = True
                Result = True
            if Inc and Dec:
                Result = False
                break
            if abs(change) > 3:
                Result = False
                break
        if Result:
            counter += 1
            break

print(counter)







