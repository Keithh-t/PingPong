import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
FONT = pygame.font.SysFont('Arial', 36)

# Paddle dimensions
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100

# Ball dimensions
BALL_RADIUS = 7

# Speeds
PADDLE_SPEED = 7
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game with Scoring")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Define paddles using Rect objects
paddle1 = pygame.Rect(10, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - 20, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Define the ball using a Rect object
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS,
                   BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y

# Scores
score1 = 0
score2 = 0

# Main game loop
running = True
while running:
    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current state of all keyboard buttons
    keys = pygame.key.get_pressed()
    # Player 1 movement (W/S keys)
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += PADDLE_SPEED
    # Player 2 movement (Up/Down arrow keys)
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
        paddle2.y += PADDLE_SPEED

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1  # Reverse the Y direction

    # Ball collision with paddles
    if ball.colliderect(paddle1) and ball_speed_x < 0:
        ball_speed_x *= -1  # Reverse the X direction
    if ball.colliderect(paddle2) and ball_speed_x > 0:
        ball_speed_x *= -1  # Reverse the X direction

    # Check for scoring
    if ball.left <= 0:
        score2 += 1  # Player 2 scores
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= -1  # Serve to the scoring player
    if ball.right >= WIDTH:
        score1 += 1  # Player 1 scores
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= -1  # Serve to the scoring player

    # Clear the screen
    screen.fill(BLACK)

    # Draw paddles, ball, and center line
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Render the scores
    score_text = FONT.render(f"{score1}    {score2}", True, WHITE)
    text_rect = score_text.get_rect(center=(WIDTH // 2, 50))
    screen.blit(score_text, text_rect)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame and close the window
pygame.quit()
sys.exit()
