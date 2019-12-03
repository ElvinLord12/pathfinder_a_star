import unittest

from mapwork.map import mazemaker
from mapwork.map.mazemaker import MazeMaker


class TestMaze(unittest.TestCase):

    def test_is_removeable_wall(self):
        # 3x3 grid has only middle removeable
        a_maze = MazeMaker(mazemaker.make_solid_grid(3, 3))
        for y in range(3):
            for x in range(3):
                if x == 1 and y == 1:
                    self.assertTrue(a_maze.is_removeable_wall_in_perfect_maze((x, y)))
                else:
                    self.assertFalse(a_maze.is_removeable_wall_in_perfect_maze((x, y)))

        # 5x5 grid has middle 9 squares removeable
        a_grid = mazemaker.make_solid_grid(5, 5)
        a_maze = MazeMaker(a_grid)
        for y in range(5):
            for x in range(5):
                if 0 < x < 4 and 0 < y < 4:
                    self.assertTrue(a_maze.is_removeable_wall_in_perfect_maze((x, y)))
                else:
                    self.assertFalse(a_maze.is_removeable_wall_in_perfect_maze((x, y)))
        # make piece not wall
        a_grid[1][1] = " "
        self.assertFalse(a_maze.is_removeable_wall_in_perfect_maze((1, 1)))
        # can remove below it
        self.assertTrue(a_maze.is_removeable_wall_in_perfect_maze((2, 1)))
        a_grid[1][2] = " "

        # can't remove a wall that would join two spaces
        a_grid[3][1] = " "
        a_grid[3][2] = " "
        self.assertFalse(a_maze.is_removeable_wall_in_perfect_maze((2, 1)))
        self.assertFalse(a_maze.is_removeable_wall_in_perfect_maze((2, 2)))

        # can remove a wall that is not attached to any open space
        self.assertTrue(a_maze.is_removeable_wall_in_perfect_maze((2, 3)))

    def test_find_removeable_neighbor_walls(self):
        a_grid = mazemaker.make_solid_grid(5, 5)
        a_grid[1][1] = " "
        a_grid[1][2] = " "
        a_grid[3][1] = " "
        a_grid[3][2] = " "
        a_maze = MazeMaker(a_grid)
        # print(a_maze)
        for y in range(5):
            for x in range(5):
                if x == 2 and y == 3:
                    self.assertEqual(len(a_maze.find_removeable_neighbor_walls((x, y))), 2,
                                     "should be 2 removeable walls on sides")
                elif 0 <= x <= 4 and y == 3:
                    self.assertEqual(len(a_maze.find_removeable_neighbor_walls((x, y))), 1,
                                     "should be 1 removeable wall")
                elif 0 < x < 4 and y == 2:
                    self.assertEqual(len(a_maze.find_removeable_neighbor_walls((x, y))), 1,
                                     "should be 1 removeable wall below at: "+str(x)+", "+str(y))
                elif 0 < x < 4 and y == 4:
                    self.assertEqual(len(a_maze.find_removeable_neighbor_walls((x, y))), 1,
                                     "should be 1 removeable wall above at: " + str(x) + ", " + str(y))
                else:
                    self.assertEqual(len(a_maze.find_removeable_neighbor_walls((x, y))), 0,
                                     "should be no removeable walls anywhere else, but there are at: "+str(x)+", "+str(y))

    def test_create_perfect_maze(self):
        print("Perfect Maze")
        a_maze = MazeMaker()
        a_maze.create_perfect_maze(20, 10)
        # print(a_maze)
        a_maze.place_start()
        a_maze.place_randomized_bottom_right_goal()
        print(a_maze)

    def test_create_loopy_maze_grid(self):
        print("Loopy Maze")
        a_maker = MazeMaker()
        a_maker.create_perfect_maze(30, 20)
        a_maker.place_start()
        a_maker.place_randomized_bottom_right_goal()
        a_maker.remove_random_walls(0.1)
        print(a_maker)

    def test_create_open_grid(self):
        print("Open Map")
        a_maker = MazeMaker()
        a_maker.create_perfect_maze(30, 20)
        a_maker.place_start()
        a_maker.place_randomized_bottom_right_goal()
        a_maker.remove_random_walls(1.2)
        print(a_maker)

    def test_create_line_grid(self):
        print("Smaller Line Map")
        grid = mazemaker.make_line_map_grid(80, 30, 0.25)
        to_print = MazeMaker(grid)
        print(to_print)
        print("Giant Line Map")
        grid = mazemaker.make_line_map_grid(500, 500, 0.1)
        to_print = MazeMaker(grid)
        print(to_print)



if __name__ == '__main__':
    unittest.main()
