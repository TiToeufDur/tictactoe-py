import pygame
import random
pygame.init()
#Dans largeur d'ecran avec une bordure mettre le dropper a une place random et faire avancer avec y une boule qui tombe depuis le dropper
X = pygame.image.load("images/X.PNG")
screen_lenght = 900
screen_height = 700
screen = pygame.display.set_mode((screen_lenght,screen_height))
font = pygame.font.SysFont(None, 20)
clock = pygame.time.Clock()
position_x = screen_lenght/2


def Dropper():
    global position_x
    key = pygame.key.get_pressed()
    if key[pygame.K_d]:
        position_x += 4
    elif key[pygame.K_a]:
        position_x -= 4
    screen.blit(X,(position_x,30))    

def Fps():
    fps = round(clock.get_fps(),2)
    fps_text = font.render(f"{fps}", True,"BLACK")
    screen.blit(fps_text, (10, 10)) 





playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        

    screen.fill("WHITE")
    Dropper()
    Fps()
    pygame.display.flip()
    clock.tick(60)

pygame.quit