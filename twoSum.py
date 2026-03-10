
def twoSum(nums,target):
    hash_table = {}
    for i, number in enumerate(nums):
       difference = target - number
       if difference in hash_table:
           return hash_table[difference], i
       else:
           hash_table[number] = i
    return
            
       
nums = [3,2,3]
target = 6

print(twoSum(nums, target))