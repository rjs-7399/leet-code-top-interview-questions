def get_majority(nums):
    from collections import Counter

    mydict = Counter(nums)
    max_occurence = max(mydict.values())
    print(max_occurence)
    ans = None
    for key, val in mydict.items():
        if val == max_occurence:
            ans = key
    return ans

print(get_majority([2, 2, 1, 1, 1, 2, 2]))