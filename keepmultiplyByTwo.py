def keepmultiplyByTwo(lst, original):
    nums = set(lst)   
    while original in nums:
        original *= 2
    return original

# Test
lst = [2,7,9]
original = 4
print(keepmultiplyByTwo(lst, original)) 
