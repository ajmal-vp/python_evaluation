def array_challenge(arr):
    max_profit = 0
    n = len(arr)

    for i in range(n - 1):
        for j in range(i + 1, n):
            profit = arr[j] - arr[i]
            max_profit = max(max_profit, profit)

    return max_profit

arr = [44, 30, 24, 32, 35, 30, 40, 38, 15]
print(array_challenge(arr))





