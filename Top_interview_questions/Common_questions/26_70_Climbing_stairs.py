memory = {}
memory[1] = 1
memory[2] = 2

def climbStairs(n):

    if n in memory:
        return memory[n]
    else:
        memory[n] = climbStairs(n-1) + climbStairs(n-2)
        return memory[n]

x = 5
ans = climbStairs(5)
print(ans)