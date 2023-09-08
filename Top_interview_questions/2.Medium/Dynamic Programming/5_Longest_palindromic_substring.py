
def longestPalindrome(s):
    dp = [[False]*len(s) for _ in range(len(s)) ]
    for i in range(len(s)):
        dp[i][i]=True
    ans=s[0]
    for j in range(len(s)):
        for i in range(j):
            if s[i]==s[j] and (dp[i+1][j-1] or j==i+1):
                dp[i][j]=True
                if j-i+1>len(ans):
                    ans=s[i:j+1]
    return ans

if __name__ == "__main__":
    s = "babad"
    result = longestPalindrome(s)
    print(result)