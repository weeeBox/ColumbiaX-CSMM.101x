"""
Skeleton code for Project 1 of Columbia University's AI EdX course (8-puzzle).
Python 3
"""

import math
import sys
from collections import deque
from typing import List


class Result:
    def __init__(self, path: List[str], nodes_expanded: int, search_depth: int, search_depth_max: int):
        self.path = path[:]
        self.nodes_expanded = nodes_expanded
        self.search_depth = search_depth
        self.search_depth_max = search_depth_max

    @property
    def cost_of_path(self):
        return len(self.path)


class State(object):
    """The Class that Represents the Puzzle"""

    def __init__(self, config, n, parent=None, action="Initial", cost=0):
        if n * n != len(config) or n < 2:
            raise ValueError("the length of config is not correct!")

        self.n = n
        self.cost = cost
        self.parent = parent
        self.action = action
        self.dimension = n
        self.config = config
        self.children = []

        for i, item in enumerate(self.config):
            if item == 0:
                self.blank_row = i // self.n
                self.blank_col = i % self.n
                break

    def display(self):
        for i in range(self.n):
            line = []
            offset = i * self.n
            for j in range(self.n):
                line.append(self.config[offset + j])
            print(line)

    def move_left(self):
        if self.blank_col == 0:
            return None
        else:
            blank_index = self.blank_row * self.n + self.blank_col
            target = blank_index - 1
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return State(tuple(new_config), self.n, parent=self, action="Left", cost=self.cost + 1)

    def move_right(self):
        if self.blank_col == self.n - 1:
            return None
        else:
            blank_index = self.blank_row * self.n + self.blank_col
            target = blank_index + 1
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return State(tuple(new_config), self.n, parent=self, action="Right", cost=self.cost + 1)

    def move_up(self):
        if self.blank_row == 0:
            return None
        else:
            blank_index = self.blank_row * self.n + self.blank_col
            target = blank_index - self.n
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return State(tuple(new_config), self.n, parent=self, action="Up", cost=self.cost + 1)

    def move_down(self):
        if self.blank_row == self.n - 1:
            return None
        else:
            blank_index = self.blank_row * self.n + self.blank_col
            target = blank_index + self.n
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return State(tuple(new_config), self.n, parent=self, action="Down", cost=self.cost + 1)

    def expand(self):
        # add child nodes in order of UDLR
        if len(self.children) == 0:
            up_child = self.move_up()
            if up_child is not None:
                self.children.append(up_child)

            down_child = self.move_down()
            if down_child is not None:
                self.children.append(down_child)

            left_child = self.move_left()
            if left_child is not None:
                self.children.append(left_child)

            right_child = self.move_right()
            if right_child is not None:
                self.children.append(right_child)

        return self.children

    def __eq__(self, other):
        return type(other) is type(self) and self.config == other.config

    def __lt__(self, other):
        return True  # to make priority queue happy

    def __hash__(self) -> int:
        return hash(self.config)

    def is_goal(self):
        for i, n in enumerate(self.config):
            if n != i:
                return False

        return True


KEY = 0
VALUE = 1


