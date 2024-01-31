def divide(level: int):
    if level % 2 == 0:
        half = int(level / 2)
        return (half, half)
    else:
        half = int((level - 1) / 2)
        return (half + 1, half)
