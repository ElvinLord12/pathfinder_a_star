import copy

WALL = chr(9608)
OPEN = " "
START = "S"
GOAL = "G"


class Map:

    def __init__(self, grid):
        self._grid = copy.deepcopy(grid)
        self.start_pos = find_start_pos(grid)
        self.goals = find_goals(grid)

    def to_string(self, traveller=None, path_list=[], path_mark="#", considered_list=[], considered_mark="."):
        the_str = ""
        for y in range(len(self._grid[0])):
            for x in range(len(self._grid)):
                if traveller is not None and traveller.current_position == (x, y):
                    the_str += traveller.current_appearance
                elif (x, y) in path_list and self._grid[x][y] != START and self._grid[x][y] != GOAL:
                    the_str += path_mark
                elif (x, y) in considered_list and self._grid[x][y] != START and self._grid[x][y] != GOAL:
                    the_str += considered_mark
                elif traveller is not None and (x, y) in traveller.all_visited_positions and self._grid[x][y] != START and self._grid[x][y] != GOAL:
                    the_str += traveller.visited_appearance
                else:
                    the_str += self._grid[x][y]
            the_str += "\n"
        return the_str

    def valid_moves_from(self, pos):
        potential_neighbors = valid_neighbors(pos, len(self._grid), len(self._grid[0]))
        valid_moves = []
        for potential_neighbor in potential_neighbors:
            if self._grid[potential_neighbor[0]][potential_neighbor[1]] != WALL:
                valid_moves.append(potential_neighbor)
        return valid_moves

    def print(self):
        print(self.to_string())

    def print_with_traveller(self, traveller):
        print(self.to_string(traveller))

    def is_goal(self, pos):
        if self._grid[pos[0]][pos[1]] == GOAL:
            return True
        else:
            return False


def valid_neighbors(pos, x_length, y_length):
    x = pos[0]
    y = pos[1]
    all_neighbors_list = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
    valid_neighbors_list = []
    for x, y in all_neighbors_list:
        if 0 <= x < x_length and 0 <= y < y_length:
            valid_neighbors_list.append((x, y))
    return valid_neighbors_list


def find_start_pos(grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == START:
                return x, y
    raise Exception("No start point defined")


def find_goals(grid):
    goals = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == GOAL:
                goals.append((x, y))
    if len(goals) > 0:
        return goals
    else:
        raise Exception("No goals defined")
