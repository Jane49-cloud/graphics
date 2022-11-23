import pygame

pygame.init()
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (225, 255, 225)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Robot Animation")

pygame.draw.rect(screen, (0, 225, 0), (200, 166, 200, 140), 0)
pygame.draw.ellipse(screen, GREEN, (190,156, 220, 40))
pygame.draw.circle(screen, (225, 0, 0), (300, 100), 50, 0)
pygame.draw.ellipse(screen, BLUE, (210,310, 50, 30))

pygame.display.update()

clock = pygame.time.Clock()
fps = 60  # frames per second

while True:
    clock.tick(fps)
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # user presses quit button
            quit()

# animation updates


# renders
