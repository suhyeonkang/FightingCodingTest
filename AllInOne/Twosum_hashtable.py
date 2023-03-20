def twoSum(nums, target) :
    dict = {}
    for i in nums :
        dict[i] = True

    for i in nums :
        if target - i in dict :
            return True

    return False

# print(twoSum(nums=[2,7,11,15], target=9))        
# print(twoSum(nums=[3,3], target=6))
print(twoSum(nums=[3,2,4], target=6))