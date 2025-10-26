import random
from allies import Allies
from enemies import Enemy
from Player import *    

# GLOBALS
ENCOUNTER_CHANCE = 50  # percentage chance of any encounter occurring

# SEEDING
#seed = random.randint(0, 1000000)
#seed = 5000 # fixed value for testing
#random.seed(seed)

class Encounter:
    def __init__(self, encounter=None):
        encounters = Allies.__subclasses__() + Enemy.__subclasses__()
        self.encounter = encounter if encounter and encounter in encounters else random.choice(encounters)

class Cell:
    def __init__(self, visible=False, edge=0, start=False, end=False):
        
        path_types = ['Dead End', 'Straight', 'Positive Corner', 'Negative Corner', 'Fork', 'Crossroads']
        self.path = 'Dead End' if end else random.choice(path_types)

        while start and self.path not in ['Fork', 'Crossroads']:
            self.path = random.choice(path_types)

        while edge == 1 and self.path in ['Positive Corner', 'Fork', 'Crossroads']:
            self.path = random.choice(path_types)
        
        while edge == -1 and self.path in ['Negative Corner', 'Fork', 'Crossroads']:
            self.path = random.choice(path_types)
        
        self.start = start
        self.visited = start
        self.visible = visible or start

        self.encounter = Encounter() if random.randint(1, 100) <= ENCOUNTER_CHANCE else None
        
    
    def get_valid_directions(self):
        directions = []
        if not self.start:
            directions.append('down')
        if self.path in ['Straight', 'Crossroads']:
            directions.append('up')
        if self.path in ['Positive Corner', 'Fork', 'Crossroads']:
            directions.append('right')
        if self.path in ['Negative Corner', 'Fork', 'Crossroads']:
            directions.append('left')
        return directions


class Map:
    def __init__(self, size=5):
        self.size = size
        self.map_grid = [[None for _ in range(size)] for _ in range(size-1)]

        starting_cell = Cell(start=True)
        first_row = [None for _ in range(self.size-1)]
        first_row.insert(self.size//2, starting_cell)
        self.map_grid.insert(0,first_row)

        for row in range(1, self.size):
            temp_row = [None for _ in range(self.size)]
            end = row == self.size - 1
            while all(cell is None or (cell.path == 'Dead End' and not end) for cell in temp_row):
                for col in range(self.size):
                    pointer_cells = self.get_pointer_cells(row, col)
                    if pointer_cells:
                        edge = 1 if col == self.size - 1 else -1 if col == 0 else 0
                        visible = any(self.map_grid[pc[0]][pc[1]].visited for pc in pointer_cells)
                        new_cell = Cell(visible=visible, edge=edge, end=end)
                        temp_row[col] = new_cell
            self.map_grid[row] = temp_row

    def get_cell(self, row_index, col_index):
        if 0 <= row_index < self.size and 0 <= col_index < self.size:
            return self.map_grid[row_index][col_index]
        return None

    # get all cells that point to the given cell
    def get_pointer_cells(self, row_index, col_index):
        pointer_cells = []
        if self.map_grid[row_index-1][col_index] is not None and \
                self.map_grid[row_index-1][col_index].path == 'Straight':
            pointer_cells.append((row_index-1, col_index))
        
        elif self.map_grid[row_index-2][col_index] is not None and \
                self.map_grid[row_index-2][col_index].path == 'Crossroads':
            pointer_cells.append((row_index-2, col_index))

        if col_index > 0 and self.map_grid[row_index-1][col_index-1] is not None and \
                self.map_grid[row_index-1][col_index-1].path in ['Positive Corner', 'Fork', 'Crossroads']:
            pointer_cells.append((row_index-1, col_index-1))

        if col_index < self.size - 1 and self.map_grid[row_index-1][col_index+1] is not None and \
                self.map_grid[row_index-1][col_index+1].path in ['Negative Corner', 'Fork', 'Crossroads']:
            pointer_cells.append((row_index-1, col_index+1))

        return pointer_cells
    
    # get all cells that the given cell points to
    def get_pointing_cells(self, row_index, col_index):
        pointing_cells = []
        shape = self.map_grid[row_index][col_index].path

        if shape == 'Straight':
            if row_index + 1 < self.size and self.map_grid[row_index + 1][col_index] is not None:
                pointing_cells.append((row_index + 1, col_index))
        
        elif shape == 'Crossroads':
            if row_index + 2 < self.size and self.map_grid[row_index + 2][col_index] is not None:
                pointing_cells.append((row_index + 2, col_index))
        
        if shape in ['Positive Corner', 'Fork', 'Crossroads']:
            if row_index + 1 < self.size and col_index + 1 < self.size and \
                    self.map_grid[row_index + 1][col_index + 1] is not None:
                pointing_cells.append((row_index + 1, col_index + 1))
        
        if shape in ['Negative Corner', 'Fork', 'Crossroads']:
            if row_index + 1 < self.size and col_index - 1 >= 0 and \
                    self.map_grid[row_index + 1][col_index - 1] is not None:
                pointing_cells.append((row_index + 1, col_index - 1))
        
        return pointing_cells

    def visit_cell(self, row_index, col_index):
        cell = self.map_grid[row_index][col_index]
        if cell:
            cell.visited = True
            for pc in self.get_pointing_cells(row_index, col_index):
                self.map_grid[pc[0]][pc[1]].visible = True

    def row_has_visible_cells(self, row_index):
        return any(cell and cell.visible for cell in self.map_grid[row_index-1])
    
    def get_visible_map(self):
        visible_map = []
        for row in range(self.size):
            visible_row = []
            for col in range(self.size):
                cell = self.map_grid[row][col]
                if cell and cell.visible:
                    visible_row.append(cell)
                else:
                    visible_row.append(None)
            
            if all(c is None for c in visible_row):
                return visible_map
            visible_map.append(visible_row)
        
        return visible_map

    def get_valid_coords(self):
        valid_coords = []
        for row in range(self.size):
            for col in range(self.size):
                cell = self.map_grid[row][col]
                if cell:
                    valid_coords.append((row, col))
        return valid_coords
    
    def change_encounter(self, row, col, new_encounter):
        if (row, col) not in self.get_valid_coords():
            raise ValueError("Invalid cell coordinates.")
        
        cell = self.map_grid[row][col]
        if cell:
            cell.encounter = Encounter(encounter=new_encounter)

    def display_map(self, visible_only=True):
        map = self.get_visible_map() if visible_only else self.map_grid
        for row in range(len(map)-1, -1, -1):
            for col in range(len(map[row])):
                cell = map[row][col]
                if cell:
                    if (visible_only and cell.visited) or not visible_only:
                        encounter = cell.encounter.encounter if cell.encounter else None
                        if cell.path == 'Straight':
                            print("↑", end="")
                        elif cell.path == 'Dead End':
                            print("X", end="")
                        elif cell.path == 'Positive Corner':
                            print("┌", end="")
                        elif cell.path == 'Negative Corner':
                            print("┐", end="")
                        elif cell.path == 'Fork':
                            print("Y", end="")
                        elif cell.path == 'Crossroads':
                            print("+", end="")

                        if encounter:
                            print(f"[{encounter.__name__.upper()}]", end=" ")
                        else:
                            print("[N]", end=" ")
                    elif visible_only and cell.visible: 
                        print("[?]", end=" ")
                else:
                    print("  ", end=" ")
            print("\n", end="")


if __name__ == "__main__":
    game_map = Map(size=10)
    game_map.display_map(False)
