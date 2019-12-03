import sys

from mapwork.map.mazemaker import make_perfect_maze_grid, make_loopy_maze_grid, make_open_map_grid, make_line_map_grid
from mapwork.map.map import Map
from mapwork.pathfinder.pathfinder import choose_path_dfs, choose_path_bfs, choose_path_a_star
import datetime


def run_path_finder(map, path_finder):
    start = datetime.datetime.now()

    path, visited = path_finder(map, map.start_pos)

    timing = datetime.datetime.now() - start

    # print(map.to_string(path_list=path, considered_list=visited), sep="")
    print(timing, "\t", len(path))


def main():
    line_map = Map(make_perfect_maze_grid(50, 50))

    print(line_map.to_string())
    for path_finder in [choose_path_dfs, choose_path_bfs, choose_path_a_star]:
        start = datetime.datetime.now()
        path_list, considered_list = path_finder(line_map, line_map.start_pos)
        elapsed = datetime.datetime.now() - start
        print(line_map.to_string(path_list=path_list, considered_list=considered_list), sep="")
        print(path_finder.__name__, " - ", "Time: ", elapsed, "\tpath length:", len(path_list))

    for i in range(10,101000,1000):
        open_map = Map(make_open_map_grid(i, i))
        start = datetime.datetime.now()
        path, visited = choose_path_a_star(open_map, open_map.start_pos)
        timing = datetime.datetime.now() - start
        print(timing, "\t", len(path), "\t", i)

    # print("DFS Line")
    # for i in range(10, 1000, 50):
    #     line_map = Map(make_line_map_grid(i, i, 0.25))
    #
    #     start = datetime.datetime.now()
    #     path, visited = choose_path_dfs(line_map, line_map.start_pos)
    #     timing = datetime.datetime.now() - start
    #
    #     print(timing, "\t", len(path), "\t", i)
    # print("==================")
    # print("DFS Open")
    # for i in range(10,1000,50):
    #     open_map = Map(make_open_map_grid(i, i))
    #     start = datetime.datetime.now()
    #     path, visited = choose_path_dfs(open_map, open_map.start_pos)
    #     timing = datetime.datetime.now() - start
    #
    #     print(timing, "\t", len(path), "\t", i)
    # print("==================")
    # print("DFS Loopy")
    # for i in range(10,1000,50):
    #     loopy_map = Map(make_loopy_maze_grid(i, i))
    #     start = datetime.datetime.now()
    #     path, visited = choose_path_dfs(loopy_map, loopy_map.start_pos)
    #     timing = datetime.datetime.now() - start
    #
    #     print(timing, "\t", len(path), "\t", i)
    # print("==================")
    # print("DFS Perfect")
    # for i in range(10,1000,50):
    #     perfect_map = Map(make_perfect_maze_grid(i, i))
    #     start = datetime.datetime.now()
    #     path, visited = choose_path_dfs(perfect_map, perfect_map.start_pos)
    #     timing = datetime.datetime.now() - start
    #
    #     print(timing, "\t", len(path), "\t", i)
    #
    # # ========================
    #
    # print("BFS Line")
    # for i in range(10, 1000, 50):
    #     line_map = Map(make_line_map_grid(i, i, .25))
    #     start = datetime.datetime.now()
    #     path, visited = choose_path_bfs(line_map, line_map.start_pos)
    #     timing = datetime.datetime.now() - start
    #
    #     print(timing, "\t", len(path), "\t", i)
    # print("==================")
    # print("BFS Open")
    # for i in range(10, 1000, 50):
    #     open_map = Map(make_open_map_grid(i, i))
    #     start = datetime.datetime.now()
    #     path, visited = choose_path_bfs(open_map, open_map.start_pos)
    #     timing = datetime.datetime.now() - start
    #
    #     print(timing, "\t", len(path), "\t", i)
    # print("==================")
    # print("BFS Loopy")
    # for i in range(10, 1000, 50):
    #     loopy_map = Map(make_loopy_maze_grid(i, i))
    #     start = datetime.datetime.now()
    #     path, visited = choose_path_bfs(loopy_map, loopy_map.start_pos)
    #     timing = datetime.datetime.now() - start
    #
    #     print(timing, "\t", len(path), "\t", i)
    # print("==================")
    # print("BFS Perfect")
    # for i in range(10, 1000, 50):
    #     perfect_map = Map(make_perfect_maze_grid(i, i))
    #     start = datetime.datetime.now()
    #     path, visited = choose_path_bfs(perfect_map, perfect_map.start_pos)
    #     timing = datetime.datetime.now() - start
    #
    #     print(timing, "\t", len(path), "\t", i)
    #
    # # ========================
    #
    # print("A* Line")
    # for i in range(10, 1000, 50):
    #     line_map = Map(make_line_map_grid(i, i, 0.25))
    #     start = datetime.datetime.now()
    #     path, visited = choose_path_a_star(line_map, line_map.start_pos)
    #     timing = datetime.datetime.now() - start
    #
    #     print(timing, "\t", len(path), "\t", i)
    # print("==================")
    # print("A* Open")
    # for i in range(10, 1000, 50):
    #     open_map = Map(make_open_map_grid(i, i))
    #     start = datetime.datetime.now()
    #     path, visited = choose_path_a_star(open_map, open_map.start_pos)
    #     timing = datetime.datetime.now() - start
    #
    #     print(timing, "\t", len(path), "\t", i)
    # print("==================")
    # print("A* Loopy")
    # for i in range(10, 1000, 50):
    #     loopy_map = Map(make_loopy_maze_grid(i, i))
    #     start = datetime.datetime.now()
    #     path, visited = choose_path_a_star(loopy_map, loopy_map.start_pos)
    #     timing = datetime.datetime.now() - start
    #
    #     print(timing, "\t", len(path), "\t", i)
    # print("==================")
    # print("A* Perfect")
    # for i in range(10, 1000, 50):
    #     perfect_map = Map(make_perfect_maze_grid(i, i))
    #     start = datetime.datetime.now()
    #     path, visited = choose_path_a_star(perfect_map, perfect_map.start_pos)
    #     timing = datetime.datetime.now() - start
    #
    #     print(timing, "\t", len(path), "\t", i)





if __name__ == '__main__':
    main()
