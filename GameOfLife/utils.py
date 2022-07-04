from enum import IntEnum

class Colours:
    """Defining Colours used"""
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 128, 255)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    PURPLE = (128, 0, 128)
    ORANGE = (255, 165 ,0)
    GREY = (128, 128, 128)
    LIGHTGREY = (200,200,200)
    TURQUOISE = (64, 224, 208)

class CellState(IntEnum):
    """Defining cell states #"""
    DEAD = 0 #(255, 255, 255) # WHITE
    ALIVE = 1 #(0, 0, 0) # BLACK
