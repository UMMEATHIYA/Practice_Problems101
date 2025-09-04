def sqrt(x):

    low = 0
    high = x//2
    if x == 0 or x == 1:
        return x
    while low <= high:
        mid = (low + high)//2
        if mid * mid == x:
            return mid 
        elif mid * mid < x:
            low = mid + 1
        else:  # mid * mid > x
            high = mid - 1

    return high # return the last stored value.

x = 8
print(sqrt(x))