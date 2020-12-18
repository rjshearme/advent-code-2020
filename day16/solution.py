import math


class Field:

    def __init__(self, raw_text):
        self.name, ranges = raw_text.split(": ")
        lower_ranges, _, upper_ranges = ranges.split(" ")
        self.lower_range_min, self.lower_range_max = map(int, lower_ranges.split("-"))
        self.upper_range_min, self.upper_range_max = map(int, upper_ranges.split("-"))

    def __repr__(self):
        return self.name

    def contains_value(self, value):
        return self.lower_range_min <= value <= self.lower_range_max or self.upper_range_min <= value <= self.upper_range_max

    def contains_values(self, values):
        for value in values:
            if not self.contains_value(value):
                return False
        return True


class Ticket:

    def __init__(self, raw_text):
        self.values = list(map(int, raw_text.split(",")))


def solve_part_1(fields, nearby_tickets):
    invalid_ticket_count = 0
    for ticket in nearby_tickets:
        for value in ticket.values:
            if not any(field.contains_value(value) for field in fields):
                invalid_ticket_count += value

    return invalid_ticket_count


def is_valid_ticket(fields, ticket):
    for value in ticket.values:
        if not any(field.contains_value(value) for field in fields):
            return False
    return True


def possible_fields_for_position(fields, tickets, position):
    ticket_values = [ticket.values[position] for ticket in tickets]
    possible_fields = set()
    for field in fields:
        if field.contains_values(ticket_values):
            possible_fields.add(field.name)
    return possible_fields


# def fill_in_name_to_position_mapping(fields, nearby_tickets, mapping):


def solve_part_2(fields, tickets, my_ticket):
    fields_ = fields.copy()
    positions = range(len(fields))
    name_position_mapping = {}
    while positions:
        new_positions = []
        field_found = ""
        for position in positions:
            possible_fields = possible_fields_for_position(fields, tickets, position)
            if len(possible_fields) == 1:
                field_found = possible_fields.pop()
                name_position_mapping[field_found] = position
            else:
                new_positions.append(position)
        positions = new_positions
        fields = [field for field in fields if field.name != field_found]
    total = 1
    for field_name, position in name_position_mapping.items():
        if field_name.startswith("departure"):
            total *= my_ticket.values[position]
    return total


with open("input.txt") as fh:
    raw_fields, my_ticket_raw, nearby_tickets_raw = fh.read().split("\n\n")

fields = [Field(raw_field) for raw_field in raw_fields.split("\n")]
nearby_tickets = [Ticket(raw_ticket) for raw_ticket in nearby_tickets_raw.split("\n")[1:]]
valid_tickets = [ticket for ticket in nearby_tickets if is_valid_ticket(fields, ticket)]
my_ticket = Ticket(my_ticket_raw.split("\n")[1])

print(solve_part_2(fields, valid_tickets, my_ticket))