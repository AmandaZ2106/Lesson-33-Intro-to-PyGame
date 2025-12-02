import pygame
pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My first game screen")

GREY = (58, 58, 58)

image = pygame.image.load("my_image.jpg")  
image = pygame.transform.scale(image, (300, 300))

image_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(GREY) 
    screen.blit(image, image_rect)  

    pygame.display.flip()
    clock.tick(60)

pygame.quit()