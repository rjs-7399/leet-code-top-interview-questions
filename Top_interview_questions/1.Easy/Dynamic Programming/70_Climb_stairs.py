stairs = {}
stairs[1] = 1
stairs[2] = 2


def climb(n):
    if n in stairs:
        return stairs[n]
    else:
        stairs[n] = climb(n-1) + climb(n-2)
        return stairs[n]
print(climb(40))