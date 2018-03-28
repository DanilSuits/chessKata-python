def random_pieces(random):
    index = random.randrange(0,960)
    return fixed_pieces(index)

def fixed_pieces(index):
    if index < 2:
        if 1 == index:
            return "RBB" + "KRQNN"
        return positions2PieceNames([0,1,2] + [3,4,5,6,7])
    else:
        return fixed_pieces(0)

def positions2PieceNames(positions):

    pieceNames = "BBRKRQNN"

    crntRow = ""
    for p in range(8):
        crntPiece = positions.index(p)
        crntRow = crntRow + pieceNames[ crntPiece ]

    return crntRow
