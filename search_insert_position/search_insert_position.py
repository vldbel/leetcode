def search_insert_position(nums: list[int], target: int) -> int:
    el_count = len(nums)
    if nums[-1] < target:
        return el_count
    for idx in range(el_count):
        if nums[idx] >= target:
            return idx
        

assert search_insert_position([1,3,5,6], 5) == 2
assert search_insert_position([1,3,5,6], 2) == 1
assert search_insert_position([1,3,5,6], 7) == 4
