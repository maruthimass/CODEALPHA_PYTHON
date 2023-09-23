import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Colorful Snake Game")

# Initialize the clock
clock = pygame.time.Clock()

# Snake initial position and direction
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
direction = (0, -1)

# Food initial position
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Game variables
game_over = False
score = 0

# Color variables
snake_colors = [(0, 255, 0), (0, 0, 255), (255, 0, 0), (255, 255, 0)]
food_color = (255, 0, 0)

# Current color index
current_color_index = 0

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    # Update snake position
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)

    # Check for collision with food
    if snake[0] == food:
        score += 1
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        current_color_index = (current_color_index + 1) % len(snake_colors)

    else:
        snake.pop()

    # Check for collision with the wall or itself
    if (
        snake[0][0] < 0
        or snake[0][0] >= GRID_WIDTH
        or snake[0][1] < 0
        or snake[0][1] >= GRID_HEIGHT
        or snake[0] in snake[1:]
    ):
        game_over = True

    # Clear the screen
    screen.fill((0, 0, 0))  # Black background

    # Draw snake
    for i, segment in enumerate(snake):
        pygame.draw.rect(
            screen, snake_colors[(current_color_index + i) % len(snake_colors)],
            (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        )

    # Draw food
    pygame.draw.rect(
        screen, food_color, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    )

    # Update the display
    pygame.display.update()

    # Control the game speed
    clock.tick(10)

# Game over message
font = pygame.font.Font(None, 36)
text = font.render(f"Game Over - Score: {score}", True, (255, 255, 255))  # White text
text_rect = text.get_rect()
text_rect.center = (WIDTH // 2, HEIGHT // 2)
screen.blit(text, text_rect)
pygame.display.update()

# Wait for a moment before quitting
pygame.time.wait(2000)

# Quit Pygame
pygame.quit()

# Quit the program
sys.exit()

