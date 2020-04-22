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

    def move(self, board, *args):                                           # args as 2 rackets
        """
        Move a ball by speed vector
        """
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # Ball has to recognize where are the borders of surface

        if self.rect.x < 0 or (self.rect.x + self.width) > board.surface.get_width():
            self.bounce_x()

        if self.rect.y < 0 or (self.rect.y + self.height) > board.surface.get_height():
            self.bounce_y()

        for racket in args:
            if self.rect.colliderect(racket.rect):                          # Collision of rackets and ball
                self.bounce_y()

    def reset(self):
        """
        Reset position of the ball to start position and change direction on y axis
        """
        self.rect.move(self.start_x, self.start_y)
        self.bounce_y()


class Racket(Drawable):
    """
    Racket, moves only on x axis with speed limit
    """
    def __init__(self, width, height, x, y, color=(0, 255, 0), max_speed=10):
        super(Racket, self).__init__(width, height, x, y, color)
        self.max_speed = max_speed
        self.surface.fill(color)

    def move(self, x):
        """
        Move racket to desired place
        """
        delta = x - self.rect.x
        if abs(delta) > self.max_speed:
            delta = self.max_speed if delta > 0 else -self.max_speed
        self.rect.x += delta


class AI(object):
    """
    Opponent, his racket control base on ball position
    """
    def __init__(self, racket, ball):
        self.racket = racket
        self.ball = ball

    def move(self):
        x = self.ball.rect.centerx
        self.racket.move(x)
