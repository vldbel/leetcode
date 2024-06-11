def two_nums(nums: list, target: int) -> list:
    valid_nums = {}
    for idx, num in enumerate(nums):
        if num + 1 > target:
            continue
        if target - num in valid_nums:
            return [valid_nums[target - num], idx]
        valid_nums[num] = idx
# complexity: O(n), size: O(n) 

assert two_nums([2, 7, 11, 15, 16, 28, 12, 6, 2 , 1], 21) == [3, 7]
assert two_nums([2, 7, 11, 15], 9) == [0, 1]
assert two_nums([3, 2, 4], 6) == [1, 2]
assert two_nums([3, 3], 6) == [0, 1]
