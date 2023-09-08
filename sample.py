a = [2, 7, 11, 15, 3, 6]
target = 9

ans = []
ans_dict = []
for i in range(len(a)):
    if target - a[i] in a:
        if i != a.index(target - a[i]):
            element = [i, a.index(target - a[i])]
            if set(element) not in ans_dict:
                ans.append(element)
                ans_dict.append(set(element))

print(ans)