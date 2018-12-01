import itertools

freq_changes = [int(n) for n in open("input.txt").readlines()]
print(sum(freq_changes))

already_seen = set([0])
freq = 0
for num in itertools.cycle(freq_changes):
    freq += num
    if freq in already_seen:
        print(freq)
        break
    already_seen.add(freq)
