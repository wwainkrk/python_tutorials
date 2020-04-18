import pygame


class Board(object):
    """
    Chart for game. Is responsible for drawing game window.
    """
    def __init__(self, width, height):
        """
        Constructor method. Preparing setting for game window.
        :param width:
        :param height:  resolution of window
        """
        self.surface = pygame.display.set_mode((width, height), 0, 32)
        pygame.display.set_caption('Simple Pong')

    def draw(self, *args):
        """
        This drawing game window

        :param args: list of objects to draw
        """
        background = (230, 255, 255)
        self.surface.fill(background)

        for drawable in args:
            drawable.draw_on(self.surface)

            # Only here the actual drawing takes place
            # Before, we only decided what and how to draw
            pygame.display.update()
