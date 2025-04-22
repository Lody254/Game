


import pygame
import random
import sys
#import winsound
import time



# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Blocks")

# Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

#ISERT MUSIC
pygame.mixer.init()
pygame.mixer.music.load('song1.mp3')
pygame.mixer.music.play(loops=-1, start=10)

#winsound.PlaySound('music\background.mp3')



# Player
player_size = 60
player = pygame.Rect(WIDTH // 2, HEIGHT - player_size - 10, player_size, player_size)

# Block
block_size = 60
block = pygame.Rect(random.randint(0, WIDTH - block_size), 0, block_size, block_size)
block_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += 5

    # Move block
    block.y += block_speed
    if block.top > HEIGHT:
        block.y = 0
        block.x = random.randint(0, WIDTH - block_size)
        score += 1  # Increase score when block is dodged

    # Collision
    if player.colliderect(block):
        print("Game Over! Final Score:", score)
        pygame.mixer.music.stop()
        pygame.quit()
        sys.exit()

    # Draw everything
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, RED, block)

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()

