import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
FPS = 60
SHEEP_WIDTH = 50
SHEEP_HEIGHT = 50
FENCE_WIDTH = 50
FENCE_HEIGHT = 20
GRAVITY = 1
JUMP_STRENGTH = 15

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
SKY_BLUE = (135, 206, 250)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sheep Jumping Game")

# Game variables
clock = pygame.time.Clock()
score = 0
high_score = 0
game_over = False
sheep_y = SCREEN_HEIGHT - SHEEP_HEIGHT
sheep_velocity_y = 0
fences = []
fence_timer = 0

def reset_game():
    global score, game_over, sheep_y, sheep_velocity_y, fences
    score = 0
    game_over = False
    sheep_y = SCREEN_HEIGHT - SHEEP_HEIGHT
    sheep_velocity_y = 0
    fences.clear()

def draw_sheep(x, y):
    # Draw sheep as a white rectangle with a black outline
    pygame.draw.rect(screen, BLACK, (x, y, SHEEP_WIDTH, SHEEP_HEIGHT), 2)  # Outline
    pygame.draw.rect(screen, WHITE, (x + 2, y + 2, SHEEP_WIDTH - 4, SHEEP_HEIGHT - 4))  # Body

def draw_fences():
    for fence in fences:
        pygame.draw.rect(screen, BROWN, fence)

def check_collision():
    sheep_rect = pygame.Rect(100, sheep_y, SHEEP_WIDTH, SHEEP_HEIGHT)
    for fence in fences:
        if sheep_rect.colliderect(fence):
            return True
    return False

# Main game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(SKY_BLUE)  # Sky blue background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                sheep_velocity_y = -JUMP_STRENGTH
            if event.key == pygame.K_r and game_over:
                reset_game()

    if not game_over:
        # Update sheep position
        sheep_velocity_y += GRAVITY
        sheep_y += sheep_velocity_y

        # Prevent sheep from falling below the ground
        if sheep_y > SCREEN_HEIGHT - SHEEP_HEIGHT:
            sheep_y = SCREEN_HEIGHT - SHEEP_HEIGHT

        # Add fences
        fence_timer += 1
        if fence_timer > 60:  # Add a fence every second
            fence_height = SCREEN_HEIGHT - random.randint(50, 150)
            fences.append(pygame.Rect(SCREEN_WIDTH, fence_height, FENCE_WIDTH, FENCE_HEIGHT))
            fence_timer = 0

        # Move fences
        for fence in fences:
            fence.x -= 5  # Move fence to the left
            if fence.x < 0:
                fences.remove(fence)
                score += 1  # Increase score when fence is passed

        # Check for collisions
        if check_collision():
            game_over = True
            high_score = max(high_score, score)

    # Draw sheep
    draw_sheep(100, sheep_y)

    # Draw fences
    draw_fences()

    # Draw score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    high_score_text = font.render(f'High Score: {high_score}', True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(high_score_text, (10, 50))

    if game_over:
        game_over_text = font.render('Game Over! Press R to Retry', True, (0, 0, 0))
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2))

    pygame.display.flip()

pygame.quit()