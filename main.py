import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 400, 400
    screen = pygame.display.set_mode(size)

    fps = 10
    clock = pygame.time.Clock()
    running = True
    s_r = 0
    pos = None
    while running:
        screen.fill(('blue'))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill(('blue'))
                pos = event.pos
                s_r = 0
        if pos:
            pygame.draw.circle(screen, ('yellow'), pos, s_r)
            s_r += 1
            pygame.display.flip()
            clock.tick(fps)

