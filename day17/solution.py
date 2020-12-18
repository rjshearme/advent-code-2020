ACTIVE = "#"
INACTIVE = "."

class LifeMatrix:

    def __init__(self, starting_cells):
        self.matrix = starting_cells

    def get_next_matrix(self):
        cur_matrix_height = len(self.matrix)
        cur_matrix_depth = len(self.matrix[0])
        cur_matrix_width = len(self.matrix[0][0])
        return [[[""] * (cur_matrix_width+2) for d in range(cur_matrix_depth+2)] for h in range(cur_matrix_height+2)]

    def get_num_adjacent_cells(self, layer_idx, row_idx, col_idx):
        return 1

    def tick(self):
        temp_matrix = self.get_next_matrix()
        for layer_idx, layer in enumerate(temp_matrix):
            for row_idx, row in enumerate(layer):
                for col_idx, cell in enumerate(row):
                    num_adjacent_cells = self.get_num_adjacent_cells(layer_idx, row_idx, col_idx)
                    if num_adjacent_cells == 3 or (num_adjacent_cells == 2 and cell == ACTIVE):
                        temp_matrix[layer_idx][row_idx][col_idx] = ACTIVE
                    else:
                        temp_matrix[layer_idx][row_idx][col_idx] = INACTIVE
        self.matrix = temp_matrix

    def count_alive_cells:
        return "".join("".join("".join()))



with open("input.txt") as fh:
    starting_cells = [list(line) for line in fh.read().split("\n")]

life_matrix = LifeMatrix(starting_cells)
life_matrix.tick()