class PriorityDict:
    def __init__(self):
        self._items = []
        self._indices = {}

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def peek(self):
        return self._items[0][VALUE]

    def pop(self):
        value = self._items[0][VALUE]

        self._swap(0, len(self._items) - 1)
        self._items.pop()
        del self._indices[value]

        self._sink(0)
        return value

    def insert(self, key, value):
        index = len(self._items)
        self._items.append(self._wrap(key, value))
        self._indices[value] = index
        self._swim(index)

    def get_key(self, value):
        index = self._indices.get(value, -1)
        if index == -1:
            raise ValueError("Missing value: " + value)
        return self._items[index][KEY]

    def decrease_key(self, key, value):
        index = self._indices.get(value, -1)
        if index == -1:
            raise ValueError("Missing value: " + value)

        self._items[index] = self._wrap(key, value)
        self._swim(index)

    def contains(self, value):
        return value in self._indices

    def _swim(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self._items[parent][KEY] <= self._items[index][KEY]:
                break
            self._swap(index, parent)
            index = parent

    def _sink(self, index):
        child = 2 * index + 1
        while child < len(self._items):
            other_child = child + 1
            if other_child < len(self._items) and self._items[other_child][KEY] < self._items[child][KEY]:
                child = other_child

            if self._items[child][KEY] >= self._items[index][KEY]:
                break

            self._swap(child, index)
            index = child
            child = 2 * index + 1

    def _swap(self, i, j):
        self._indices[self._items[i][VALUE]] = j
        self._indices[self._items[j][VALUE]] = i
        self._items[i], self._items[j] = self._items[j], self._items[i]

    @staticmethod
    def _wrap(key, value):
        return key, value


# Function that Writes to output.txt

### Students need to change the method to have the corresponding parameters

def write_output(result):
    with open('output.txt', 'w') as file:
        write_to_output(file, result)


def write_to_output(file, result):
    def wrap(value):
        return f"'{value}'"

    file.write(f"path_to_goal: [{', '.join(wrap(path) for path in result.path)}]\n")
    file.write(f"cost_of_path: {result.cost_of_path}\n")
    file.write(f"nodes_expanded: {result.nodes_expanded}\n")
    file.write(f"search_depth: {result.search_depth}\n")
    file.write(f"max_search_depth: {result.search_depth_max}\n")
    file.write(f"running_time: 0\n")
    file.write(f"max_ram_usage: 0")


### Student Code Goes here

def _path(state):
    path = []
    while state and state.parent:
        path.append(state.action)
        state = state.parent

    path.reverse()
    return path


class Frontier:
    def __init__(self, initial_state):
        self._lookup = {initial_state}

    def __len__(self):
        return len(self._lookup)

    def __contains__(self, item):
        return item in self._lookup

    def neighbours_iter(self, neighbours):
        return iter(neighbours)

    def remove(self):
        state = self._remove()
        self._lookup.remove(state)
        return state

    def add(self, state):
        self._lookup.add(state)
        self._add(state)

    def _remove(self):
        raise NotImplementedError

    def _add(self, state):
        raise NotImplementedError


class BFSFrontier(Frontier):
    def __init__(self, initial_state):
        super(BFSFrontier, self).__init__(initial_state)
        self._frontier = deque([initial_state])

    def _remove(self):
        return self._frontier.popleft()

    def _add(self, state):
        self._frontier.append(state)


class DFSFrontier(Frontier):
    def __init__(self, initial_state):
        super(DFSFrontier, self).__init__(initial_state)
        self._frontier = [initial_state]

    def neighbours_iter(self, neighbours):
        return reversed(neighbours)

    def _remove(self):
        return self._frontier.pop()

    def _add(self, state):
        self._frontier.append(state)


class ASTFrontier(Frontier):
    def __init__(self, initial_state):
        super(ASTFrontier, self).__init__(initial_state)
        self._frontier = PriorityDict()
        self._frontier.insert(0, initial_state)

    def decrease_key(self, state):
        old_key = self._frontier.get_key(state)
        new_key = self._state_cost(state)
        if new_key < old_key:
            self._frontier.decrease_key(new_key, state)

    def _remove(self):
        return self._frontier.pop()

    def _add(self, state):
        self._frontier.insert(self._state_cost(state), state)

    @classmethod
    def _state_cost(cls, state):
        return state.cost + cls._manhattan_dist(state) + cls._action_cost(state)

    @classmethod
    def _manhattan_dist(cls, state: State) -> int:
        dist = 0
        n = state.n
        idx = 0
        for i in range(n):
            for j in range(n):
                val = state.config[idx]
                dist += abs(i - val // n) + abs(j - val % n)
                idx += 1

        return dist

    @classmethod
    def _action_cost(cls, state):
        action = state.action
        if action == 'Up':
            return 1
        if action == 'Down':
            return 2
        if action == 'Left':
            return 3
        if action == 'Right':
            return 4
        return 0


def _uninformed_graph_search(initial_state, frontier_type):
    frontier = frontier_type(initial_state)
    explored = set()
    nodes_expanded = max_depth = 0

    while frontier:
        state = frontier.remove()
        explored.add(state)

        if state.is_goal():
            return Result(
                path=_path(state),
                nodes_expanded=nodes_expanded,
                search_depth=state.cost,
                search_depth_max=max_depth
            )

        for neighbour in frontier.neighbours_iter(state.expand()):
            if neighbour not in frontier and neighbour not in explored:
                frontier.add(neighbour)
                max_depth = max(max_depth, neighbour.cost)

        nodes_expanded += 1

    return None


def _best_first_graph_search(initial_state, frontier_type):
    frontier = frontier_type(initial_state)
    explored = set()
    nodes_expanded = max_depth = 0

    while frontier:
        state = frontier.remove()
        explored.add(state)

        if state.is_goal():
            return Result(
                path=_path(state),
                nodes_expanded=nodes_expanded,
                search_depth=state.cost,
                search_depth_max=max_depth
            )

        for neighbour in frontier.neighbours_iter(state.expand()):
            if neighbour not in explored and neighbour not in frontier:
                frontier.add(neighbour)
                max_depth = max(max_depth, neighbour.cost)
            elif neighbour in frontier:
                frontier.decrease_key(neighbour)

        nodes_expanded += 1

    return None


def search(sm, initial_config):
    size = int(math.sqrt(len(initial_config)))
    initial_state = State(initial_config, size)

    if sm == "bfs":
        return _uninformed_graph_search(initial_state, BFSFrontier)
    elif sm == "dfs":
        return _uninformed_graph_search(initial_state, DFSFrontier)
    elif sm == "ast":
        return _best_first_graph_search(initial_state, ASTFrontier)
    else:
        raise ValueError("Invalid search method: " + sm)


def main():
    sm = sys.argv[1].lower()
    begin_state = sys.argv[2].split(",")
    begin_state = tuple(map(int, begin_state))
    result = search(sm, begin_state)
    write_output(result)


if __name__ == '__main__':
    main()
