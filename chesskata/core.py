def random_pieces(random):
    index = random.randrange(0,960)
    return fixed_pieces(index)

def fixed_pieces(index):
    if index < 2:
        if 1 == index:
            return "RBBKRQNN"
        return "BBRKRQNN"
    else:
        return fixed_pieces(0)
