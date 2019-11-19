import pygame


class Text:
    def __init__(self, screen, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.screen = screen

    def draw(self, value):
        rendered_text = f'{self.text}: {value}'

        font = pygame.font.SysFont('comicsans', 30)
        text = font.render(rendered_text, 1, (255, 255, 255))

        coord = self._get_coord(text)

        area = self._get_area()

        self.screen.fill(pygame.Color("black"), area)
        self.screen.blit(text, coord)

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False

    def _get_coord(self, text):
        return (self.x + (self.width / 2 - text.get_width() / 2),
                self.y + (self.height / 2 - text.get_height() / 2))

    def _get_area(self):
        return (self.x, self.y, self.width, self.height)
