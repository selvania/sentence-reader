while True:
    testcases = int(input())
    count = 0
    if testcases > (10**5):
        break
    while count <= testcases:
        inpt = input()
        countn = 0
        for x in inpt:
            if x == ' ':
                countn += 1
        if countn < 3:
            break
        a, b, c, d = inpt.split(' ')
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        if a > (10**9):
            continue
        elif b > (10**9):
            continue
        elif c > (10**9):
            continue
        elif d > (10**9):
            continue
        goal_distance = abs(a - b)
        distance = 0
        combined = abs(c + d)
        test1 = goal_distance%combined
        test2 = goal_distance - c
        if test2 == 0:
            print("yes")
            continue
        test2 = goal_distance%test2
        test3 = goal_distance - d
        if test3 == 0:
            print("yes")
            continue
        test3 = goal_distance%test3
        if test1 == 0:
            print("YES")
        elif test2 == 0:
            print("YES")
        elif test3 == 0:
            print("YES")
        else:
            print("NO")
        count += 1
    break
