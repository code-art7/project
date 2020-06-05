

l = [1,2,3,2,3,4,2,7,6]
for team in [ele for ind, ele in enumerate(l,1) if ele not in l[ind:]]:
    count = 0
    for ele in l:
        if team == ele:
            count += 1
    print("{} {}".format(team,count))
    count = 0