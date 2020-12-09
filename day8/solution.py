import argparse


def parse_operation_line(line):
    operation, value = line.split(" ")
    value = int(value)
    return operation, value


def get_operation_list(input_file):
    with open(input_file) as fh:
        file_lines = fh.readlines()
    return [parse_operation_line(line) for line in file_lines]


class Operations:

    def __init__(self, operations):
        self._operations = operations
        self.edit_position = -1

    def __repr__(self):
        return str(self.operations)

    @property
    def runs(self):
        _, terminated = self.run()
        return terminated

    @property
    def operations(self):
        return [
            self.flip_operation(operation) if index == self.edit_position else operation
            for index, operation
            in enumerate(self._operations)
        ]

    def get_next_operation_index(self, operation, value, current_position):
        return current_position + 1 if operation in ["nop", "acc"] else current_position + value

    def run(self):
        accumulator_value = current_operation_index = 0
        operation_indices_seen = set()
        while current_operation_index not in operation_indices_seen and current_operation_index < len(self.operations):
            operation_indices_seen.add(current_operation_index)
            operation, value = self.operations[current_operation_index]
            current_operation_index = self.get_next_operation_index(operation, value, current_operation_index)

            if operation == "acc":
                accumulator_value += value
        return accumulator_value, current_operation_index==len(self.operations)

    def flip_operation(self, operation_items):
        operation, value = operation_items
        if operation == "jmp":
            return("nop", value)
        elif operation == "nop":
            return ("jmp", value)
        return (operation, value)

    def get_next_possible_operations(self):
        self.edit_position +=1


def solve_part_1(input_file):
    parsed_operations = get_operation_list(input_file)
    operations = Operations(parsed_operations)
    accumulator_value, _ = operations.run()
    print(accumulator_value)


def solve_part_2(input_file):
    parsed_operations = get_operation_list(input_file)
    operations = Operations(parsed_operations)
    while not operations.runs:
        operations.get_next_possible_operations()
    accumulator_value, _ = operations.run()
    print(accumulator_value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Advent of Code Day 8")
    parser.add_argument("input_file", help="The input file to run the code on")
    parser.add_argument("part", type=int, choices=[1,2], help="The part of the problem to sovle")

    args = parser.parse_args()

    if args.part == 1:
        solve_part_1(args.input_file)
    elif args.part == 2:
        solve_part_2(args.input_file)
