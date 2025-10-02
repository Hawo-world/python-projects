# Snake Game Commands (Python + Git)

This file explains all the commands and functions used in the Snake Game.

---

## 🐍 Python & Pygame Commands

### Setup
- `import pygame, sys, random` → import libraries.
- `pygame.init()` → initialize all pygame modules.
- `pygame.display.set_mode((WIDTH, HEIGHT))` → create game window.
- `pygame.display.set_caption("Snake Game")` → set window title.
- `pygame.time.Clock()` → create clock to control FPS.
- `pygame.font.SysFont(None, 35)` → load font for text.

---

### Event Handling
- `pygame.event.get()` → get all events (keyboard, mouse, quit).
- `pygame.QUIT` → quit event (when window is closed).
- `pygame.KEYDOWN` → when a key is pressed.
- `pygame.K_UP / K_DOWN / K_LEFT / K_RIGHT` → arrow keys.

---

### Snake Logic
- `snake.move(grow)` → move snake, optionally grow if food eaten.
- `snake.change_direction((x, y))` → change direction.
- `snake.check_collision(WIDTH, HEIGHT)` → check wall/self collision.

---

### Food Logic
- `food.random_position()` → set new random position for food.

---

### Drawing
- `pygame.draw.rect(surface, color, rect)` → draw rectangles (snake, food).
- `font.render("Score", True, (255,255,255))` → render text.
- `window.blit(text, (x, y))` → draw text on screen.
- `pygame.display.flip()` → update the whole screen.

---

### Timing
- `clock.tick(FPS)` → control game speed (frames per second).

---

### Exiting
- `pygame.quit()` → close pygame.
- `sys.exit()` → exit program.

---

## 🐙 Git Commands

### Basic Workflow
- `cd snake_game` → move into project folder.
- `git add .` → stage all new/changed files.
- `git commit -m "Add Snake Game with Pygame"` → save snapshot with a message.
- `git push origin main` → upload changes to GitHub.

---
