nums =   [10,9,2,5,3,7]


def get_max(nums):
    n = len(nums)
    dp = [1] * n

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                print(dp)

if __name__ == "__main__":
    ans = get_max(nums)
    print(ans)