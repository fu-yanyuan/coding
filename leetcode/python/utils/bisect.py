def bisect_left(arr, target):
    '''
    return i, arr[:i] < target <= arr[i:]   <=>  find a i, that arr[i] is the first element that >= target
    for this i, arr[i] >= target, 
    so if arr[m] < target, m is not the ans, so l = m + 1
    but if arr[m] >= target, we cannot exclude m
    '''
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2
        if target > arr[m]:
            l = m + 1
        else:
            r = m
    return l

def bisect_right(arr, target):
    '''
    return i, arr[:i] <= target < arr[i:]  <=> find a i, that arr[i] is the first element that > target
    for this i, arr[i] > target
    so if arr[m] <= target, i > m => we should find in the range [m+1, r]
    elif arr[m] > target, i is in the range [l, m]
    '''
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2
        if target < arr[m]:
            r = m
        else:
            l = m + 1
    return l

def bisect_left_with_f(arr, target, f):
    '''
    arr[:i] < target <= arr[i:]
    '''
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2
        if target > f(arr[m]):
            l = m + 1
        else:
            r = m
    return l

def bisect_right_with_f(arr, target, f):
    '''
    arr[:i] <= target < arr[i:]
    '''
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2 
        if target < f(arr[m]):
            r = m
        else:
            l = m + 1
    return l


# arr = [1,1,1,0,0,0]
# find the i s.t. arr[i] is the first 0
# 1 = arr[:i] < target(0) <= arr[i:] = 0
def bisect_condition_left(arr, condition):
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2
        if condition[m] == 1:
            l = m + 1
        else:
            r = m
    return l

# arr = [1,1,1,0,0,0]
# find the i s.t. arr[i] is the first 0
# 1 = arr[:i] <= target(1) < arr[i:] = 0
def bisect_condition_right(arr, condition):
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2
        if condition[m] == 1:
            l = m + 1
        else:
            r = m
    return l