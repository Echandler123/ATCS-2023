import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player
player_size = 40
player_pos = [0, 0]

# Classes
class_positions = {
    "Math": [random.randint(1, 8) * (WIDTH // 10), random.randint(1, 8) * (HEIGHT // 10)],
    "History": [random.randint(1, 8) * (WIDTH // 10), random.randint(1, 8) * (HEIGHT // 10)],
    "Science": [random.randint(1, 8) * (WIDTH // 10), random.randint(1, 8) * (HEIGHT // 10)],
}

# Initialize Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("School Maze Game")
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_size
    if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - player_size:
        player_pos[1] += player_size
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_size
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_size

    # Check if the player has reached a class
    for class_name, class_pos in class_positions.items():
        if player_pos == class_pos:
            print(f"You found your {class_name} class! Congratulations!")
            running = False

    # Draw everything
    screen.fill(WHITE)
    for class_pos in class_positions.values():
        pygame.draw.rect(screen, RED, (class_pos[0], class_pos[1], player_size, player_size))

    pygame.draw.rect(screen, GREEN, (WIDTH - player_size, HEIGHT - player_size, player_size, player_size))

    pygame.draw.rect(screen, BLACK, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
