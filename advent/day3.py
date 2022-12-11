import re


def halfsies(input: str) -> str:
    result = 0
    for line in input.splitlines():
        half_idx = int(len(line)/2)
        [first_half, second_half] = line[:half_idx], line[half_idx:]
        error_item = [c for c in second_half if c in first_half][0]
        # print('error item:', error_item)
        if re.match(r'[a-z]', error_item):
            result += ord(error_item) - 97 + 1 # ord('a') == 97
        elif re.match(r'[A-Z]', error_item):
            result += ord(error_item) - 65 + 27 # ord('A') == 65
        else:
            raise ValueError('invalid error_item: ', error_item) 
    return result
