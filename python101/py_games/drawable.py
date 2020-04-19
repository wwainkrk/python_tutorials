import pygame


class Drawable(object):
    """
    Base class for objects in draw
    """

    def __init__(self, width, height, x, y, color=(0, 255, 0)):
        self.width = width
        self.height = height
        self.color = color
        # We convert surface to desired pixel format
        self.surface = pygame.Surface([width, height], pygame.SRCALPHA, 32).convert_alpha()
        self.rect = self.surface.get_rect(x=x, y=y)                     # We take a rectangle from surface area

    def draw_on(self, surface):
        surface.blit(self.surface, self.rect)                           # We draw one image onto another


class Ball(Drawable):
