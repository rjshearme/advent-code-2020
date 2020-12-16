import re

def apply_mask_v1(mask, value):
    edited_value = list(bin(value)[2:].rjust(36, "0"))
    for i, m in enumerate(mask):
        if m == "X":
            continue
        edited_value[i] = m
    return edited_value

def apply_mask_v2(mask, value):
    edited_value = list(bin(value)[2:].rjust(36, "0"))
    for i, m in enumerate(mask):
        if m == "0":
            continue
        edited_value[i] = m
    return edited_value

def write_to_memory_v2(memory, loc, val):
    locations = []
    for bit in loc:


def part1(data):
    memory_storage = {}
    mask = None
    for line in data:
        if line.startswith("mask"):
            mask = line[7:]
        else:
            loc = re.search(r"(\[)([0-9]+)\]", line).group(2)
            val = re.search(r"(?<= \= )\d+", line).group(0)

            print(mask, loc, val)
            memory_storage[int(loc)] = apply_mask_v1(mask, int(val))

    total = 0
    for v in memory_storage.values():
        total += int("".join(v), 2)

    return total

def part2(data):
    pass

with open("input.txt") as fh:
    data = fh.read().split("\n")

print(part2(data))