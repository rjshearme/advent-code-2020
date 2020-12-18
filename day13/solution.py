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


def inverse(a: int, n: int):
    t = 0
    newt = 1
    r = n
    newr = a

    while newr != 0:
        quotient = r // newr
        (t, newt) = (newt, t - quotient * newt)
        (r, newr) = (newr, r - quotient * newr)

    if r > 1:
        raise Exception("a is not invertible")
    if t < 0:
        t += n

    return t

def chinese_remainder_theorem(bus_ids):
    m = [bus_id for bus_id in bus_ids if bus_id != "x"]
    a = [bus_id-idx for idx, bus_id in enumerate(bus_ids) if bus_id != "x"]

    M = 1
    for v in m:
        M *= v
    Mi = [M // m[i] for i in range(len(m))]
    yi = [inverse(Mi[i], m[i]) for i in range(len(m))]

    X = sum([a[i] * Mi[i] * yi[i] for i in range(len(yi))])
    return X % M


def part2():
    with open("input.txt") as fh:
        _ = int(fh.readline())
        bus_ids = [int(id_) if id_ != "x" else "x" for id_ in fh.readline().split(",")]

    return chinese_remainder_theorem(bus_ids)


print(part2())