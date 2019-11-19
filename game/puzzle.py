import time

import pygame

from game.puzzle_drawer import PuzzleDrawer
from game.button import Button
from game.text import Text


class Puzzle:
    def __init__(self, path, method):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        self.dist = 200

        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((600, 600))
        header = "Puzzle using: "+method
        pygame.display.set_caption(header)
        self.screen.fill(self.black)

        self.puzzle_drawer = PuzzleDrawer(self.screen)

        self.path = path

    def initialization(self):

        speed_button = Button(self.screen, (255, 255, 153), 450, 100, 100, 50, "1x")
        speed_button.draw((255, 255, 0))

        moves_text = Text(self.screen, 450, 170, 100, 50, "Moves")
        moves_text.draw(0)

        cost_text = Text(self.screen, 450, 240, 100, 50, "Cost")
        cost_text.draw(0)

        sleep_time = 2
        moves_count = 0
        cost_count = 0

        for state in self.path:
            self.puzzle_drawer.draw_puzzle(state)
            cost_text.draw(moves_count)
            moves_text.draw(cost_count)

            for event in pygame.event.get():

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if speed_button.is_over(pos):
                        if speed_button.text == "1x":
                            speed_button.text = "2x"
                            sleep_time = 1
                        else:
                            speed_button.text = "1x"
                            sleep_time = 2

            pygame.display.update()
            time.sleep(sleep_time)

            moves_count += 1
            cost_count += 1
