def pascal_triangle():
    row = [1]
    while True:
        yield from row
        row = [sum(i) for i in zip(row + [0], [0] + row)]
