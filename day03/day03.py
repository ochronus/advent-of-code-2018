from collections import defaultdict


def parse_line(line):
    id, _, offset, dimension = line.strip().split()
    id = id[1:]
    delta_left, delta_top = offset[:-1].split(",")
    width, height = dimension.split("x")
    return id, int(delta_left), int(delta_top), int(width), int(height)


def solve(lines):
    data = [parse_line(line) for line in lines]
    overlaps = defaultdict(int)
    for _, left, top, width, height in data:
        for i in range(width):
            for j in range(height):
                overlaps[(i + left, j + top)] += 1

    total = sum(i > 1 for i in overlaps.values())
    print(total)

    for id, left, top, width, height in data:
        has_no_overlap = True
        for i in range(width):
            for j in range(height):
                if overlaps[(i + left, j + top)] != 1:
                    has_no_overlap = False
                    break
            else:
                continue
        if has_no_overlap:
            print(id)
            break


solve(open("input.txt").readlines())
