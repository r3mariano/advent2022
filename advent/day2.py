from dataclasses import dataclass

@dataclass
class _Rule:
    beats: str
    equal: str
    innate_score: int

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

# this is really dumb, but it's fast!
_rps2_lookup = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7,
}

def rps2(input: str) -> int:
    """
    - Rock is A, and 1
    - Paper is B, and 2
    - Scissors is C, and 3
    - X means you should lose
    - Y means it should be a draw
    - Z means you should win
    """
    total = 0
    for line in input.split('\n'):
        if line == '':
            continue
        total += _rps2_lookup[line]
    return total

t=lambda i:sum(int('312456897'[ord(l[0])+ord(l[2])*3-329])for l in i.split('\n'))
