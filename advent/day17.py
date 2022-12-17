from dataclasses import dataclass


@dataclass
class Shape:
    # coords that are filled; top right is (0, 0)
    filled: 'list[complex]'

    def bottom_left(self) -> complex:
        return complex(int(min([coord.real for coord in self.filled])),
            int(max([coord.imag for coord in self.filled])))

    def offset(self, offset: complex) -> 'Shape':
        return Shape(filled=[coord + offset for coord in self.filled])

shapes = [
    Shape([0, 1, 2, 3]),
    Shape([1, 0+1j, 1+1j, 2+1j, 1+2j]),
    Shape([2, 2+1j, 0+2j, 1+2j, 2+2j]),
    Shape([0j, 1j, 2j, 3j]),
    Shape([0, 1, 0+1j, 1+1j])
]

def rocktris(input: str) -> int:
    # board will also be filled with coords of set pieces
    board = []
    peak = 0
    """
    The board is represented by negative y and x

    -y
    ^
    |
    |b......
    |ac..... 
    +---------> x

    where a = 0 + 0j, b = 0 + 1j, and c = 1 + 0j

    y = 0 is the floor.
    """
    jet_num = 0
    for shape_num in range(2022):
        shape_template = shapes[shape_num % len(shapes)]
        offset = complex(0, peak) - shape_template.bottom_left() + 2 - 3j
        upcoming_shape = shape_template.offset(offset)
        # print('upcoming: ', upcoming_shape)
        while True:
            jet = 0
            if (input[jet_num % len(input)] == '>'):
                jet = jet + 1
            else:
                jet = jet - 1
            # print(input[jet_num % len(input)], jet)
            jet_num += 1
            candidate = upcoming_shape.offset(jet)
            # Collision checks!
            # Does it hit the walls? 😏
            if sum([1 for coord in candidate.filled if coord.real < 0]) > 0:
                candidate = candidate.offset(1)
            if sum([1 for coord in candidate.filled if coord.real > 6]) > 0:
                candidate = candidate.offset(-1)
            # Does any part of the shape hit the board?
            rock_collision = [coord for coord in candidate.filled if coord in board]
            if len(rock_collision) > 0:
                # print('hit da rock sideways')
                upcoming_shape = candidate
                candidate = candidate.offset(-jet)
            # Now move it down.
            jet = 1j
            candidate = candidate.offset(jet)
            # Does any part of the shape hit the board?
            rock_collision = [coord for coord in candidate.filled if coord in board]
            if len(rock_collision) > 0:
                # print('hit da rock')
                candidate = candidate.offset(-1j)
                upcoming_shape = candidate
                break
            # Does it hit the floor?
            if sum([1 for coord in candidate.filled if coord.imag > 0]) > 0:
                # print('hit da floor')
                candidate = candidate.offset(-1j)
                upcoming_shape = candidate
                break
            upcoming_shape = candidate
        # Ossify the shape.
        # print('ossifying: ', upcoming_shape)
        board = board + upcoming_shape.filled
        peak = int(min([coord.imag for coord in board])) - 1
        # print(board, peak)
    return abs(peak)

# sample_input = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
# print(rocktris(sample_input))
