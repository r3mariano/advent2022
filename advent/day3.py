import re


def halfsies(input: str) -> int:
    result = 0
    for line in input.splitlines():
        half_idx = int(len(line)/2)
        [first_half, second_half] = line[:half_idx], line[half_idx:]
        error_item = [c for c in second_half if c in first_half][0]
        # print('error item:', error_item)
        result += _priority(error_item)
    return result

def _priority(item: str) -> int:
    if re.match(r'[a-z]', item):
            return ord(item) - 97 + 1 # ord('a') == 97
    elif re.match(r'[A-Z]', item):
        return ord(item) - 65 + 27 # ord('A') == 65
    else:
        raise ValueError('invalid item: ', item) 

def threesies(input: str) -> int:
    result = 0
    lines = input.splitlines()
    for i in range(0, len(lines), 3):
        badge = [c for c in lines[i] if c in lines[i+1] and c in lines[i+2]][0]
        # print('badge: ', badge)
        result += _priority(badge)
    return result
