import pygame

class Snake:
    def __init__(self, block_size, x=100, y=100):
        self.block_size = block_size
        self.body = [(x, y)]
        self.direction = (1, 0)  # moving right

    def move(self, grow=False):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x * self.block_size, head_y + dir_y * self.block_size)
        self.body.insert(0, new_head)
        if not grow:
            self.body.pop()

    def change_direction(self, new_dir):
        # Prevent reversing
        if (new_dir[0] * -1, new_dir[1] * -1) != self.direction:
            self.direction = new_dir

    def draw(self, surface, color=(0, 255, 0)):
        for segment in self.body:
            pygame.draw.rect(surface, color, (*segment, self.block_size, self.block_size))

    def check_collision(self, max_width, max_height):
        head = self.body[0]
        return (
            head in self.body[1:] or  # ran into itself
            head[0] < 0 or head[0] >= max_width or
            head[1] < 0 or head[1] >= max_height
        )

