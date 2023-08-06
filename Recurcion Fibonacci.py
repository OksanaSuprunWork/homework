def GetFibonacciList(n, list):
    count = len(list)
    if len(list) < 2:
        return []
    num1 = list[count - 2]
    num2 = list[count - 1]
    if (num1 + num2) < n:
        list = list + [num1 + num2]
        return GetFibonacciList(n, list)
    else:
        return list
recursFibon = GetFibonacciList(5000, [0, 1])
print("Recursion Fibonacci = ", recursFibon)