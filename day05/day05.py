import string


def part1(polymer, polarity_pairs):
    prev_len = len(polymer) + 1
    while(len(polymer) < prev_len):     # stop when there were no more reductions
        prev_len = len(polymer)
        for m in polarity_pairs:
            polymer = polymer.replace(m, "")
    return len(polymer)


polymer = open("input.txt").read().strip()

polarity_pairs = [(x + x.upper()) for x in string.ascii_lowercase] + \
    [(x.upper() + x) for x in string.ascii_lowercase]

result = part1(polymer, polarity_pairs)

print(result)

for char in string.ascii_lowercase:
    temp = polymer.replace(char, "").replace(char.upper(), "")
    result = min(result, part1(temp, polarity_pairs))

print(result)
