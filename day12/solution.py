NORTH = "N"
SOUTH = "S"
EAST = "E"
WEST = "W"
LEFT = "L"
RIGHT = "R"
FORWARD = "F"


class Bearing:

    def __init__(self, val_):
        self.val = val_

    def __repr__(self):
        return f"<Bearing({self.val})>"

    def __add__(self, other):
        self.val += other
        self.val %= 360

    def __iadd__(self, other):
        self.__add__(other)
        return self

    def __sub__(self, other):
        self.__add__(-other)

    def __isub__(self, other):
        self.__sub__(other)
        return self

    @property
    def direction(self):
        return NORTH if self.val == 0 else SOUTH if self.val == 180 else EAST if self.val == 90 else WEST


with open("input.txt") as fh:
    instructions = [(line[0], int(line[1:])) for line in fh.read().split()]


def move_ship_part1(cur_x, cur_y, cur_bearing, action, value):
    if action == NORTH:
        cur_y += value
    elif action == SOUTH:
        cur_y -= value
    elif action == EAST:
        cur_x += value
    elif action == WEST:
        cur_x -= value
    elif action == LEFT:
        cur_bearing -= value
    elif action == RIGHT:
        cur_bearing += value
    elif action == FORWARD:
        cur_x, cur_y, cur_bearing = move_ship_part1(cur_x, cur_y, cur_bearing, cur_bearing.direction, value)

    return cur_x, cur_y, cur_bearing


def rotate_waypoint(way_x, way_y, value):
    value %= 360
    rotations = value // 90
    if rotations == 1:
        way_x, way_y = way_y, -way_x
    if rotations == 2:
        way_x, way_y = -way_x, -way_y
    if rotations == 3:
        way_x, way_y = -way_y, way_x
    return way_x, way_y


def move_ship_part2(ship_x, ship_y, way_x, way_y, action, value):
    if action == NORTH:
        way_y += value
    elif action == SOUTH:
        way_y -= value
    elif action == EAST:
        way_x += value
    elif action == WEST:
        way_x -= value
    elif action == LEFT:
        way_x, way_y = rotate_waypoint(way_x, way_y, -value)
    elif action == RIGHT:
        way_x, way_y = rotate_waypoint(way_x, way_y, value)
    elif action == FORWARD:
        ship_x += value * way_x
        ship_y += value * way_y
    return ship_x, ship_y, way_x, way_y

# x, y, bearing = 0, 0, Bearing(90)
ship_x, ship_y, way_x, way_y = 0, 0, 10, 1

for instruction in instructions:
    # x, y, bearing = move_ship_part_1(x, y, bearing, instruction[0], instruction[1])

    ship_x, ship_y, way_x, way_y = move_ship_part2(ship_x, ship_y, way_x, way_y, instruction[0], instruction[1])
    inst = f"{instruction[0]} {instruction[1]}".ljust(5)
    print(inst, ship_x, ship_y, way_x, way_y)

print(abs(ship_x) + abs(ship_y))