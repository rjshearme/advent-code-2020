EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."

class Seats:

    def __init__(self, raw_data):
        self.matrix = [list(line) for line in raw_data.split()]
        self.prev_matrix = None
        self.row_len = len(self.matrix)
        self.col_len = len(self.matrix[0])

    def __repr__(self):
        return "\n".join("".join(row) for row in self.matrix)

    @property
    def is_alive(self):
        return self.prev_matrix != self.matrix

    @property
    def num_occupied_seats(self):
        return "".join("".join(row) for row in self.matrix).count(OCCUPIED)

    def seat_is_occupied(self, row_idx, col_idx):
        if 0 > row_idx or row_idx >= self.row_len or 0 > col_idx or col_idx >= self.col_len:
            return False
        return self.matrix[row_idx][col_idx] == OCCUPIED

    def get_occupied_adjs(self, row_idx, col_idx):
        surrounding_seats = ((row, col) for col in range(col_idx - 1, col_idx + 2) for row in
                             range(row_idx - 1, row_idx + 2) if not (row == row_idx and col == col_idx))
        return sum(self.seat_is_occupied(row, col) for row, col in surrounding_seats)

    def get_occuppied_line_of_sights_coordinates(self, row_idx, col_idx, direction_vertical, direction_horizontal):
        row_idx -= direction_vertical
        col_idx -= direction_horizontal
        while  -1 <= row_idx < self.row_len and -1 <= col_idx < self.col_len and self.matrix[row_idx][col_idx] == FLOOR:
            row_idx -= direction_vertical
            col_idx -= direction_horizontal
        return row_idx, col_idx

    def get_occupied_line_of_sights(self, row_idx, col_idx):
        directions = [
            (1, 0), (-1, 0),
            (0, 1), (0, -1),
            (1, 1), (-1, -1),
            (1, -1), (-1, 1),
        ]
        num_occupied = 0
        for direction in directions:
            dir_row, dir_col = self.get_occuppied_line_of_sights_coordinates(row_idx, col_idx, direction[0], direction[1])
            if self.seat_is_occupied(dir_row, dir_col):
                num_occupied += 1
        return num_occupied


    def tick(self):
        temp_matrix = []
        for row_idx, row in enumerate(self.matrix):
            temp_row = []
            for col_idx, seat in enumerate(row):
                num_occupied_adjs = self.get_occupied_line_of_sights(row_idx, col_idx)
                temp_seat_val = seat
                if seat == EMPTY and num_occupied_adjs == 0:
                    temp_seat_val = OCCUPIED
                if seat == OCCUPIED and num_occupied_adjs >= 5:
                    temp_seat_val = EMPTY
                temp_row.append(temp_seat_val)
            temp_matrix.append(temp_row)
        self.prev_matrix = self.matrix
        self.matrix = temp_matrix


with open("input.txt") as fh:
    raw_data = fh.read()


def run_game_of_life():
    seats = Seats(raw_data)
    while seats.is_alive:
        seats.tick()
    print(seats.num_occupied_seats)


run_game_of_life()