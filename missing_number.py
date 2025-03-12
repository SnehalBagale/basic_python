def find_missing_number(n, arr):
    total_sum = n * (n + 1) // 2 
    arr_sum = sum(arr)  
    return total_sum - arr_sum 
n = int(input("Enter the value of n: "))
arr = list(map(int, input(f"Enter {n-1} numbers separated by space: ").split()))

missing_number = find_missing_number(n, arr)
print(f"The missing number is: {missing_number}")
