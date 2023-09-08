def maxSubArray(A):
    n = len(A)
    dp = [0]*n  # dp[i] means the maximum subarray ending with A[i]
    dp[0] = A[0]
    max_sum = dp[0]

    for i in range(1, n):
        if dp[i-1] > 0:
            ans = dp[i-1]
        else:
            ans = 0
        dp[i] = A[i] + ans
        max_sum = max(max_sum, dp[i])
    return max_sum

if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    ans = maxSubArray(nums)
    print(ans)