import pygame
import sys

# Colors
BLACK = (0, 0, 0)
WALLS = (47, 79, 79)
EMPTY = (220, 220, 220)
PATH = (34, 139, 34)
WAY = (152, 251, 152)
TELEPORT = (144, 238, 144)
START = (255, 105, 180)

def parse_map(map_lines):
    # Parse the map lines into a 2D array
    return [list(line) for line in map_lines]

def draw_maze(screen, maze, solution):
    # Get the dimensions of each cell
    cell_width = screen.get_width() // len(maze[0])
    cell_height = screen.get_height() // len(maze)
    
    # Clear the screen
    screen.fill(BLACK)
    
    # Draw the maze
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            x = j * cell_width
            y = i * cell_height
            
            if cell == '#':
                pygame.draw.rect(screen, WALLS, (x, y, cell_width, cell_height))
            elif cell == " ":
                pygame.draw.rect(screen, EMPTY, (x, y, cell_width, cell_height))
            elif cell == '.':
                pygame.draw.rect(screen, WAY, (x, y, cell_width, cell_height))
            elif cell == "?":
                pygame.draw.rect(screen, START, (x, y, cell_width, cell_height))
    
    # Draw the solution path
    for step in solution:
        i, j = step
        x = j * cell_width
        y = i * cell_height
        pygame.draw.rect(screen, PATH, (x, y, cell_width, cell_height))

    # Update the screen
    pygame.display.flip()

# Example usage
map_lines = [
    '#######?#########',
    '#######.........#',
    '#######.#######.#',
    '#######.#######.#',
    '#######a#######.#',
    '#####       ###.#',
    'a..##       ###.#',
    '##.##       ###.#',
    '##..b       ###.#',
    '#####       ###.#',
    '#########c#####.#',
    'b.#######...###.#',
    '#.#########.###.#',
    'c.#########.....#',
    '###########!#####'
]

solution = [(0, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12), (1, 13), (1, 14), (1, 15), (2, 15), (3, 15), (4, 15), (5, 15), (6, 15), (7, 15), (8, 15), (9, 15), (10, 15), (11, 15), (12, 15), (13, 15), (13, 14), (13, 13), (13, 12), (13, 11), (14, 11)]

# Parse the map
maze = parse_map(map_lines)

# Initialize pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((len(maze[0]) * 50, len(maze) * 50))
pygame.display.set_caption("Maze Solver")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the maze and its solution
    draw_maze(screen, maze, solution)

# Exit the program
pygame.quit()
sys.exit()
