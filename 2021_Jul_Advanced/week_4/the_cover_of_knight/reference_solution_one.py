#! Reference solution to compare execution times:
#! https://github.com/thewrongjames/ncss-challenge-2017/blob/master/the_cover_of_knight.py

#! Execution time (Example 1): 0.004415708997839829
#! Execution time (Example 2): 0.004900818999885814
#! Execution time (Size=100, Moves=10, Knight=20,30): 0.407586462002655


from time import perf_counter

from copy import deepcopy


class Vector(tuple):
    def __add__(self, other):
        new_values = []
        for own_dimension_value, other_dimension_value in zip(self, other):
            new_values.append(own_dimension_value + other_dimension_value)
        return Vector(new_values)

    def __sub__(self, other):
        new_values = []
        for own_dimension_value, other_dimension_value in zip(self, other):
            new_values.append(own_dimension_value - other_dimension_value)
        return Vector(new_values)

    def __repr__(self):
        return 'Vector([{}])'.format(', '.join([str(value) for value in self]))


KNIGHTS_MOVES = []
for vertical_move in (-2, -1, 1, 2):
    for horizontal_move in (-2, -1, 1, 2):
        if abs(vertical_move) != abs(horizontal_move):
            KNIGHTS_MOVES.append(Vector([vertical_move, horizontal_move]))


size = int(input('Size: '))
number_of_moves_that_may_be_made = int(input('Moves: '))
knight_pos = input('Knight: ')

start_time = perf_counter()
starting_position = Vector(
    [int(coordinate) for coordinate in knight_pos.split(',')]
)


moves_to_get_to_square = [[None for _ in range(size)] for _ in range(size)]
moves_to_get_to_square[starting_position[0]][starting_position[1]] = 0


def update_for_next_moves(moves_so_far):
    updated_moves = deepcopy(moves_so_far)
    size = len(moves_so_far)

    for row_index, row in enumerate(moves_so_far):
        for column_index, number_of_moves in enumerate(row):
            if number_of_moves is None:
                continue

            next_positions = []
            for move in KNIGHTS_MOVES:
                next_positions.append(Vector([row_index, column_index]) + move)

            for position in next_positions:
                if False in [0 <= value < size for value in position]:
                    continue

                if moves_so_far[position[0]][position[1]] is None:
                    updated_moves[position[0]][position[1]] = \
                        number_of_moves + 1
                    continue

                if number_of_moves + 1 < \
                        moves_so_far[position[0]][position[1]]:
                    updated_moves[position[0]][position[1]] = \
                        number_of_moves + 1

    return updated_moves


for _ in range(number_of_moves_that_may_be_made):
    moves_to_get_to_square = update_for_next_moves(moves_to_get_to_square)


for row in moves_to_get_to_square:
    print(' '.join(['.' if value is None else str(value) for value in row]))

end_time = perf_counter()
print(end_time - start_time)