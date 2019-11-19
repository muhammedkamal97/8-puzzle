from game.square import Square


class PuzzleDrawer:
    def __init__(self, screen):
        self.screen = screen

    def draw_puzzle(self, digits):
        counter_x = 1
        counter_y = 1
        puzzle = []
        for digit in digits:
            puzzle.append(Square(self.screen, digit, 100 * counter_x, 100 * counter_y))
            counter_x += 1
            if counter_x % 4 == 0:
                counter_x = 1
                counter_y += 1

        return puzzle
