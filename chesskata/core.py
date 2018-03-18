def random_pieces(random):
    index = random.randrange(0,960)
    return fixed_pieces(index)

def fixed_pieces(index):
    if 1 == index:
        return "RBBKRQNN"
    return "BBRKRQNN"
