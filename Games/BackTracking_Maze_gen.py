import random
import pygame

height, width = 512, 512

cell_size = 16
wall_color = (123, 123, 244)
cols, rows = width//cell_size, height//cell_size
window = pygame.display.set_mode((width+1, height+1))

def index(row, column):
    #returns the index of a 2d array to a 1d array
    if (row >= 0 and row < rows) and (column >= 0 and column < cols):
        return (row*cols + column)

class Cell:
    #maze object and contains the current cell
    maze = None
    current_cell = None

    def __init__(self, column, row):
        self.column = column
        self.row = row
        self.x = column * cell_size
        self.y = row * cell_size
        self.walls = [True, True, True, True]
        self.visited = False

    #draws the cell out of lines and a 'visited' rectangle
    def draw_cell(self):
        if self.walls[0]:
            #top : top left -> top right
            pygame.draw.line(window, (wall_color), (self.x, self.y), (self.x+cell_size, self.y), 1)
        if self.walls[1]:
            #right : top right -> bottom left
            pygame.draw.line(window, (wall_color), (self.x+cell_size, self.y), (self.x+cell_size, self.y+cell_size), 1)
        if self.walls[2]:
            #bottom : bottom left -> bottom right
            pygame.draw.line(window, (wall_color), (self.x, self.y+cell_size), (self.x+cell_size, self.y+cell_size), 1)
        if self.walls[3]:
            #left : top left -> bottom left
            pygame.draw.line(window, (wall_color), (self.x, self.y), (self.x, self.y+cell_size), 1)

        if self.visited:
            pygame.draw.rect(window, (23,23,87, 200), pygame.Rect(self.x+1, self.y+1, cell_size+1, cell_size+1))
            #pygame.draw.rect(window, (67,45,98), pygame.Rect(self.x+1, self.y+1, cell_size+1, cell_size+1))
        
    #the paramter is a cell object
    def remove_wall(self, chosen):
        x = chosen.column - self.column
        y = chosen.row - self.row
        if x == 1:
            self.walls[1] = False
            chosen.walls[3] = False
        if x == -1:
            self.walls[3] = False
            chosen.walls[1] = False
        if y == -1:
            self.walls[0] = False
            chosen.walls[2] = False
        if y == 1:
            self.walls[2] = False
            chosen.walls[0] = False

    def check_neighbors(self):
        self.visited = True
        self.neighbors = (
            index(self.row-1, self.column),
            index(self.row, self.column+1),
            index(self.row+1, self.column),
            index(self.row, self.column-1),
            )
        self.neighbors = tuple(filter(lambda cell : cell != None and Cell.maze.grid[cell].visited == False, self.neighbors))
        if len(self.neighbors) > 0:
            chosen_cell = Cell.maze.grid[random.choice(self.neighbors)]
            self.remove_wall(chosen_cell)
            return chosen_cell

class Maze:
    def __init__(self):
        self.grid = tuple(Cell(row, column) for column in range(cols) for row in range(rows)) 
        self.stack = []
        
clock = pygame.time.Clock()
running = True
Cell.maze = Maze()

Cell.current_cell = Cell.maze.grid[random.randint(0,len(Cell.maze.grid))]
paused = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                maze = Maze()
                Cell.maze = maze
                Cell.current_cell = Cell.maze.grid[random.randint(0,len(Cell.maze.grid))]
    chosen_cell = Cell.current_cell.check_neighbors()
    for cell in Cell.maze.grid:
        cell.draw_cell()
    pygame.draw.rect(window, (123,123,123), pygame.Rect(Cell.current_cell.x+1, Cell.current_cell.y+1, cell_size+1, cell_size+1))
    if chosen_cell != None:
        
        Cell.maze.stack.append(Cell.current_cell)
        Cell.current_cell = chosen_cell
    else:
        if len(Cell.maze.stack) > 0:
            Cell.current_cell = Cell.maze.stack.pop()
    
    pygame.display.update()
    window.fill((0,0,0))
    clock.tick(30)

pygame.quit()
