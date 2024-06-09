def longest_common_prefix(string_list:list) -> str:
    shortest_string = min(string_list, key=len)
    shortest_string_len = len(shortest_string)
    
    for pos in range(shortest_string_len):
        if not (all(map(lambda x : x.startswith(shortest_string[:pos+1]), string_list))):
            return shortest_string[:pos]
    return shortest_string[:pos+1]


assert longest_common_prefix(['flower', 'flow', 'flight']) == 'fl'
assert longest_common_prefix(['abc', 'ab', 'a']) == 'a'
assert longest_common_prefix(['flower', 'flow', 'flowcontrol']) == 'flow'
assert longest_common_prefix(['jam', 'jammy', 'jammmieee']) == 'jam'
assert longest_common_prefix(['dog', 'racecar', 'car']) == ''
