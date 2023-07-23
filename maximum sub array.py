def maximum(arr, n, b):
    max = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += arr[j]
            if sum <= b and sum > max:
                max = sum
    return max

n = int(input())
arr = list(map(int, input().split()))
b = int(input())
value = maximum(arr, n, b)
print(value)
