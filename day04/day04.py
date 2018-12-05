from collections import defaultdict


lines = sorted(open("input.txt").readlines())

guard_sleep_map = defaultdict(lambda: [0 for x in range(60)])

for line in lines:
    event_minute = int(line[15:17])
    if line[19] == "G":		                # guard noticed
        guard_id = int(line.split()[3].split('#')[1])
    if line[19] == "f":                     # guard falls asleep
        sleep_start = event_minute
    if line[19] == "w":  					# guard wakes up
        sleep_end = event_minute
        for minute in range(sleep_start, sleep_end):
            guard_sleep_map[guard_id][minute] += 1


def print_result(guard, guard_sleep_map):
    minutes = guard_sleep_map[guard]
    minute = minutes.index(max(minutes))
    print(guard * minute)


# part 1
print_result(sorted(guard_sleep_map.keys(), key=lambda g: -sum(guard_sleep_map[g]))[0], guard_sleep_map)

# part 2
print_result(sorted(guard_sleep_map.keys(), key=lambda g: -max(guard_sleep_map[g]))[0], guard_sleep_map)
