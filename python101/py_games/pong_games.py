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
        self.ball = Ball(width=20, height=20, x=width/2, y=height/2)                 # Add ball object in game board
        self.player1 = Racket(width=80, height=20, x=width/2, y=height/2)            # Racket for player

    def handle_events(self):
        """
        Handling a system event, e.g mouse event.

        :return True, if pygame passed 'exit' event
        """
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return True

            if event.type == pygame.locals.MOUSEMOTION:
                # Mouse moves control first player moves
                x, y = event.pos
                self.player1.move(x)

    def run(self):
        """
        Main loop of program
        """
        while not self.handle_events():
            # Work in loop until we receive a quit signal
            self.ball.move(self.board, self.player1)
            self.board.draw(
                self.ball,
                self.player1
            )                               # Using a method on object from imported module
            self.clock.tick(30)


if __name__ == "__main__":
    game = PongGames(800, 400)
    game.run()
