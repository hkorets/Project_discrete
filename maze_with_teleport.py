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
    return f"Solution: {path}"

def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = file.readlines()
        data = [i.replace("\n", "") for i in data]
    return data