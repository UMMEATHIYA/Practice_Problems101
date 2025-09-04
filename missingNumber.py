def missingNumber(nums):

    n = len(nums)
    expected_sum = (n * (n + 1)/2)
    actual_sum = sum(nums)
    num = expected_sum - actual_sum
    return int(num)

nums = [3,0,1]
print(missingNumber(nums))