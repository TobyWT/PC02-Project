import pygame
pygame.init()
window = pygame.display.set_mode((500, 500))





def quit_game():
    global run_game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False


run_game = True
while run_game:
    quit_game()

pygame.quit()
