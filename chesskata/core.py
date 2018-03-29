def random_pieces(random):
    index = random.randrange(0,960)
    return fixed_pieces(index)

def fixed_pieces(index):
    if index < 17:
        empty_squares = list(range(8))

        hints = []
        for p in [4, 4, 20]:
            hints = hints + [ index % p ]
            index = index // p

        first_bishop_hint = hints[0]
        second_bishop_hint = hints[1]

        positions = [2 * first_bishop_hint, 2 * second_bishop_hint + 1]

        for p in positions:
            empty_squares.remove(p)

        if hints[2] == 1:
            positions = positions + [empty_squares[0]]
            positions = positions + [empty_squares[1]]
            positions = positions + [empty_squares[3]]

            empty_squares.remove(positions[2])
            empty_squares.remove(positions[3])
            empty_squares.remove(positions[4])


        positions = positions + empty_squares

        pieceNames = "BBRKRQNN"

        crntRow = ""
        for p in range(8):
            crntPiece = positions.index(p)
            crntRow = crntRow + pieceNames[ crntPiece ]

        return crntRow

    else:
        return fixed_pieces(0)
    