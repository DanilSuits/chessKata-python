def random_pieces(random):
    index = random.randrange(0,960)
    return fixed_pieces(index)

def fixed_pieces(index):
    if index < 16:
        empty_squares = list(range(8))

        first_bishop_hint = index % 4
        second_bishop_hint = index // 4

        positions = [2 * first_bishop_hint, 2 * second_bishop_hint + 1]

        for p in positions:
            empty_squares.remove(p)

        positions = positions + empty_squares

        pieceNames = "BBRKRQNN"

        crntRow = ""
        for p in range(8):
            crntPiece = positions.index(p)
            crntRow = crntRow + pieceNames[ crntPiece ]

        return crntRow

    else:
        return fixed_pieces(0)
    