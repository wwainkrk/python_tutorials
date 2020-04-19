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
    """
    Ball, she controls speed and direction itself
    """
    def __init__(self, width, height, x, y, color=(255, 0, 0), x_speed=3, y_speed=3):
        super(Ball, self).__init__(width, height, x, y, color)
        pygame.draw.ellipse(self.surface, self.color, [0, 0, self.width, self.height])  # Draw round shape on surface
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.start_x = x
        self.start_y = y

    def bounce_y(self):
        """
        Change direction on axis y to opposite
        """
        self.y_speed *= -1

    def bounce_x(self):
        """
        Change direction on axis x to opposite
        """
        self.x_speed *= -1

    def move(self):
        """
        Move a ball by speed vector
        """
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

    def reset(self):
        """
        Reset position of the ball to start position and change direction on y axis
        """
        self.rect.move(self.start_x, self.start_y)
        self.bounce_y()
