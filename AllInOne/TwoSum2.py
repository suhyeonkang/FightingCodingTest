def twoSum(nums, target) :
    L = 0
    R = len(nums) - 1
    nums.sort()

    while L < R :
        if(nums[L] + nums[R] == target):
            return True
        elif(nums[L] + nums[R] > target):
            R -= 1
        elif(nums[L] + nums[R] < target):
            L += 1

    return False

print(twoSum(nums=[3 ,3 ], target=6))            
