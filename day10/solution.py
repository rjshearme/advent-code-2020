
with open("input.txt") as fh:
    data = [int(line) for line in fh.read().split()]


adapters = sorted(data)

solutions = {0:1}
for adapterJoltage in adapters:
    solutions[adapterJoltage] = 0
    if adapterJoltage - 1 in solutions:
        solutions[adapterJoltage] += solutions[adapterJoltage-1]
    if adapterJoltage - 2 in solutions:
        solutions[adapterJoltage] += solutions[adapterJoltage-2]
    if adapterJoltage - 3 in solutions:
        solutions[adapterJoltage] += solutions[adapterJoltage-3]

print(solutions[max(adapters)])