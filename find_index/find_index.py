def find_subtring(string:str, substring:str) -> int:
    # return string.find(substring) # that would be nice =)

    sub_len = len(substring)

    for pos in range(len(string) - sub_len + 1):
        break_flag = False
        for cur in range(sub_len):
            if string[pos + cur] != substring[cur]:
                break_flag = True
                break
        if not break_flag:
            return pos
    return -1


assert find_subtring('sadbutsad', 'sad') == 0 # beginning position
assert find_subtring('sedbutsad', 'sad') == 6 # end possition
assert find_subtring('sadbutsad', 'but') == 3 # middle position
assert find_subtring('leetcode', 'leeto') == -1 # not found
