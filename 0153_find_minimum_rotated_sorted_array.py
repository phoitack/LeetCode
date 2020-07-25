def findMin(nums):

    min_num = nums[0]

    for num in nums:
        if num <= min_num:
            min_num = num
            
    return min_num
    
#array = [3, 4, 5, 1, 2]
array = [2, 2, 2, 0, 1]

print(findMin(array))