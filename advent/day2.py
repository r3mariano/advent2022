class _Rule:
    def __init__(self, beats, equal, innate_score):
        self.beats: str = beats
        self.equal: str = equal
        self.innate_score: int = innate_score

_rps_rules = {
    'X': _Rule(beats='C', equal='A', innate_score=1),
    'Y': _Rule(beats='A', equal='B', innate_score=2),
    'Z': _Rule(beats='B', equal='C', innate_score=3),
}

def rps(input: str) -> int:
    """
    - Rock is A, X, and 1
    - Paper is B, Y, and 2
    - Scissors is C, Z, and 3
    """
    total = 0
    for line in input.split('\n'):
        if line == '':
            continue
        [opponent, you] = line.split(' ')
        rule = _rps_rules[you]
        total += rule.innate_score
        if rule.equal == opponent:
            total += 3
        elif rule.beats == opponent:
            total += 6
        else:
            total += 0
    return total
