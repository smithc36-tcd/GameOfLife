from enum import Flag
import pygame
from utils import Colours, CellState

class Cell:
    """Defines the cell which would make up the grid"""
    def __init__(self, col, row, width, totalRows, window):
        self.row = row 
        self.col = col
        self.x = row * width
        self.y = col * width
        self.state = CellState.DEAD
        self.color = Colours.WHITE
        self.neighbours = []
        self.width = width
        self.totalRows = totalRows
        self.window = window
        self.numNeighbours = 0
    
    def getPos(self):
        return self.col, self.row

    def getState(self):
        return self.state

    def isALIVE(self):
        return self.state == CellState.ALIVE
    
    def isDEAD(self):
        return self.state == CellState.DEAD

    def setALIVE(self):
        self.state = CellState.ALIVE
        self.color = Colours.WHITE

    def setDEAD(self):
        self.state = CellState.DEAD
        self.color = Colours.BLACK

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.width))
           # pygame.display.update((self.x, self.y, self.width, self.width))
    
    def getNeighbours(self, grid):
        self.neighbours.clear()
        self.neighbours = []

        midrow = self.row 
        midcol = self.col

        left =  self.col - 1 if self.col - 1 >= 0 else self.totalRows-1
        right = self.col + 1 if self.col + 1 <= self.totalRows-1 else 0

        top = self.row - 1 if self.row - 1 >= 0 else self.totalRows-1
        bottom = self.row + 1 if self.row + 1 <= self.totalRows-1 else 0

        #Top Left
        self.neighbours.append(grid[top][left])
        #Top Mid 
        self.neighbours.append(grid[top][midcol])
        #Top Right 
        self.neighbours.append(grid[top][right])

        #Mid Left 
        self.neighbours.append(grid[midrow][left])
        #Mid Right 
        self.neighbours.append(grid[midrow][right])

        #Bottoms Left 
        self.neighbours.append(grid[bottom][left])
        #Bottom Mid 
        self.neighbours.append(grid[bottom][midcol])
        #Bottom Right
        self.neighbours.append(grid[bottom][right])

        #      #Top Left
        # self.neighbours.append(grid[left][top])
        # #Top Mid 
        # self.neighbours.append(grid[midcol][top])
        # #Top Right 
        # self.neighbours.append(grid[right][top])

        # #Mid Left 
        # self.neighbours.append(grid[left][midrow])
        # #Mid Right 
        # self.neighbours.append(grid[right][midrow])

        # #Bottoms Left 
        # self.neighbours.append(grid[left][bottom])
        # #Bottom Mid 
        # self.neighbours.append(grid[midcol][bottom])
        # #Bottom Right
        # self.neighbours.append(grid[right][bottom])

    def NeighboursAlive(self):
        self.numNeighbours = 0
        # [self.count += 1 for cell in self.neighbours if cell.isALIVE()]
        for cell in self.neighbours:
            if cell.isALIVE():
                self.numNeighbours += 1 

    def updateCell(self):
        if self.state == CellState.ALIVE:
            if self.numNeighbours < 2:
                self.setDEAD()
            elif self.numNeighbours > 3: 
                self.setDEAD()
        else:
            if self.numNeighbours == 3:
                self.setALIVE()


    def __lt__(self, other):
        return False

    def ClearNeighbours(self):
        self.neighbours.clear()

  