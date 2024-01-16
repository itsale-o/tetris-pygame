from settings import *
from sys import exit
from game import Game
from score import Score
from preview import Preview
from random import choice
from os.path import join

class Main:
    def __init__(self):
        # general
        pygame.init()
        icon = pygame.image.load('./assets/img-font/tetris-icon.png')
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Tetris")
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

        # Shapes
        self.next_shapes = [choice(list(TETROMINOS.keys())) for shape in range(3)]
        # Components
        self.game = Game(self.get_next_shape, self.update_score)
        self.score = Score()
        self.preview = Preview()

        # Audio
        self.music = pygame.mixer.Sound(join('.', 'assets', 'sounds', 'music.wav'))
        self.music.play(-1)

    def update_score(self, lines, score, level):
        self.score.lines = lines
        self.score.score = score
        self.score.level = level

    def get_next_shape(self):
        next_shape = self.next_shapes.pop(0)
        self.next_shapes.append(choice(list(TETROMINOS.keys())))
        return next_shape

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            # display
            self.display_surface.fill(GRAY)

            # components
            self.game.run()
            self.score.run()
            self.preview.run(self.next_shapes)

            # updating
            pygame.display.update()
            self.clock.tick()

if __name__ == '__main__':
    main = Main()
    main.run()
        
            