def longest_common_prefix(string_list:list) -> str:
    shortest_string = min(string_list, key=len)
    shortest_string_len = len(shortest_string)
    
    for pos in range(shortest_string_len):
        if not all(map(lambda x : x[pos] == shortest_string[pos], string_list)):
            return shortest_string[:pos]
    return shortest_string


assert longest_common_prefix(['flower', 'flow', 'flight']) == 'fl'
assert longest_common_prefix(['abc', 'ab', 'a']) == 'a'
assert longest_common_prefix(['flower', 'flow', 'flowcontrol']) == 'flow'
assert longest_common_prefix(['jam', 'jammy', 'jammmieee']) == 'jam'
assert longest_common_prefix(['dog', 'racecar', 'car']) == ''
assert longest_common_prefix(["a","b"]) == ''
