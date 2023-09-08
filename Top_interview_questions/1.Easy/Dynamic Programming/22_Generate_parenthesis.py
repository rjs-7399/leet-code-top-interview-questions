def generateParenthesis(n):
    result = []
    def dfs(open, close, str):
        if len(str) == 2*n:
            result.append(str)
            return result
        if open < n:
            dfs(open+1, close, str + '(')
        if close < open:
            dfs(open, close+1, str + ')')

    dfs(0, 0, '')
    return result

if __name__ == "__main__":
    n = 1
    result = generateParenthesis(n)
    print(result)