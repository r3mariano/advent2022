def top_cals(input: str, top_n: int) -> int: 
    max_cals = 0
    curr_cals = 0
    for line in input.split('\n'):
        value = line.strip()
        # assume a new line at the end
        # print('value = {}'.format(value))
        if value == '':
            if curr_cals > max_cals:
                max_cals = curr_cals
                # print('max_cals = {}'.format(max_cals)) 
            curr_cals = 0
        else:
            curr_cals += int(value)
            # print('curr_cals = {}'.format(curr_cals))
    return max_cals

def most_cals(input: str) -> int: top_cals(input, 1)
