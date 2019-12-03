import random
from mapwork.map import map


class MazeMaker:

    def __init__(self, grid=None):
        self.grid = grid

    def __str__(self):
        the_str = ""
        for y in range(len(self.grid[0])):
            for x in range(len(self.grid)):
                the_str += self.grid[x][y]
            the_str += "\n"
        return the_str

    def create_perfect_maze(self, x_length, y_length, more_dense=False):
        assert x_length >= 3 and y_length > 3, "Perfect mazes must have at least one internal space"
        neighbor_count_to_halt = 2
        if more_dense:
            neighbor_count_to_halt = 1

        self.grid = make_solid_grid(x_length, y_length)
        self.grid[1][1] = map.OPEN
        active = [(1, 1)]
        while len(active) != 0:
            current_pos = active.pop()
            removeable_neighbor_walls = self.find_removeable_neighbor_walls(current_pos)
            if len(removeable_neighbor_walls) > 0:
                if len(removeable_neighbor_walls) > neighbor_count_to_halt:
                    active.append(current_pos)
                wall_to_remove = random.choice(removeable_neighbor_walls)
                self.grid[wall_to_remove[0]][wall_to_remove[1]] = map.OPEN
                active.append(wall_to_remove)
            # print(self, "\n")
            # time.sleep(0.2)

    def place_start(self):
        self.grid[1][1] = map.START

    def find_random_empty_location(self):
        x = random.randrange(len(self.grid))
        y = random.randrange(len(self.grid[0]))
        while self.grid[x][y] != map.OPEN:
            x = random.randrange(len(self.grid))
            y = random.randrange(len(self.grid[0]))
        return x, y

    def find_random_empty_location_away_from(self, pos_to_avoid):
        min_dist = len(self.grid)
        if len(self.grid[0]) < len(self.grid):
            min_dist = len(self.grid[0])
        new_pos = self.find_random_empty_location()
        while manhattan_distance(new_pos, pos_to_avoid) < min_dist-1:
            new_pos = self.find_random_empty_location()
        return new_pos

    def place_randomized_bottom_right_goal(self):
        goal = (len(self.grid)-1, len(self.grid[0])-1)
        while self.grid[goal[0]][goal[1]] == map.WALL:
            if random.randint(0, 1) == 0:
                goal = (goal[0]-1, goal[1])
            else:
                goal = (goal[0], goal[1]-1)
            if goal[0] < 1 or goal[1] < 1:
                raise Exception("couldn't find goal with this random method")
        self.grid[goal[0]][goal[1]] = map.GOAL

    def find_removeable_neighbor_walls(self, pos):
        removeable_neighbor_walls = []
        for neighbor in self.valid_neighbors(pos):
            if self.is_removeable_wall_in_perfect_maze(neighbor):
                removeable_neighbor_walls.append(neighbor)
        return removeable_neighbor_walls

    def is_removeable_wall_in_perfect_maze(self, pos):
        if not self.is_inner_wall(pos):
            return False
        else:
            # if 3 neighbors are walls (only one neighbor is not a wall), it can be removed
            wall_count = 0
            for nx, ny in self.valid_neighbors(pos):
                if self.grid[nx][ny] == map.WALL:
                    wall_count += 1
            return wall_count >= 3

    def is_inner_wall(self, pos):
        x = pos[0]
        y = pos[1]
        if self.grid[x][y] != map.WALL:
            return False
        elif x < 1 or y < 1 or y >= len(self.grid[0]) - 1 or x >= len(self.grid) - 1:
            return False
        else:
            return True

    def valid_neighbors(self, pos):
        return map.valid_neighbors(pos, len(self.grid), len(self.grid[0]))

    def remove_random_walls(self, removal_factor):
        assert len(self.grid) >= 5 and len(self.grid[0]) > 5, "Need to be big enough to have walls to remove"
        num_remove_attempts = int((len(self.grid)-1) * (len(self.grid[0])-1) * removal_factor)
        for count in range(num_remove_attempts):
            x = random.randrange(len(self.grid))
            y = random.randrange(len(self.grid[0]))
            if self.is_inner_wall((x, y)):
                self.grid[x][y] = map.OPEN

    def add_random_linear_wall(self, length_factor):
        x = random.randrange(len(self.grid))
        y = random.randrange(len(self.grid[0]))
        change = random.choice([-1, 1])
        if random.randint(0, 1) == 0:
            max_length = int (len(self.grid) * length_factor)
            x_change = change
            y_change = 0
        else:
            max_length = int(len(self.grid[0]) * length_factor)
            x_change = 0
            y_change = change
        len_so_far = 0
        while 0 < x < len(self.grid) and 0 < y < len(self.grid[0]) and len_so_far < max_length:
            self.grid[x][y] = map.WALL
            x += x_change
            y += y_change
            len_so_far += 1


def manhattan_distance(p1, p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])


def make_solid_grid(x_length, y_length):
    grid = []
    for x in range(x_length):
        column = []
        for y in range(y_length):
            column.append(map.WALL)
        grid.append(column)
    return grid


def make_inner_empty_grid(x_length, y_length):
    grid = []
    for x in range(x_length):
        column = []
        for y in range(y_length):
            if x == 0 or y == 0 or x == x_length-1 or y == y_length-1:
                column.append(map.WALL)
            else:
                column.append(map.OPEN)
        grid.append(column)
    return grid


def make_perfect_maze_grid(x_length, y_length):
    a_maker = MazeMaker()
    a_maker.create_perfect_maze(x_length, y_length)
    a_maker.place_start()
    a_maker.place_randomized_bottom_right_goal()
    return a_maker.grid


def make_loopy_maze_grid(x_length, y_length):
    a_maker = MazeMaker()
    a_maker.create_perfect_maze(x_length, y_length)
    a_maker.place_start()
    a_maker.place_randomized_bottom_right_goal()
    a_maker.remove_random_walls(0.1)

    return a_maker.grid


def make_open_map_grid(x_length, y_length):
    a_maker = MazeMaker()
    a_maker.create_perfect_maze(x_length, y_length)
    a_maker.place_start()
    a_maker.place_randomized_bottom_right_goal()
    a_maker.remove_random_walls(1.2)

    return a_maker.grid


def make_line_map_grid(x_length, y_length, line_length_factor):
    a_maker = MazeMaker(make_inner_empty_grid(x_length, y_length))
    for x in range(x_length//4):
        a_maker.add_random_linear_wall(line_length_factor)
    start = a_maker.find_random_empty_location()
    a_maker.grid[start[0]][start[1]] = map.START
    goal = a_maker.find_random_empty_location_away_from(start)
    a_maker.grid[goal[0]][goal[1]] = map.GOAL
    return a_maker.grid
