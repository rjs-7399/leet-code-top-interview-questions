s = "leetcodel"

def first_unique_char(s):
    from collections import Counter
    dict = Counter(s)

    for i in range(len(s)):
        if dict[s[i]] == 1:
            return i

ans = first_unique_char(s)
print(ans)