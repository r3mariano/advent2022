from advent.day17 import rocktris

def test_sample_input():
    assert rocktris(sample_input) == 3068

def test_puzzle_input():
    assert rocktris(puzzle_input) == 2020

sample_input = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
puzzle_input = "><<<><><<<>>><<<>>>><<<<>><<<>><<<<>>><<<><<<>><>><<><<>>><<>><<<<>>>><<<<>><<<<>><<<><>>>><>>><<>>>><>><><<<>><<<<>>><<<<>><<><<>><<><>><<<<>>><<>>><>>><<><>>>><<>><<>>>><<>>>><><<><>>><<>>><<<<><<<>><<<>>><<>>><<<>><><>><>>><<<><<<>>>><<<<><>>><<<>><<<>>>><<<<>>><<><>><<<<><><<<>>>><<<<>>>><<>><<<>>>><<<<>><><><<>><<<<>>>><<><<<<>>>><<<<>>>><<<>><<<<>><<>>>><<>>><>><<>>>><><<<>>>><<<><<<<>>><<<<>>>><<<<>>>><<>>><<<<>><><>><>>><>>>><<<<>>>><>>><<>><<<<>><<>>><<<>>><<>>>><<><<<<><<<<><<<<>><<<>><<<>>>><>><<>>><>>>><>><<><<><>>><<<>>>><<<>><<><<<>>><>><<<<>>><<>><<<>><<<<>><<<<><>><><>>>><>><<><<>><>>><><>>>><<>><<<<>>>><<<<>><<<>>>><<<<>>><<<>><<<>>><<<><<><>><<<>><<<<>>><<<<>><>><<<>>><<<>>>><>><<<>><<>>><<><>><<<<>>><>><<><<>><<>>>><>><<>><<<><>>><><>>><<<<>>>><<<>><<>><<<<><>><<>>>><<>><<<<>>><<<>>>><<<><<>><>>>><<<>>><<<<>>><<<>>>><><<<<>>>><<<>>>><<<<>>><>>><>><<<<>>>><<<><<<<>>>><<>><<><<<<>>><<<<>>><><<<>><<>><<<<>><<<><<<<>>><<<><>>><<>>><><<<<><>><<<<>>>><<<<><>>><<>>><<<<><><<<<>>><<<<><<>>><<<<>>><<<>>><<<<>>>><>>><<<<>><<<><<<>><<<<>>><<<>><<<<>>><<<>><><<<<>>>><><<<>>>><<<>><<<<>><<<>>><><>>><<><><>><<>>>><<>>><>>><<<>>>><<>>>><>>>><<<<>>><<<<>><<><<>>>><<>>>><<>>><<<><<>><>>>><>>><<<<>><>>>><>>>><>>><<>>><<<<>>>><<<<>>><<>>><<<<>>><<<<>><<>>><<<<>><<<>>>><<<<>>><>><>>><<<>>><<>><<>><<<<>>>><<<>>><<<<>>><<<>>><<<><><<<<>>><<>><<<><<<<>>><><>>>><<<>><<>><<><><<<>>>><><<<<><<>><>>><<>><>>><<<<><<<<>><<>><<<<><<<<>>><<<><>><<<>><><<>>><<<<><<<<>>>><<<>><<>>><<<><<<<><<<><>>><<<<>>>><>><>><<<><<<<>><<>>>><>><<<<>>><<>>>><<<>>>><<><<><>>>><<><<<<>>><<>>>><<<>>>><<>>>><<>>>><<<<><<<><<>>>><<<>><><<<>>><<>>>><<<>>><<>>><<>>>><<<><>>>><<<<><>>>><<>>><<<><<<><<<>>>><>>>><<><<<>>>><<<<>>><<<<><<<>><<<>>>><>>>><<>>>><<<>>>><>><<>><<>>>><<<><<><<<<>>>><<<>>>><>>><<>>><<<>><<<>>>><>><<<>><<>>><<>>>><>><>><<>>>><>><<<<>>>><><<<<><<<>>>><<<<>><>>><<<>>><<<>>><>>>><<>><<<>><>><<<>>>><<>>><><<<<><<<>>><<<<><><<<<>>>><<>><<<><<>>>><<>><<>><><><<><<<>><<<<>>>><<<<><<><<<<>><>><<<><<<<><>><<>><>>><<<><><<><<<<><<<<><<>><<>>><<>>><>><<<<><<<>>>><<<>><<>>>><<<>><>>>><<<>><<>><<><<<<>>><><<<<><<<>>><<>>>><>>><>>>><<><>><<<>>><<><<<>><<><<<><<<<><>>><><<>>>><<>><<<<>>>><<>>><<<<>><<<<>>>><<<<>>>><<><<<<>><<>>><<<<>>><><>>><>>><<><<<>>><<<<>>>><><<<<>>><<<><<<<>>><<<<><<<>>><>><>><<<<>>><><<<>>>><<<>>>><>><<>>><<>>><<>><><<<<><<<<><<<>>>><<<<><>>>><>>><>>><<<<>>><<>>>><<<<>>><>>>><>>><<<<>>><<<<>>>><<>>>><<<><<>><<<><<<<><<<<><<<>>>><<>>>><<<<><<>><>>><<<<>>><<>><<<<>>><<<<>>><<<<>><<><<<<><<<<>>><>>>><<<<>>><<<>>>><>>>><<<<>>><<<<>>><<>>>><<<>>>><>><<<>><<<<>>>><<>><<<>>><<>>>><>>>><<<<>>><<<<>>>><<>>>><<<>><<<>>><<<<>><<<>>>><<<<>><<<<>>><<<<>><<<<><>>><<<>>><<<<>>><<<>>><<<<>>>><<><>>><<<<>><<<<>>>><><>>><<<><<<><<>><<<><><<<<>><<<<>>>><<>>>><<><><<>>><<<<><<>>>><<<<>>><>>><<<<>><>>>><><<<<>><<<<>>><<<>><<><>>>><<<<>>><<><<>>>><>>>><>>><<<>><>>><<<<>>><<>><<<>>>><<<<><>><><<><<<<><>>><<>><>>><<><<<>>>><<>><>>>><<<<>><<>><<<>>><<<<>><<><<<>>><<<>><<<>><>><<<<>>>><>><<>>>><<<<>>>><>>><<>>>><<<><><<<<>><<<><><<><<><<>>><<<><<<>>><<><<><<<><<<<>><>><<<><<<>>>><<<>>><>><<<>>><<<<>>><<><<>>>><<<>><<<<><<<>><<<<>>><<>>><>><<>><><<>>>><>><>>>><>>><<<><<><<<<>>><<>>>><<<><<<>><<<>>><<>>>><><<<<>>>><<<<>>>><<>>>><<>>>><<<<>>>><<<>><<>><<<>>>><<<>>><<<<>>><<<><<<<>><<<<><<<<>>><<<<>><>>>><<><<<<>><<>>><>>><<<>><<<><<<><>>>><<<<>>>><<<>><<>>>><<>>><<><<>>>><<<<><>>>><<<<>><<<>>><<<<>><<><>><><>><>>>><<><<>>><<<<>><<<>><<<<><<<>>>><<>><>>>><<<><<>><<<<>><<<><<<><<<<>>><<>>><<<>><>>><<<<>>><<<<>>><>>><<<>>><<>>><<>>>><<<<>><><<>><>>>><><<<<>>>><<<<>><<<<>><<<<>>><<>>>><<<><<>><<<<><<<<><<>><<<<>><<><<>><<>>><<<<>>>><<><<<>>><<<>>><>><<>>>><<<<>>>><<<>><<>><>>>><<>><<>>>><>>><>><<><<<<>><<<>>><<<>><>>>><<>>><<<<>>><<<>>><<<<>>>><<<>>>><<<>>>><<<<>>>><<<>><<>>><<<<>>>><<<>>><<<>>>><<<<>><>><<<>>>><>>>><<<<><<<<><<<<>>>><<<<>><<<<><<>>>><>>>><<>>>><<<<>><>>>><<<<>>><>>>><>>>><>>><<<><>>>><<<<>>>><>><<<<>><<><<><>><<<<><>>>><<<>>><<>><<<>>>><>><<<><<><<>>>><<>>>><<><><<><>>><<>>><<>>>><<<<><<>>><>>><><><<<<>><>>><<<<>>><<<<>>>><<<>>>><<<<>>><<<>><<<>>><<>><>>>><>><<>>><<<<>>>><>><<>><>>>><>>>><<<>>><>>><<<<>>><<<>>><<>>><<<><<<<>><>><<<>>>><<<>>>><<<>><<<>><<<>><>><<<>>>><<<>>><>>>><<<<>>>><<<<>>><><<<<><<<<>>><<<>>><<<><>>>><>>><><>>><<>>>><<<<>><>>>><>>>><>><<>><<><<<>><<<>>>><<>><><>><<<><<>>><<<<>>><<<>><><<<<><<<>>>><>>><<<>><>><<>><><<>>>><<<>>>><<<><<<<>><<<<>>>><>><<<>>>><<<<>><<>><<<>>><<>>><>><<<>>><>><<<>>><<<>>><><<<<>>><<<<>>><<<<><><><<<<><<>>>><><<<<><<>>>><<>>><<<>><><<<<><<<>>>><<<>><<<<>>><<<>>><<><<><>><<>>>><<<>><<<><<<<>>>><<<>>>><<<><<>>>><><<>>><<>>>><<><<<<><<>><<<<><<><<<<>>>><<<>><>>>><>>>><<>>>><>>>><>>>><<>>><>>><<<><<<<>>>><<<<><<<>><>><<>>>><>><<<<>>>><>>>><<<<><<>>><<<>><<<<>>>><<>><<<>><>>>><<>><>>><>>><><>>><<<>>>><<<<>>>><<<<>><<>><<<<><<<>><<<>>>><<>>>><<<<>>><<<>>><<>>><<<><<<>><<>>><<<<>>>><<<<>>>><<<<><>>>><<><<>><><<<<><<<>><<>>>><><<<<>><<<>>><<>>>><>>>><<<<><<<<>>><>><<<>><<<>><>>>><<>>>><<<<><>>><>>><<<>>><>><<<<>><<<<>>><<<>>><>>><>>>><<<><<>><<>><<<<>>>><<>>><<<<><>>>><<<<><<><>>>><<<<><<<<>><<<<><<<<>>><>><<><<>><>>>><<<>>>><<<<>>><<<<>>>><<<<><<>>>><<>><>>>><<>><<<<>>>><<><>>><<<<>>>><<<>>><>><>>><<>>>><<<>>>><<<>>>><>>>><<><<<>>><<<<>>>><>>><<<>>><<<<>><<<<>>><<<>><><<<<>><><<><>>><>>><<<<>><<<<><>>>><<>>>><<<>>>><>>>><<<>>>><><<<<><>><<>>>><<<<>>><<<>>><<<<>>><<>>>><<<>><<<<>>>><><<<<>>>><<<<><><<<><<<><<>>><<<>>><<><>>>><<>>><<<>>>><<<>>><>><<<><<>><<<>><<>><>><<<>>>><<<<>>><>><<>><<<<>>><<<>>><<<<>>><<<>>><>>><<>>><<><<><<<><<<<>>><<<><<<<><<<<>>>><>>><>>>><>><>>><<<>>><<>>>><<><<>>><<<>>><<><<<<><<<<>>><<<<>><<<<>>><>><><<>>>><>><<<<><<<><><<<>>><<<<>><<<<>>>><>>>><>>><<<>>><>><<<<><<<<>>>><<<<><<<><<>>><<<<>>><<<>><<<<>>>><<<>><>>><<<<><<<>><<>>>><>><>><<<<>><<<<>>><<>>>><<<<>>><>>><<<<>>>><<<<><<<<><<><<<>><>><<<>>>><<<<>><>>>><<<>>>><>>>><<><><<<<>><<<><>>>><<><<>><<>>><<><>><<<><<>>><<<>>><<<<>>><<<><<>><<<>>><<>>><<>><<<<>>>><>>>><>><<<>>>><<<><<<><<>><<<>><<>><<<>>><<<>>><>>><<<<>>>><<>><<<><<<>>>><>>>><<<>>>><><<<<><<<<>><<<<>><<<>>>><<<<>>>><<<><>>><<<><><<>><>>><<<<>><>><<<>>>><>><<<<><<<>>>><<><<<>>><<<<>>>><<<<>>><>><>>><<<><<<<><<>>>><<>>>><<<<>>>><<<<>>><<<<>>><><><<<<>><<<<><<<<>>><<<>><<<<><<<>><>>>><<<<><<<<>>><>><<>>>><<<>>>><<<<>>><<>>><<<>><<>>><<<<>><>><<<<><<<<>><<<>>><<<>><<>>><<<<>>><<<<>>>><<>>><<<>>><<<><<<>><<><>>><<<>>>><<<<>>><>><>>>><<>>><><<<>>>><<>>><<>><<>>>><<<>>><<<<>><<<<><<<><><<<>>><<<<>><<>>>><<<>>><<<>>><<>>>><<<><<<><<><<<><>>><<<>><>>><>>>><<<>>>><<<><<<>>>><<>>>><<<>><<<<>>><<>>><<<>><<<>>>><<>><>><<<<>>>><<>>><<<>>><<<>>><<<>>><<<<>>>><>><>>><>>><<<<>>><<<<>>>><>>>><<>>>><<>><>><><<<>>><<<><<<>><<<<>><<<<>><<>>><<><<<<>>><<<<>>><<><<<<><>>><<<<>><>>>><<>>><>>>><<<><>><>>>><<>><<<<>>>><<<><<>>><<<<><<<<><<<>>>><<<>><<<<><>>>><<<<><<>>>><<<>>>><<<>><>>><<<<>>>><<<>><<>>>><<<<>><<<>>><>>><<<>>><>>>><<<<>>><<<<>>><<<><<<<>>><<><<<<>>>><><<<>>><<<<><<><<<<><<<<><<<>>><<<>><<<<>><<<<>><<<>>>><<<>>>><>>><<<<>>><<<>>>><<<<>><<<<><<>>>><<<<>><>>><>>>><<<><<<><<<<>><>>>><<<<>>>><>><<<<><<>>><<><<>>><<><<<>>>><<<>>>><>>>><<<<>>><<><<<><>><<<>>><<>>><<<><<<<>><<<><<<<>><<<<>>>><<<><<<<>>>><<>><<<<><<<><<<>><<<>><>>>><<<>>><<><<<<>><<<<>>>><<<>><<<<>>><<>>><<<<>>><<>>>><<>><<><>><>>>><<<>><<<<><<<>><<<>>>><<<<>><<><<>>><<<<><<<>>>><>>>><<<>>><>><<>>><<>>><<<>><<<>><>>>><<<>>>><<<<>>><<<<>>>><<<>>>><<>>>><<><<<>>>><<>>>><<<<>>>><<<><<><<>><<<>>><<<<>>>><<<>><>>>><><<<<>>><<>>>><<<>><<<><<<<><<>>><>>><<<>>><>><<>><<><<<>>>><>>><><<<>>>><<<><>><><>>><>><>>>><<<>><<<>>>><<>>>><<>>><>>><<<><>>>><>>>><>>><<>>><<>>>><<<<><<<>>>><<<<><<>>>><<<>>><<<<><>><<<>>><<<<>>>><<<<>>>><>>>><>><<<>>><<<>><<<><<<<><<>>><>>>><<<<>>>><<<><<<>><>><>><<<>>>><>>><><>><<><<>>>><>><>>><<><<<<>>>><><>><<>>>><<<<>>><<>>>><<<><>><<>>>><<<>><<<>><<<><<<><><><<<><>>><><<<<>><<<<>>><<>><<<<>>><<>>><<>>>><<<<>><<<<>>><<<>>><<<<>>><<<>>>><<<<>>>><<<>>><<<>>><<<<><>>>><<<><>><<<>>>><<<><<<<>>>><><<><<<<>><><<<<><<<>>>><>><<<><<><<<>>>><<<<>><<<<>>><<>>>><<<><<<<><<<>>>><<>><<<<>><<>>>><<<<>><<<>>>><>>>><<>>><<>><<<>>><>><<>><<>>>><<<<>><<>><>><<<><>><<<><<>>><<<><<>><<<<>>><<>>>><<<<>>><<<<>><>>><<<><<>>><<>><<>>>><>>><<<>>>><<<<><>>>><<<>>>><<>>>><>><<>>>><<<<>><>><<<<>>>><><<><<<<>>><<<<>>>><>>><<>><>><<>><<>>><<<>>>><<>><><<<>>><<<>>>><<>>>><<<>><<<><<<>>>><<>>><<<>>>><>><<<>><<<<>>><<>>><<<><<>>>><<<>>><<>><<<><>><<>>>><<<>>>><><><<>>><<<<>><<>>><<<<><<<>>><>>>><<<>>><><>><<>>><<<<>>><><<<>>>><<>>>><<<<>>><>>>><<>>><>><<<>>>><>>>><<<>>>><<<>>><><>><<<>>>><<<>>>><>>>><<<<><<>><<<<>>><<>>>><<>>>><<<>>><<<<>>><<>>><<<<>><<<>>>><<>><<<<>>>><<<>>><>>>><<<><<<<>>>><<>>><<<<>>>><>><>>><<<>>>><>><<<<><<<<><<<>>><>><<<>>><<<<>>><<>>><><<<<>>><<<<>><<<<><<<>>>><>><<<>>>><<<>>><<>>><<<<>>><<>>>><<<>>>><<<<>>><>>><<><<<><<<<><<<>><<<<>><<>>>><><<<<>>>><<<<>><<><<<>>>><<<>>><<><<>>>><<>>><<<<>>>><><<<>><<<<><<<>><>>><<>><<<<>>>><<<<>>><<><<<<>>>><<>>><><>><<<><<<>><<<<>>><>>><<<<>>>><>><<<>>>><<<>>>><<<>><>>><<<><>><<<<>>>><<>>><>>><>><>>><<<>>>><>><<>>>><<>>>><<<<>>><<<<>><<<<>>><><<<<>>>><<<>><<<>><<<<>>><<<>>><<<>>><<<<><<<><<<<><>>>><<<<>>><<>>><>><<>><>><>><>>><<<>>>><<><>><><<<<>><<<<>><<<<>>>><>><<<>>><<<><<<>>><<><<<<>>><<<<>><>>><<<>>>><>><<><>>><<<<>>><<>><<<>>><<>>><<<>>><<<>>><<><<<>>>><<>><<><<><<>>>><<<<>>><<<>>><<<>>>><><<<><>><>><<>>><<<<>><<>>><<<<>>>><>><<<<>><<<<>>>><<<<>>><><<>>>><<<>><<<<>>><><<>>><<>>>><<<><<<>>>><<<>>><>><<>><<>><>>><<<>>><<><<>>>><<>><><<<>>>><>><<<<><<<>><><<<<><<>>><><<<>>><<>>>><<<<><>>><><<<<>>><><>>>><<>>><<>><<<>><<<<><<><<<<>>><>>><<<<>>><<>><<<<><<<<>>><<<<><<<>><<<>>><<<<>><<>>><<>>>><<<>>>><>><>><<>>>><<<>>><<>>><<<>>>><<>>>><>>><<<>>>><<<><>>><<>>>><><><<<<><>>>><<>>>><<><<><<<<>>><<>>><<><>>>><<>>>><<>>>><><<<<><<<<>><<<<><<<>>><<<><<<><>>><<<<>>>><>><<<>>><<>>><>><>>>><<><>>><<<>>>><><>><<<<>>><<<<>>>><<>><>><>>><<<>><<><<<<>>>><<<<>>>><<><>><<<>><<>><<>>><><<<<>>>><<<>>>><>>><<<<>>>><<<<>><<><><>>><<<>>>><>>><><<<><<<<><<<<>>>><<>>><<>><<<<><<>>><>>>><<<<>><<<>>>><<><<<<>><<<>>><<>>><<<><<<><<>>><>><<<<>>>><>>><>>>><<<<>><<<>>><<<>><<<"