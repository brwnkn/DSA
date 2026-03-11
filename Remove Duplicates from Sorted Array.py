

def removeDuplicates(nums):
    expectedNums = []
    for i in range(len(nums)):
        if nums[i] not in expectedNums:
            expectedNums.append(nums[i])
    k = len(expectedNums)
    for i in range(k):
        nums[i] = expectedNums[i]
    return nums, k

nums = [1,1,2]  

print(removeDuplicates(nums))