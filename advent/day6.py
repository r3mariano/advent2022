def start_of_packet(input: str) -> int:
    return _marker(input, 4)

def start_of_message(input: str) -> int:
    return _marker(input, 14)

def _marker(input: str, num_uniq: int):
    for (i, candidate) in [(i, input[i: i + num_uniq]) for i in range(len(input) - num_uniq + 1)]:
        if len(set(candidate)) == len(candidate):
            return i + num_uniq
