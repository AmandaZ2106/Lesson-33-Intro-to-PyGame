import pygame
pygame.init()
Screen_width,Screen_height=500,500

display_surface=pygame.display.set_mode((Screen_width,Screen_height))
pygame.display.set_caption("Adding Background image")

background_image=pygame.transform.scale(
    pygame.image.load('background.jpg').convert(),
    (Screen_width,Screen_height))

penguin_image=pygame.transform.scale(
    pygame.image.load('hello_penguin.png').convert_alpha(),(200,200))

penguin_rect=penguin_image.get_rect(center=(Screen_width//2,
                                            Screen_height//2-30))

text=pygame.font.Font(None,36).render('Hello World',True,
                                      pygame.Color('black'))

text_rect=text.get_rect(center=(Screen_width//2,Screen_height//2+110))

def game_loop():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        display_surface.blit(background_image,(0,0))
        display_surface.blit(penguin_image,penguin_rect)
        display_surface.blit(text,text_rect)
        
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if __name__=='__main__':
    game_loop()