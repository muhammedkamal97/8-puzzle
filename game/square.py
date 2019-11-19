import pygame


class Square:
    def __init__(self, screen, digit, sqr_x=100, sqr_y=100):
        self.screen = screen
        self.green = (152, 251, 152)
        self.dark_green = (0, 100, 0)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.digit = digit
        self.sqr_side = 98
        if self.digit != 0:
            self.rect = pygame.draw.rect(self.screen, self.green, (sqr_x, sqr_y, self.sqr_side, self.sqr_side))
        else:
            self.rect = pygame.draw.rect(self.screen, (255, 255, 255), (sqr_x, sqr_y, self.sqr_side, self.sqr_side))
        if self.digit != 9:
            self.text_to_screen(self.digit, self.rect.x + 40, self.rect.y + 25)

    def draw_rect(self, x, y):
        self.rect = self.rect.move(x, y)
        if self.digit != 9:
            self.text_to_screen(self.digit, self.rect.x + 40, self.rect.y + 25)
        pygame.display.update()

    def text_to_screen(self, text, x, y):
        try:
            text = str(text)
            text_surface = self.myfont.render(text, True, self.dark_green)
            self.screen.blit(text_surface, (x, y))

        except Exception as e:
            raise e
