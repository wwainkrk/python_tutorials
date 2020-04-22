import pygame


class Judge(object):
    """
    Game judge class
    """

    def __init__(self, ball, board, *args):
        self.ball = ball
        self.board = board
        self.rackets = args
        self.score = [0, 0]

        # Before start writing some scores/texts, we have to initialize font chosing mechanism
        pygame.font.init()
        font_path = pygame.font.match_font('arial')
        self.font = pygame.font.Font(font_path, 64)

    def update_score(self):
        """
        Give a point for rackets
        :param board_height: surface height
        """
        if self.ball.rect.y < self.rackets[0].rect.y:
            self.score[0] += 1
            self.ball.reset()
        elif self.ball.rect.y > self.rackets[1].rect.y:
            self.score[1] += 1
            self.ball.reset()

    def draw_text(self, surface, text, x, y):
        """
        Draw text in pointed place
        :param surface: object where we want to draw our text
        :param text:    text
        :param x:       x position for text
        :param y:       y position for text
        """
        text = self.font.render(text, True, (150, 150, 150))
        rect = text.get_rect()
        rect.center = x, y
        surface.blit(text, rect)

    def draw_on(self, surface):
        """
        Update and draw scores
        """
        height = self.board.surface.get_height()
        self.update_score()

        width = self.board.surface.get_width()
        self.draw_text(surface, "Computer: {}".format(self.score[1]), width / 2, height * 0.3)
        self.draw_text(surface, "Player: {}".format(self.score[0]), width / 2, height * 0.7)
