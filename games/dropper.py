#Dans largeur d'ecran avec une bordure mettre le dropper a une place random et faire avancer avec y une boule qui tombe depuis le dropper
import pygame
pygame.init()

img_X = pygame.image.load("images/X.PNG")
img_O = pygame.image.load("images/O.png")
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.SysFont(None, 20)
clock = pygame.time.Clock()

dropper_x = screen_width / 2


#  CLONE CLASS
class Ball(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = img_O
        self.rect = self.image.get_rect(center=(x, 50))  # start at dropper height
        self.speed = 4  # falling speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > screen_height:
            self.kill()  # delete ball when off screen


# Sprite Group to store all balls
balls = pygame.sprite.Group()



#  DROPPER MOVEMENT
def Dropper():
    global dropper_x
    speed = 4
    key = pygame.key.get_pressed()
    if key[pygame.K_d]:
        dropper_x += speed
    if key[pygame.K_a]:
        dropper_x -= speed
    # keep dropper on screen
    dropper_x = max(0, min(dropper_x, screen_width - img_X.get_width()))
    screen.blit(img_X, (dropper_x, 30))


#  FPS DISPLAY
def Fps():
    fps = round(clock.get_fps(), 2)
    txt = font.render(f"{fps}", True, "BLACK")
    screen.blit(txt, (10, 10))



#  MAIN LOOP
playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        # SPACE → create a new falling ball
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            balls.add(Ball(dropper_x))

    screen.fill("WHITE")
    Dropper()
    balls.update()
    balls.draw(screen)
    Fps()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
