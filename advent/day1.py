def top_cals(input: str, top_n: int) -> int: 
    elves_cals = []
    curr_cals = 0
    for line in input.split('\n'):
        value = line.strip()
        # assume a new line at the end
        # print('value = {}'.format(value))
        if value == '':
            if curr_cals > 0:
                elves_cals.append(curr_cals)
            curr_cals = 0
        else:
            curr_cals += int(value)
            # print('curr_cals = {}'.format(curr_cals))
    elves_cals.sort(reverse=True)
    return sum(elves_cals[:top_n])

def most_cals(input: str) -> int: return top_cals(input, 1)
