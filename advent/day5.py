import re


"""
Approach:
1. We can divide the sample input into two by checking for two newlines.
2. For the initial crate positions, parse some stacks. Assuming single-char boxes, we can 
    check the index of each alpha char to determine its bay.
3. The second half is a list of instructions...

Sample input:
    [D]    
[N] [C]    
[Z] [M] [P]
1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

def crate9000(input: str) -> str:
    [positions, instructions] = input.split('\n\n')

    bays = _bays(positions)

    for line in instructions.splitlines():
        inst_match = re.match(r'move (\d*) from (\d*) to (\d*)', line)
        if inst_match is None:
            continue
        num_crates, from_bay_str, to_bay_str = inst_match.group(1, 2, 3)
        for _ in range(int(num_crates)):
            crate = bays[int(from_bay_str) - 1].pop()
            bays[int(to_bay_str) - 1].append(crate)

    bay_numbers = list(bays.keys())
    bay_numbers.sort()
    return ''.join([bays[bay].pop() for bay in bay_numbers])

def crate9001(input: str) -> str:
    [positions, instructions] = input.split('\n\n')

    bays = _bays(positions)

    for line in instructions.splitlines():
        inst_match = re.match(r'move (\d*) from (\d*) to (\d*)', line)
        if inst_match is None:
            continue
        num_crates, from_bay_str, to_bay_str = inst_match.group(1, 2, 3)
        from_bay: list = bays[int(from_bay_str) - 1]
        crates = from_bay[len(from_bay) - int(num_crates):]
        bays[int(from_bay_str) - 1] = from_bay[:len(from_bay) - int(num_crates)]
        bays[int(to_bay_str) - 1] = bays[int(to_bay_str) - 1] + (crates)
        # print(bays)

    bay_numbers = list(bays.keys())
    bay_numbers.sort()
    return ''.join([bays[bay].pop() for bay in bay_numbers])

def _bays(positions: str) -> dict:
    bays = dict()
    pos_input = positions.splitlines()
    pos_input.reverse()
    for line in pos_input:
        for crate_match in re.finditer(r'([A-Z])', line):
            bay = int((crate_match.start(1) - 1) / 4)
            if bay not in bays:
                bays[bay] = []
            bays[bay].append(crate_match.group(1))
    return bays
