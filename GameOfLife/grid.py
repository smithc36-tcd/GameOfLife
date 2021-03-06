import pygame
import json
from cell import Cell
from utils import Colours

class Grid:
    def __init__(self,rows, screenWidth, window):
        self.rows = rows
        self.cellWidth = screenWidth // rows
        self.screenWidth = screenWidth
        self.window = window
        self.grid = []

    def createGrid(self):
        """Create the grid of size rows"""
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.rows):
                cell = Cell(j, i, self.cellWidth, self.rows, self.window)
                cell.setDEAD()
                self.grid[i].append(cell)

    def drawGrid(self):
        """Draw lines to the grid"""
        for i in range(self.rows):
            pygame.draw.line(self.window, Colours.GREY, (0, i * self.cellWidth), (self.screenWidth, i * self.cellWidth))
            pygame.draw.line(self.window, Colours.GREY, (i*self.cellWidth, 0),(i*self.cellWidth, self.screenWidth))

    def draw(self):
        #self.window.fill(Colours.WHITE)

        [cell.draw() for row in self.grid for cell in row]
        #pygame.draw.line(self.window, Colours.GREY, (self.screenWidth, 0),(self.screenWidth, self.screenWidth))
        self.drawGrid()
        pygame.display.update()

    def getCellIndex(self, mousePosition):
        """Returns the index of cell from a clicked mouse position"""
        x, y = mousePosition

        row = x // self.cellWidth
        col = y // self.cellWidth

        return col, row

    def updateStates(self):
        [cell.NeighboursAlive() for row in self.grid for cell in row]
        [cell.updateCell() for row in self.grid for cell in row]

    def initNeighbours(self):
        [cell.getNeighbours(self.grid) for row in self.grid for cell in row]

   