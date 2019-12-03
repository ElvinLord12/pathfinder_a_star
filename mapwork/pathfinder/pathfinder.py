import copy
from heapq import *
import random
from collections import deque
from queue import Queue, PriorityQueue
from mapwork.pathfinder.coord import Coordinate
from mapwork.map.mazemaker import manhattan_distance


def choose_path_dfs(a_map, start_point):
    """
    :param start_point: Where you want the path to start
    :param a_map: a map to analyze, not change
    :return: a list of positions (x, y) that are the suggested path from current position to a goal
    """

    previous = {}  # visited/came from
    previous[start_point] = None
    has_visited = []

    path = []

    stack = []  # stack

    # setup
    stack.append(start_point)

    while len(stack) > 0:
        current = stack.pop()
        has_visited.append(current)
        children = a_map.valid_moves_from(current)
        if a_map.is_goal(current):
            break
        for i in children:
            if i not in previous:
                stack.append(i)
                previous[i] = current
    while current != start_point:
        path.append(current)
        current = previous[current]
    return path, has_visited



def choose_path_bfs(a_map, start_point):
    """
    :param start_point: Where you want the path to start
    :param a_map: a map to analyze, not change
    :return: a list of positions (x, y) that are the suggested path from current position to a goal
    """

    # our data structures
    available = Queue()
    available.put(start_point)
    has_visited = []

    path = []

    previous = {}
    previous[start_point] = None

    # while our available places to move isn't empty do stuff
    while not available.empty():
        current = available.get()
        has_visited.append(current)
        for i in a_map.valid_moves_from(current):  # for all valid moves from our current to check
            if i not in previous:
                available.put(i)
                previous[i] = current
        if a_map.is_goal(current):  # if our current is now the goal we start to backtrack
            while current != start_point:
                path.append(current)
                current = previous[current]
            return path, has_visited
    return path, has_visited


def choose_path_a_star(a_map, start_point):
    goal = a_map.goals[0]
    visited = []

    heap = []
    heappush(heap, (0, start_point))

    previous = {}
    costs = {}
    previous[start_point] = None
    costs[start_point] = 0

    while len(heap) != 0:
        got = heappop(heap)  # grabs tuple from priority q
        current = got[1]  # grabs point
        visited.append(current)

        if current == goal:
            break  # if goal is found break loop

        for available in a_map.valid_moves_from(current):
            new_cost = costs[current] + 1

            if available not in costs or new_cost < costs[available]:
                costs[available] = new_cost  # add new cost to our cost dict

                priority = new_cost + manhattan_distance(goal, available)  # grab the priority using heuristic

                heappush(heap, (priority, available))
                previous[available] = current

    path = []
    path_point = previous[current]
    if current != goal:
        return path, visited
    while path_point != start_point:
        path.append(path_point)
        path_point = previous[path_point]
    return path, visited







