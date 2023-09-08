s = ['l','e','e','t']
lt = ['a','e','i','o','u']
n = len(s)
i = 0

while i < n:
    if s[i] in lt:
        del s[i]
        n = n-1
    i+=1
print(s)