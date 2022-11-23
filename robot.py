import pygame
import os

pygame.font.init()
font = pygame.font.SysFont(' comicsans', 40)

pygame.init()

# colors
CHROME_WHITE = (199, 196, 185)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robot Animation")

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'back.jpg')), (WIDTH, HEIGHT))

ROBOT_Head = pygame.image.load(os.path.join("assets", "images.png"))
ROBOT_Head = pygame.transform.scale(ROBOT_Head, (90, 90))
ROBOT_BODY = pygame.image.load(os.path.join("assets", "body.png"))
ROBOT_BODY = pygame.transform.scale(ROBOT_BODY, (140, 140))
ROBOT_RIGHT_HAND_Upper = pygame.image.load(os.path.join("assets", 'hand.jpg'))
ROBOT_RIGHT_HAND_Upper = pygame.transform.rotate(pygame.transform.scale(ROBOT_RIGHT_HAND_Upper, (30, 100)), -10)
ROBOT_LEFT_HAND_Upper = pygame.image.load(os.path.join("assets", 'hand.jpg'))
ROBOT_LEFT_HAND_Upper = pygame.transform.rotate(pygame.transform.scale(ROBOT_LEFT_HAND_Upper, (30, 100)), 10)
ROBOT_RIGHT_HAND = pygame.image.load(os.path.join("assets", 'hand.jpg'))
ROBOT_RIGHT_HAND = pygame.transform.rotate(pygame.transform.scale(ROBOT_RIGHT_HAND, (30, 120)), 10)
ROBOT_LEFT_HAND = pygame.image.load(os.path.join("assets", 'hand.jpg'))
ROBOT_LEFT_HAND = pygame.transform.rotate(pygame.transform.scale(ROBOT_LEFT_HAND, (30, 120)), -10)
ROBOT_RIGHT_LEG = pygame.image.load(os.path.join("assets", 'leg.png'))
ROBOT_RIGHT_LEG = pygame.transform.rotate(pygame.transform.scale(ROBOT_RIGHT_LEG, (30, 150)), -23)
ROBOT_LEFT_LEG = pygame.image.load(os.path.join("assets", 'leg.png'))
ROBOT_LEFT_LEG = pygame.transform.rotate(pygame.transform.scale(ROBOT_LEFT_LEG, (30, 150)), 10)


def draw_window():
    WIN.blit(SPACE, (0, 0))
    WIN.blit(ROBOT_Head, (277, 20))
    WIN.blit(ROBOT_BODY, (255, 110))
    WIN.blit(ROBOT_RIGHT_HAND_Upper, (210, 110))
    WIN.blit(ROBOT_LEFT_HAND_Upper, (390, 110))
    WIN.blit(ROBOT_RIGHT_HAND, (210, 210))
    WIN.blit(ROBOT_LEFT_HAND, (390, 210))
    WIN.blit(ROBOT_RIGHT_LEG, (228, 240))
    WIN.blit(ROBOT_LEFT_LEG, (350, 245))
    WIN.blit(button.surface, (10, 10))
    pygame.display.update()


class Button:
    def __init__(self, text):
        self.text = font.render(text, 1, CHROME_WHITE)
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.blit(self.text, (0, 0))



button = Button("Animate")


def main():
    clock = pygame.time.Clock()
    clock.tick(60)  # fps
    pos = pygame.mouse.get_pos()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if button:
            if pygame.mouse.get_pressed()[0] ==1:
                pygame.transform.rotate(ROBOT_LEFT_HAND_Upper, -20)
        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
