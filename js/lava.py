import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
FPS = 60
FENCE_WIDTH = 50
GRAVITY = 1
JUMP_STRENGTH = 15
MOVE_SPEED = 5  # Speed at which the sheep moves left or right

# Colors
BROWN = (139, 69, 19)
SKY_BLUE = (135, 206, 250)
GREEN = (0, 255, 0)  # Ground color

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sheep Jumping Game")

# Game variables
clock = pygame.time.Clock()
score = 0
game_started = False
sheep_x = SCREEN_WIDTH // 2 - 25  # Center the sheep horizontally
sheep_y = SCREEN_HEIGHT // 2 - 50  # Initial position of the sheep
sheep_velocity_y = 0
fence_height = random.randint(50, 150)  # Initial random height for the fence
fence_x = SCREEN_WIDTH  # Start position of the fence

def reset_game():
    global score, game_started, sheep_y, sheep_velocity_y, fence_height, fence_x
    score = 0
    game_started = True
    sheep_y = SCREEN_HEIGHT // 2 - 50
    sheep_velocity_y = 0
    fence_height = random.randint(50, 150)  # Reset fence height
    fence_x = SCREEN_WIDTH  # Reset fence position

def draw_fence():
    pygame.draw.rect(screen, BROWN, (fence_x, SCREEN_HEIGHT - fence_height, FENCE_WIDTH, fence_height))

def check_collision():
    sheep_rect = pygame.Rect(sheep_x, sheep_y, 50, 50)  # Sheep rectangle
    fence_rect = pygame.Rect(fence_x, SCREEN_HEIGHT - fence_height, FENCE_WIDTH, fence_height)  # Fence rectangle
    return sheep_rect.colliderect(fence_rect)

# Main game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(SKY_BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_started:
                    reset_game()
                else:
                    sheep_velocity_y = -JUMP_STRENGTH
            if event.key == pygame.K_r and not game_started:
                reset_game()  # Reset the game if it's over

    if game_started:
        # Update sheep position
        sheep_velocity_y += GRAVITY
        sheep_y += sheep_velocity_y

        # Allow the sheep to fall to the ground
        if sheep_y > SCREEN_HEIGHT - 20:
            sheep_y = SCREEN_HEIGHT - 20
            sheep_velocity_y = 0

        # Move the fence towards the left
        fence_x -= MOVE_SPEED

        # Check if the fence is off the screen
        if fence_x < -FENCE_WIDTH:
            # Reset fence position and increase score
            fence_x = SCREEN_WIDTH
            fence_height = random.randint(50, 150)  # Randomize the height of the new fence
            score += 1  # Increase score when the fence is passed

        # Check for collisions
        if check_collision():
            game_started = False  # End the game if the sheep touches the fence

    # Draw the fence
    draw_fence()

    # Draw sheep
    pygame.draw.rect(screen, (255, 255, 255), (sheep_x, sheep_y, 50, 50))  # Draw sheep as a white rectangle

    # Draw score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    if not game_started:
        font = pygame.font.Font(None, 48)
        start_text = font.render('Game Over! Press SPACE to Restart', True, (255, 255, 255))
        screen.blit(start_text, (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 + 30))

    pygame.display.flip()

pygame.quit()