import math



def get_first_available_departure_time_for_bus(bus_id, departure_time):
    time_found = 0
    while time_found < departure_time:
        time_found += bus_id
    return time_found

def part1():
    with open("input.txt") as fh:
        departure_time = int(fh.readline())
        bus_ids = [int(id_) for id_ in fh.readline().split(",") if id_ != "x"]

    earliest_available_bus_time = math.inf
    output_val = 0

    for bus_id in bus_ids:
        first_time_for_bus = get_first_available_departure_time_for_bus(bus_id, departure_time)
        if first_time_for_bus < earliest_available_bus_time:
            earliest_available_bus_time = first_time_for_bus
            output_val = (earliest_available_bus_time - departure_time) * bus_id

    return output_val

def is_consecutive_dep_time(dep_time, bus_ids):
    for offset, bus_id in enumerate(bus_ids):
        if bus_id == 0:
            continue
        if (dep_time + offset) % bus_id != 0:
            return False

    return True


def part2():
    with open("input.txt") as fh:
        _ = fh.readline()
        bus_ids = [int(id_) if id_!="x" else 0 for id_ in fh.readline().split(",")]

    jump_val = max(bus_ids)
    dep_time = 0
    while not is_consecutive_dep_time(dep_time, bus_ids):
        dep_time += jump_val

    return dep_time

f = part2()
print(part2())