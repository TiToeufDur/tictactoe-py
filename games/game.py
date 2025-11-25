import pygame
pygame.init()
start_size = 30
options_size = 30
screen = pygame.display.set_mode((800,700))
cadre = pygame.image.load("images/Cadre.png")
titre = pygame.font.Font("Font/GothicPixels.ttf",80).render("The aim",False,"RED")
options = pygame.font.Font("Font/Minecraft.ttf",options_size).render("Options",False,"RED")
start = pygame.font.Font("Font/Minecraft.ttf",start_size).render("Start",False,"RED")
start_hitbox = pygame.Rect(screen.get_width()/2-start.get_width()/2,300,start.get_width(),start.get_height())

def Display():
    screen.fill("BLACK")
    screen.blit(titre,(screen.get_width()/2-titre.get_width()/2,100))
    screen.blit(start,(screen.get_width()/2-start.get_width()/2,300))
    screen.blit(options,(screen.get_width()/2-options.get_width()/2,340))
    screen.blit(cadre,(0,0))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            exit()
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
            if start_hitbox.collidepoint(mouse_pos):
                start_size = 37
                options_size = 37
            else:
                start_size = 30
                options_size = 30
            start = pygame.font.Font("Font/Minecraft.ttf",start_size).render("Start",False,"RED")
            options = pygame.font.Font("Font/Minecraft.ttf",options_size).render("Options",False,"RED")

    Display()
    pygame.display.flip()
    