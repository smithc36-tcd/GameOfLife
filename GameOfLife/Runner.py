from grid import Grid
from utils import CellState
import pygame
import time

import cProfile

def main(window, screenWidth):
    # Define the number of rows in the grid
    rows = 50

    #Create a grid object to handle the grid state 
    gridObj = Grid(rows, screenWidth, window)
    gridObj.createGrid()
    gridObj.initNeighbours()

    #Create a GUI manager to create and manage buttons
    run = False
    game = True
    gridObj.draw()

    # Create the game loop
    while game:
        # time.sleep(0.05)
        gridObj.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

            if pygame.mouse.get_pressed()[0]:
                col, row = gridObj.getCellIndex(pygame.mouse.get_pos())
                currentCell = gridObj.grid[row][col]
                currentCell.setALIVE()


            elif pygame.mouse.get_pressed()[2]:
                # Reset cell 
                col, row = gridObj.getCellIndex(pygame.mouse.get_pos())
                currentCell = gridObj.grid[row][col]
                currentCell.setDEAD()
            
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_SPACE:
                    run = True
                

            while run: 
                time.sleep(0.02)
                gridObj.updateStates()
                gridObj.draw()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        game = False
                    
                    # If the mouse is presse
                    if event.type == pygame.KEYDOWN:
                        if event.key ==  pygame.K_SPACE:
                            run = False
        
    pygame.quit()

SIZE = 800
WIDTH = SIZE
HEIGHT = SIZE
WINDOW =  pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

pygame.init()
pygame.font.init()

# cProfile.run("main(WINDOW, GRIDSIZE)")
main(WINDOW, SIZE)
