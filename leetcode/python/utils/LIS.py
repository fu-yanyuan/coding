# Longest Increasing Subsequence
# leetcode: 300, 2407
from bisect import bisect_left

def LIS(nums):
    arr = []
    for num in nums:
        idx = bisect_left(arr, num)
        if idx == len(arr):
            arr.append(num)
            continue
        num[idx] = num
    return len(arr)
