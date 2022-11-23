import pygame

pygame.init()
pygame.display.init()

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Robot Animation')

clock = pygame.time.Clock()
FPS = 60  # Frames per second.
x = ''
y=''

# Some shortcuts for colors
WHITE = (255, 0, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)

# For example, display a white rect
rect = pygame.Rect((250, 250), (32, 32))
image = pygame.Surface((32, 32))
image.fill(WHITE)
circle_image =pygame.Surface((400, 400))
circle_image.fill(ORANGE)
pygame.draw.circle(circle_image,(0,0,0),(200, 200), 5)

# Game loop
while True:
    # Ensure game runs at a constant speed
    clock.tick(FPS)

    # 1. Handle events
    for event in pygame.event.get():
        # User pressed the close button ?
        if event.type == pygame.QUIT:
            quit()
            # Close the program. Other methods like 'raise SystemExit' or 'sys.exit()'.
            # Calling 'pygame.quit()' won't close the program! It will just uninitialize the modules.

    # 2. Put updates to the game logic here

    # 3. Render
    win.fill(BLACK)  # first clear the screen
    win.blit(image, rect)  # draw whatever you need
    win.blit(circle_image, 50,50)
    pygame.display.flip()  # copy to screen
