import sys
sys.set_int_max_str_digits(0)


def fib(n):
    # Sinple recursion
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)


################################################

def calcu_me(n,dp):
    # Memoized approach
    if n==0 or n==1:
        return n
    if dp[n]!=-1:
        return dp[n]
    dp[n] = calcu_me(n-1,dp) + calcu_me(n-2,dp)
    return dp[n]

def fib_me(n):
    dp = [-1 for _ in range(n+1)]
    return calcu_me(n,dp)

#####################################################


def fib_tab(n):
    # tabulted approach 
    if n == 0 or n == 1:
        return n
    
    dp = [0 for _ in range(n+1)]
    dp[0] = 0 # no need for this line
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


#####################################################

def fib_sp(n):
    if n == 0 or n == 1:
        return n
    prev = 0
    curr = 1
    for _ in range(2,n+1):
        res = prev + curr
        prev = curr
        curr = res
    return curr

# n = int(input("Enter n to compute: "))
# print(fib(n),fib_me(n),fib_tab(n),fib_sp(n),sep="\n")
# print(fib_me(n),fib_tab(n),fib_sp(n),sep="\n")
# print(fib_tab(n),fib_sp(n),sep="\n")
# print(fib_sp(n),sep="\n")

def compute(i,j):
    if i==0 and j==0:
        return 1
    if i<0 or j<0:
        return 0
    up = compute(i-1,j)
    left = compute(i,j-1)
    return up + left

def tabu(i,j):
    i = i+1
    j = j+1
    dp = [[0 for _ in range(j)] for _ in range(i)]
    for row in range(i):
        for col in range(j):
            if row == 0  and col == 0:
                dp[0][0] = 1
                continue
            up = dp[row-1][col]
            left = dp[row][col-1]
            dp[row][col] =  up + left
    return dp[i-1][j-1]

def space_op(i,j):
    i = i+1
    j = j+1
    prev = [0 for _ in range(j)] 
    for row in range(i):
        curr = [0 for _ in range(j)] 
        for col in range(j):
            if row == 0  and col == 0:
                curr[0] = 1
                continue
            up = prev[col]
            left = curr[col-1]
            curr[col] =  up + left
        prev = curr
    return prev[j-1]

def space_op2(i, j):
    i = i + 1
    j = j + 1
    row_vals = [0 for _ in range(j)]
    row_vals[0] = 1  # Initialize the first value to 1
    for _ in range(i):
        for col in range(1, j):
            row_vals[col] += row_vals[col - 1]
    return row_vals[-1]

# i, j = int(input("Enter i: ")),int(input("Enter j: "))
i,j = 1_000,1_000
# print(compute(i,j),tabu(i,j),space_op(i,j),sep="\n")
# print(tabu(i,j),space_op(i,j),sep="\n")
print(space_op(i,j) == space_op2(i,j),sep="\n")


