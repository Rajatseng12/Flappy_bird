import pygame
import random

# Initialize the Pygame
pygame.init()

# Screen dimensions 
screen_width = 400
screen_height = 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

# Game screen  
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# Bird properties
bird_width = 40
bird_height = 40
bird_x = 50
bird_y = screen_height // 2
bird_velocity = 0
gravity = 0.5

# Pipe properties
pipe_width = 70
pipe_gap = 200
pipe_velocity = 5

# Initial pipe position
pipe_x = screen_width
pipe_height = random.randint(150, screen_height - 150 - pipe_gap)

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = -10  # Jump when space is pressed

    # Update bird position
    bird_velocity += gravity
    bird_y += bird_velocity

    # Update pipe position
    pipe_x -= pipe_velocity

    # Reset pipe when it goes off screen
    if pipe_x < -pipe_width:
        pipe_x = screen_width
        pipe_height = random.randint(150, screen_height - 150 - pipe_gap)
        score += 1

    # Check for collisions
    if bird_y < 0 or bird_y + bird_height > screen_height or (
            bird_x + bird_width > pipe_x and bird_x < pipe_x + pipe_width and 
            (bird_y < pipe_height or bird_y + bird_height > pipe_height + pipe_gap)):
        running = False  # End the game on collision

    # Drawing
    screen.fill(white)  # Clear the screen
    pygame.draw.rect(screen, green, [pipe_x, 0, pipe_width, pipe_height])
    pygame.draw.rect(screen, green, [pipe_x, pipe_height + pipe_gap, pipe_width, screen_height - pipe_height - pipe_gap])
    pygame.draw.ellipse(screen, black, [bird_x, bird_y, bird_width, bird_height])
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.update()

    # Frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
