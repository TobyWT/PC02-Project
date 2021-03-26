import pygame

pygame.init()
window = pygame.display.set_mode((500, 500))
char = pygame.image.load("Illustration3.png")
rect = char.get_rect()
obstacle = pygame.Rect(100, 100, 40, 40)
moveLeft = True
moveRight = True
moveDown = True
moveUp = True


def quit_game():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


def still_collided():
    global moveRight
    global moveLeft
    global moveUp
    global moveDown
    if not rect.colliderect(obstacle):
        moveDown = True
        moveUp = True
        moveLeft = True
        moveRight = True


def collision_check():
    global moveRight
    global moveLeft
    global moveUp
    global moveDown
    if rect.colliderect(obstacle):
        if rect.bottom - obstacle.top <= 10:
            moveDown = False
        if rect.top - obstacle.bottom <= 10:
            moveUp = False
        if rect.right - obstacle.left <= 10:
            moveRight = False
        if rect.left - obstacle.right <= 10:
            moveLeft = False

        # print("collision detected")


def draw():
    window.fill((255, 255, 255))
    window.blit(char, rect)
    pygame.draw.rect(window, (255, 0, 0), obstacle)
    pygame.display.update()


vel = 1
run = True
while run:
    pygame.time.delay(30)
    still_collided()
    user_input = pygame.key.get_pressed()
    if user_input[pygame.K_LEFT] and moveLeft:
        rect.x -= vel
    if user_input[pygame.K_RIGHT] and moveRight:
        rect.x += vel
    if user_input[pygame.K_UP] and moveUp:
        rect.y -= vel
    if user_input[pygame.K_DOWN] and moveDown:
        rect.y += vel
    collision_check()
    quit_game()
    draw()
pygame.quit()
