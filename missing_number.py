"""
Problem Explanation:

You are given an array that contains n-1 distinct numbers. These numbers are chosen from the range 1 to n, where 
n is the total number of elements you expect. Since there is one missing number, the array contains every number 
from the range except one.

For example, if n = 6, the complete set of numbers would be: [1, 2, 3, 4, 5, 6]
If the array contains the numbers: [1, 2, 3, 5, 6]
Then the missing number is 4.

"""


# 1st Approch

def find_missing_number(n, arr):
    total_sum = n * (n + 1) // 2 
    arr_sum = sum(arr)  
    return total_sum - arr_sum 
n = int(input("Enter the value of n: "))
arr = list(map(int, input(f"Enter {n-1} numbers separated by space: ").split()))

missing_number = find_missing_number(n, arr)
print(f"The missing number is: {missing_number}")



# 2nd Approch

num=int(input("Enter The Number of elements:"))
arr=[]
for i in range(num-1):
    ele = int(input(f"Enter {i+1}th element: "))
    arr.append(ele)

for i in range(num-1):
    if arr[i] != i+1:
        missingNo=i+1
        break
    else:
        missingNo=num
print("Missing number is:",missingNo)
