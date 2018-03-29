def random_pieces(random):
    index = random.randrange(0, 960)
    return fixed_pieces(index)


def fixed_pieces(index):
    empty_squares = list(range(8))

    hints = []
    for p in [4, 4, 20, 3]:
        hints = hints + [index % p]
        index = index // p

    first_bishop_hint = hints[0]
    positions = [2 * first_bishop_hint]

    empty_squares.remove(positions[0])

    second_bishop_hint = hints[1]
    positions = positions + [2 * second_bishop_hint + 1]

    empty_squares.remove(positions[1])

    # http://bridge.thomasoandrews.com/impossible/algorithm.html
    import itertools
    rkr = list(itertools.combinations(range(6), 3))[hints[2]]

    for p in rkr:
        positions = positions + [empty_squares[p]]

    empty_squares.remove(positions[2])
    empty_squares.remove(positions[3])
    empty_squares.remove(positions[4])

    positions = positions + [empty_squares[hints[3]]]
    empty_squares.remove(positions[5])

    positions = positions + empty_squares

    piece_names = "BBRKRQNN"

    crnt_row = ""
    for p in range(8):
        crnt_piece = positions.index(p)
        crnt_row = crnt_row + piece_names[crnt_piece]

    # Mirror World
    return crnt_row[::-1]
