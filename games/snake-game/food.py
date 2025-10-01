import pygame, random

class Food:
    def __init__(self, block_size, max_width, max_height):
        self.block_size = block_size
        self.max_width = max_width
        self.max_height = max_height
        self.position = self.random_position()

    def random_position(self):
        x = random.randrange(0, self.max_width, self.block_size)
        y = random.randrange(0, self.max_height, self.block_size)
        return (x, y)

    def draw(self, surface, color=(255, 0, 0)):
        pygame.draw.rect(surface, color, (*self.position, self.block_size, self.block_size))

