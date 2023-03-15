import sys

def twoSum (nums, target) :
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target :
                
                return True
            
    return False

print(twoSum( nums=[3, 3], target=6))
