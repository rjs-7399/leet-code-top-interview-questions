def longest_common_prefix(strs):
    lcp = strs[0]
    print(lcp)

    for index in range(1,len(strs)):
        i=0
        print(strs[index])
        element = strs[index]
        while element[:i] == lcp[:i] and i<=len(element):
            i += 1
        i -= 1
        lcp = element[:i]
        print(lcp)
        print("\n\n")

strs = ["flower","flower","flower"]
#strs = ["geeksforgeeks", "geeks", "geek", "geezer"]

longest_common_prefix(strs)