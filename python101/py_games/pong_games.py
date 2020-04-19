from board import *
from drawable import *
import pygame
import pygame.locals


class PongGames(object):
    """
    Class to connect each component of game
    """

    def __init__(self, width, height):
        # Initialize game engine
        pygame.init()
        self.board = Board(width, height)                           # Create object from import module class

        # We use a clock to control the drawing speed game frames
        self.clock = pygame.time.Clock()
        self.ball = Ball(20, 20, width/2, height/2)                 # Add ball object in game board

    def handle_events(self):
        """
        Handling a system event, e.g mouse event.

        :return True, if pygame passed 'exit' event
        """
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return True

    def run(self):
        """
        Main loop of program
        """
        while not self.handle_events():
            # Work in loop until we receive a quit signal
            self.ball.move(self.board)
            self.board.draw(
                self.ball
            )                               # Using a method on object from imported module
            self.clock.tick(30)


if __name__ == "__main__":
    game = PongGames(800, 400)
    game.run()