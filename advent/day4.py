import re


def range_contains(input: str) -> int:
    result = 0
    for line in input.splitlines():
        a_s, a_e, b_s, b_e = map(
            lambda x: int(x), 
            re.match(r'(\d*)-(\d*),(\d*)-(\d*)', line)
                .group(1, 2, 3, 4)
        )
        a, b = range(a_s, a_e + 1), range(b_s, b_e + 1)
        # print('ranges: ', a, b)
        if (a_s in b and a_e in b) or (b_s in a and b_e in a):
            # print('yes')
            result += 1
    return result

# This is copy-paste except for the condition in line 30
def range_overlaps(input: str) -> int:
    result = 0
    for line in input.splitlines():
        a_s, a_e, b_s, b_e = map(
            lambda x: int(x), 
            re.match(r'(\d*)-(\d*),(\d*)-(\d*)', line)
                .group(1, 2, 3, 4)
        )
        a, b = range(a_s, a_e + 1), range(b_s, b_e + 1)
        # print('ranges: ', a, b)
        if (a_s in b or a_e in b) or (b_s in a or b_e in a):
            # print('yes')
            result += 1
    return result
