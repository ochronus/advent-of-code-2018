ids = [l.strip() for l in open("input.txt").readlines()]

no_of_twos = 0
no_of_threes = 0

for id in ids:
    has_two = False
    has_three = False
    unique_chars = set(id)

    for char in unique_chars:
        count = id.count(char)

        if count == 2:
            has_two = True

        if count == 3:
            has_three = True

    if has_two:
        no_of_twos += 1
    if has_three:
        no_of_threes += 1

print(no_of_twos * no_of_threes)

#  ---------  PART 2

for id1 in ids:
    for id2 in ids:
        diff = [char1 for char1, char2 in zip(id1, id2) if char1 == char2]
        if len(id2) - len(diff) == 1:
            print("".join(diff))
            break
    else:
        continue
    break
