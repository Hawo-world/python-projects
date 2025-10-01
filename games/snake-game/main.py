import pygame, sys
from snake import Snake
from food import Food

pygame.init()

# Window settings
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
FPS = 10

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
snake = Snake(BLOCK_SIZE)
food = Food(BLOCK_SIZE, WIDTH, HEIGHT)
score = 0

font = pygame.font.SysFont(None, 35)

def draw_score():
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    window.blit(text, [10, 10])

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0, -1))
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, 1))
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-1, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((1, 0))

    # Move snake
    grow = False
    if snake.body[0] == food.position:
        grow = True
        food.position = food.random_position()
        score += 1

    snake.move(grow)

    # Check collision
    if snake.check_collision(WIDTH, HEIGHT):
        running = False

    # Draw
    window.fill((0, 0, 0))
    snake.draw(window)
    food.draw(window)
    draw_score()
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()

