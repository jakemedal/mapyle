"""Curses User Interface


"""

import curses
from curses.wrapper import wrapper

class CursesUI():
    def start_ui(self):
        curses.wrapper(CursesUI.main)


    def main(self):
        self.stdscr = curses.initscr()
        rando = CursesView([[2,3,4,5,6][3,4,5,5,3,2]], 1, 1, 10, 10)
        while True:
            rando.print_to_term(self.stdscr)

class CursesView():
    def __init__(self, blocks, min_height, min_width, x, y):
        self.blocks = blocks
        self.min_height = min_height
        self.min_width = min_width
        self.x = x
        self.y = y

    def print_to_term(self, stdscr):
        for i, row in enumerate(self.blocks):
            for j, col in enumerate(self.blocks):
                stdscr.addstr(i + self.x, j + self.y, col, self.blocks[row][col])
        stdscr.refresh()
