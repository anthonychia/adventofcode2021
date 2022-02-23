from typing import List
import numpy as np
from collections import Counter

class Cave():
    def __init__(self, name):
        self.name = name
        self.visited = 0

    def visit(self):
        self.visited += 1

    def is_big(self):
        return self.name.isupper()

class Connection():
    def __init__(self, points: List):
        self.points = points

    def find_connection(self, point):
        if self.points[0] == point:
            return self.points[1]
        elif self.points[1] == point:
            return self.points[0]
        else:
            return None

    def __str__(self):
        return '-'.join(self.points)

def find_connections(point):
    destinations = []
    for c in connections:
        next = c.find_connection(point)
        if next: destinations.append(next)
    return destinations

# input
f = open('input.txt')
lines = f.readlines()
connections = [Connection(line.replace('\n', '').split('-')) for line in lines]
caves = set(np.array([c.points for c in connections]).flatten())
caves = {cave: Cave(cave) for cave in caves}
graph = {cave: find_connections(cave) for cave in caves}

print(graph)

# part 1
def find_all_paths(start, end, graph, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for node in graph[start]:
        if (Counter(visited)[node] >= 1 and not node.isupper()) or node == start:
            continue
        if node == end:
            yield [start, end]
        else:
            visited_copy = visited.copy()
            for path in find_all_paths(node, end, graph, visited_copy):
                yield [start] + path


paths = [path for path in find_all_paths('start', 'end', graph)]
print(len(paths))


# part 2
def find_all_paths_small_twice(start, end, graph, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for node in graph[start]:
        small_caves_count = {k: v for k, v in Counter(visited).items() if not k.isupper() and k != 'start'}.values()
        if sum([count >= 2 for count in small_caves_count]) > 1 or max(small_caves_count, default=0) > 2 \
                or node == start or node == 'start':
            continue

        if node == end:
            # print(visited + [node])
            yield [start, end]
        else:
            visited_copy = visited.copy()
            for path in find_all_paths_small_twice(node, end, graph, visited_copy):
                yield [start] + path


paths = [path for path in find_all_paths_small_twice('start', 'end', graph)]
print(len(paths))