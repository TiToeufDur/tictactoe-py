import pygame
pygame.init()
screen = pygame.display.set_mode((800,700))
cadre = pygame.image.load("images/Cadre.png")
titre = pygame.font.Font("Font/GothicPixels.ttf",80).render("The aim",False,"RED")
options = pygame.font.Font("Font/Minecraft.ttf",30).render("Options",False,"RED")
start = pygame.font.Font("Font/Minecraft.ttf",30).render("Start",False,"RED")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            exit()
    
    screen.blit(titre,(screen.get_width()/2-titre.get_width()/2,100))
    screen.blit(start,(screen.get_width()/2-start.get_width()/2,300))
    screen.blit(options,(screen.get_width()/2-options.get_width()/2,340))
    screen.blit(cadre,(0,0))
    pygame.display.flip()
    