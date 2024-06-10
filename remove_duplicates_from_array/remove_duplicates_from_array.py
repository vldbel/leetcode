def remove_duplicates(nums:list) -> tuple:
    for pos in range(1, len(nums) - 1):
        for car in range(1, len(nums) - 1):
            if nums[car-1] == nums[car] and nums[car] != nums[car+1]:
                nums[car] = nums[car+1]
    unique_nums = len(set(nums))
    return unique_nums, nums[:unique_nums] 
    
    # not happy with that solution
    # It is not clear from description if I can use additional "arrays" to store data to reduce itrations count.        

assert remove_duplicates([1, 1, 2]) == (2, [1, 2])
assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == (5, [0, 1, 2, 3, 4])
