import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shooting Game")

# Load background image
background = pygame.image.load("bg.png")

# Load player image
player_image = pygame.image.load("icon.png")

# Load enemy image
enemy_image = pygame.image.load("enemy.png")

# Load bullet image
bullet_image = pygame.image.load("bullet.png")

# Set player position and movement speed
player_x = 50
player_y = SCREEN_HEIGHT/2
player_speed = 5

# Set enemy position and movement speed
enemy_x = SCREEN_WIDTH-50
enemy_y = random.randint(50, SCREEN_HEIGHT-50)
enemy_speed = 3

# Set bullet position and movement speed
bullet_x = 0
bullet_y = SCREEN_HEIGHT/2
bullet_speed = 10
bullet_state = "ready"

# Set score and font
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

# Function to display score on screen
def show_score(x, y):
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (x, y))

# Function to draw player on screen
def draw_player(x, y):
    screen.blit(player_image, (x, y))

# Function to draw enemy on screen
def draw_enemy(x, y):
    screen.blit(enemy_image, (x, y))

# Function to fire bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (x, y))

# Function to check collision between bullet and enemy
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = ((enemy_x - bullet_x)**2 + (enemy_y - bullet_y)**2)**0.5
    if distance < 27:
        return True
    else:
        return False

# Game loop
running = True
while running:
    # Fill screen with background image
    screen.blit(background, (0, 0))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x + 50
                    bullet_y = player_y + 25
                    fire_bullet(bullet_x, bullet_y)

    # Move player up/down
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    elif keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT-50:
        player_y += player_speed

    # Move enemy left
    enemy_x -= enemy_speed
    if enemy_x < 0:
        enemy_x = SCREEN_WIDTH-50
        enemy_y = random.randint(50, SCREEN_HEIGHT-50)

    # Fire bullet
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_x += bullet_speed
        if bullet_x > SCREEN_WIDTH:
            bullet_state = "ready"

    # Check collision between bullet and enemy
    collision = is_collision(enemy_x, enemy_y, bullet_x, bullet_y)
    if collision:
        bullet_state = "ready"
        bullet_x = 0
        bullet_y = SCREEN_HEIGHT / 2
        enemy_x = SCREEN_WIDTH - 50
        enemy_y = random.randint(50, SCREEN_HEIGHT - 50)
        score += 1

        # Draw player, enemy, and score on screen
    draw_player(player_x, player_y)
    draw_enemy(enemy_x, enemy_y)
    show_score(10, 10)

    # Update screen
    pygame.display.update()
pygame.quit()
