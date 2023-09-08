s = "aaabaaa"

def self_partition(s):
    def is_palindrome(sub):
        return sub == sub[::-1]

    result = []
    n = len(s)

    for i in range(1, n + 1):
        partition_1 = s[:i]
        partition_2 = s[i:]

        if is_palindrome(partition_1):
            if not partition_2:
                result.append([partition_1])
            else:
                sub_partitions = self_partition(partition_2)
                for sub_partition in sub_partitions:
                    result.append([partition_1] + sub_partition)

    return result


if __name__ == "__main__":
    s = "bb"
    ans = partition(s)
    print(ans)