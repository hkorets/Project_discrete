import pygame
import sys
import time
class TreeNode:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def find_paths(map, start_symbol, end_symbol):
    def get_neighbors(x, y):
        neighbors = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(map) and 0 <= new_y < len(map[0]):
                if map[new_x][new_y].isalpha() or map[new_x][new_y].isdigit():
                    teleporter = map[new_x][new_y]
                    teleporter_positions = [(new_x, new_y)]
                    for i, row in enumerate(map):
                        for j, char in enumerate(row):
                            if char == teleporter and (i != new_x or j != new_y):
                                teleporter_positions.append((i, j))
                    neighbors.extend(teleporter_positions)
                elif map[new_x][new_y] != '#' and map[new_x][new_y] != ' ':
                    neighbors.append((new_x, new_y))
        return neighbors

    def build_tree(parent_node, current_position):
        for neighbor in get_neighbors(*current_position):
            if neighbor not in visited:
                visited.add(neighbor)
                child_node = TreeNode(neighbor, parent_node)
                parent_node.add_child(child_node)
                build_tree(child_node, neighbor)
    start_position = None
    end_position = None
    for i, row in enumerate(map):
        for j, char in enumerate(row):
            if char == start_symbol:
                start_position = (i, j)
            elif char == end_symbol:
                end_position = (i, j)
    if start_position is None or end_position is None:
        return "Start or End Point was not found!"
    visited = set()
    root = TreeNode(start_position)
    visited.add(start_position)
    build_tree(root, start_position)

    def find_path(node, path=[]):
        path.append(node.position)
        if node.position == end_position:
            nonlocal found_path
            found_path = True
            return path.copy()
        for child in node.children:
            if not found_path:
                result = find_path(child, path)
                if result:
                    return result
        path.pop()
    found_path = False
    path = find_path(root)
    print("Solution:")
    return path

def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = file.readlines()
        data = [i.replace("\n", "") for i in data]
    return data

#VIZUALISATION
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (175, 238, 238)
GREY = (211, 211, 211)
GREEN = (107, 142, 35)

def draw_grid(screen, maze, cell_size):
    for row in range(len(maze)):
        for column in range(len(maze[0])):
            if maze[row][column] == "." or maze[row][column] == " ":
                color = WHITE
            elif maze[row][column] == "#":
                color = BLACK
            pygame.draw.rect(screen, color, [column * cell_size, row * cell_size, cell_size, cell_size])

def draw_path(screen, path, cell_size):
    for coord in path:
        row, col = coord
        pygame.draw.rect(screen, GREEN, [col * cell_size, row * cell_size, cell_size, cell_size])
        pygame.display.flip()
        time.sleep(0.1 * (30 / len(path)))  # Dynamic delay based on maze size

def solve_maze(maze, path):
    pygame.init()
    maze_size = max(len(maze), len(maze[0]))
    window_size = min(700, 700 // maze_size * maze_size)  # Calculate window size
    cell_size = window_size // maze_size  # Calculate cell size
    screen = pygame.display.set_mode((window_size, window_size))
    pygame.display.set_caption("Maze Solver")
    clock = pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(WHITE)
        draw_grid(screen, maze, cell_size)
        draw_path(screen, path, cell_size)
        pygame.display.flip()
        clock.tick(10)
    pygame.quit()

maze = read_file("test_cases_teleportation/50.txt")
path = find_paths(read_file("test_cases_teleportation/50.txt"), "?", "!")
solve_maze(maze, path)
