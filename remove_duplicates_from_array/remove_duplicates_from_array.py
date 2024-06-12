def remove_duplicates(nums:list) -> int:
    last_registered_num = nums[0] # the first element always keeps its place 
    insert_cursor = 1 # cursor to track place to insert new element 

    for looking_cursor in range(1, len(nums)):        
        current_num = nums[looking_cursor]
        
        if current_num == last_registered_num:
            continue  # num is already registered
        
        nums[insert_cursor] = current_num
        last_registered_num = current_num
        insert_cursor += 1
            
    return insert_cursor

                
assert remove_duplicates([1, 1, 2]) == 2
assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
