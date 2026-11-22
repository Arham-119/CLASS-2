import math
import os
import random
import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27
LEVEL_UP_EVERY = 5  # new background + faster enemies every 5 points

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Backgrounds (add as many files as you like to this list)
BACKGROUND_FILES = ['background.png', 'background2.png', 'background3.png', 'background4.png']
backgrounds = []
for filename in BACKGROUND_FILES:
    if os.path.exists(filename):
        img = pygame.image.load(filename)
        backgrounds.append(pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)))
if not backgrounds:
    # Safety net so the game still runs if no image files are found
    backgrounds.append(pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)))
background_index = 0

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Sound (just one: background music)
pygame.mixer.music.load('background.wav')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)  # -1 = loop forever
muted = False

# Player
playerImg = pygame.image.load('player.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))  # 64 is the size of the enemy
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
small_font = pygame.font.Font('freesansbold.ttf', 18)
textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)
game_over = False

def show_score(x, y):
    # Display the current score on the screen.
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def show_hints():
    # Show level and the mute/background keys
    level = small_font.render("Level " + str(score_value // LEVEL_UP_EVERY + 1), True, (255, 255, 255))
    screen.blit(level, (10, 50))
    label = "Sound: OFF (M)" if muted else "Sound: ON (M)"
    sound_text = small_font.render(label, True, (255, 255, 255))
    screen.blit(sound_text, (SCREEN_WIDTH - 150, 10))
    bg_text = small_font.render("Background (B)", True, (255, 255, 255))
    screen.blit(bg_text, (SCREEN_WIDTH - 150, 32))

def game_over_text():
    # Display the game over text
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    # Draw the player on the screen
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    # Draw an enemy on the screen
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    # Fire a bullet from the player's position
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    # Check if there is a collision between the enemy and a bullet
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE

def next_background():
    # Switch to the next background image
    global background_index
    background_index = (background_index + 1) % len(backgrounds)

def level_up():
    # New background and faster enemies
    next_background()
    for k in range(num_of_enemies):
        direction = 1 if enemyX_change[k] > 0 else -1
        enemyX_change[k] = direction * (abs(enemyX_change[k]) + 1)

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(backgrounds[background_index], (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready" and not game_over:
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
            if event.key == pygame.K_b:
                next_background()
            if event.key == pygame.K_m:
                muted = not muted
                if muted:
                    pygame.mixer.music.pause()
                elif not game_over:
                    pygame.mixer.music.unpause()
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            playerX_change = 0

    # Player Movement
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64))  # 64 is the size of the player

    # Enemy Movement
    for i in range(num_of_enemies):
        if enemyY[i] > 340:  # Game Over Condition
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            if not game_over:
                game_over = True
                pygame.mixer.music.stop()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = abs(enemyX_change[i])
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_change[i] = -abs(enemyX_change[i])
            enemyY[i] += enemyY_change[i]

        # Collision Check
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
            score_value += 1
            if score_value % LEVEL_UP_EVERY == 0:
                level_up()
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

        enemy(enemyX[i], enemyY[i], i)

    if game_over:
        game_over_text()

    # Bullet Movement
    if bulletY <= 0:
        bulletY = PLAYER_START_Y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    show_hints()
    pygame.display.update()