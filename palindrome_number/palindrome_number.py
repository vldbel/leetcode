def palindrome_num_check(num: int) -> bool:
    str_num = str(num)
    for idx in range(len(str_num) // 2):
        if str_num[idx] != str_num[-1 - idx]:
            return False
    return True


assert palindrome_num_check(121) == True
assert palindrome_num_check(123454321) == True
assert palindrome_num_check(12344321) == True
assert palindrome_num_check(-121) == False
assert palindrome_num_check(10) == False
assert palindrome_num_check(101) == True
