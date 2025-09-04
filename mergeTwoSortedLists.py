def mergeSortedLists(list1, list2):
    i = j = 0
    merged = []

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Append any leftovers
    if i < len(list1):
        merged.extend(list1[i:])
    if j < len(list2):
        merged.extend(list2[j:])

    return merged

# Test
list1 = [1,2,4]
list2 = [1,3,4]
print(mergeSortedLists(list1, list2))  
