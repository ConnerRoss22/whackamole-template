import pygame
import random

def draw_grid(screen):
    #Draws vertical lines
    x = 32
    while x < 640:
        pygame.draw.line(screen, "black", (x, 0 ), (x, 512))
        x += 32
    y = 32
    while y < 512:
        pygame.draw.line(screen, "black", (0, y), (640, y))
        y += 32

def determine_square(x,y):
    x_square = x//32
    y_square = y//32
    square = (x_square, y_square)








def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        mole_x_pos = 0
        mole_y_pos = 0

        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    X, Y = event.pos
                    if (mole_x_pos <= X < mole_x_pos + 32) and (mole_y_pos <= Y <mole_y_pos + 32):
                        mole_x_pos = random.randrange(0,640,32)
                        mole_y_pos = random.randrange(0,512,32)

            screen.fill("cyan")

            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x_pos, mole_y_pos)))

            draw_grid(screen)
            pygame.display.flip()
            clock.tick(60)





    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
