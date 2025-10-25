import random

# GLOBALS
ENCOUNTER_CHANCE = 50  # percentage chance of any encounter occurring

# SEEDING
#seed = random.randint(0, 1000000)
seed = 5000 # fixed value for testing
random.seed(seed)


class Path:
    def __init__(self, edge=0, start=False):
        path_types = ['Dead End', 'Straight', 'Positive Corner', 'Negative Corner', 'Fork', 'Crossroads']
        self.type = random.choice(path_types)
        while start and self.type not in ['Fork', 'Crossroads']:
            self.type = random.choice(path_types)

        while edge == 1 and self.type in ['Positive Corner', 'Fork', 'Crossroads']:
            self.type = random.choice(path_types)
        while edge == -1 and self.type in ['Negative Corner', 'Fork', 'Crossroads']:
            self.type = random.choice(path_types)



class Encounter:
    def __init__(self):
        # temp encounter list, take from encounters module later
        encounters = ['Bandits', 'Wild Animals', 'Traders', 'Travelers', 'Monsters']
        self.encounter = random.choice(encounters)
        # further details can be added here later


class Cell:
    def __init__(self, edge=0, start=False):
        self.path = Path(start=start)
        self.encounter = Encounter() if random.randint(1, 100) <= ENCOUNTER_CHANCE else None


class Map:
    def __init__(self, size=5):
        self.size = size
        self.map_grid = [[None for _ in range(size)] for _ in range(size-1)]

    def get_pointer_cells(self, row_index, col_index):
        pointer_cells = []
        if self.map_grid[row_index-1][col_index] is not None and self.map_grid[row_index-1][col_index].path.type == 'Straight':
            pointer_cells.append((row_index-1, col_index))
        
        if self.map_grid[row_index-2][col_index] is not None and self.map_grid[row_index-2][col_index].path.type == 'Crossroads':
            pointer_cells.append((row_index-2, col_index))

        if col_index > 0 and self.map_grid[row_index-1][col_index-1] is not None and self.map_grid[row_index-1][col_index-1].path.type in ['Positive Corner', 'Fork', 'Crossroads']:
            pointer_cells.append((row_index-1, col_index-1))

        if col_index < self.size - 1 and self.map_grid[row_index-1][col_index+1] is not None and self.map_grid[row_index-1][col_index+1].path.type in ['Negative Corner', 'Fork', 'Crossroads']:
            pointer_cells.append((row_index-1, col_index+1))

        return pointer_cells

    def generate_map(self):
        starting_cell = Cell(start=True)
        first_row = [None for _ in range(self.size-1)]
        first_row.insert(self.size//2, starting_cell)
        self.map_grid.insert(0,first_row)

        for row in range(1, self.size):
            for col in range(self.size):    
                pointer_cells = self.get_pointer_cells(row, col)
                if pointer_cells:
                    edge = 1 if col == self.size - 1 else -1 if col == 0 else 0
                    new_cell = Cell(edge=edge)
                    self.map_grid[row][col] = new_cell

        return self.map_grid


if __name__ == "__main__":
    game_map = Map(size=10)
    generated_map = game_map.generate_map()

    # temp basic visualiser
    for row in range(len(generated_map)-1, -1, -1):
        for col in range(len(generated_map[row])):
            cell = generated_map[row][col]
            if cell:
                encounter = cell.encounter.encounter if cell.encounter else "None"
                if cell.path.type == 'Straight':
                    print("↑", end="")
                elif cell.path.type == 'Dead End':
                    print("X", end="")
                elif cell.path.type == 'Positive Corner':
                    print("┌", end="")
                elif cell.path.type == 'Negative Corner':
                    print("┐", end="")
                elif cell.path.type == 'Fork':
                    print("Y", end="")
                elif cell.path.type == 'Crossroads':
                    print("+", end="")

                if encounter == 'Bandits':
                    print("B", end=" ")
                elif encounter == 'Wild Animals':
                    print("W", end=" ")
                elif encounter == 'Traders':
                    print("T", end=" ")
                elif encounter == 'Travelers':
                    print("R", end=" ")
                elif encounter == 'Monsters':
                    print("M", end=" ")
                else:
                    print("N", end=" ")
            else:
                print("  ", end=" ")
        print("\n", end="")