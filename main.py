import pygame
import math

pygame.init()

font = pygame.font.SysFont(None, 36)
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

center_x = 200
center_y = 300
radius = 100
time = 0
wave = []
num_circles = 5

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                num_circles += 1
            if event.key == pygame.K_DOWN:
                num_circles = max(1, num_circles - 1)

    screen.fill((0,0,0))
    pygame.display.set_caption(f"Fourier Series Visualization - Circles: {num_circles}")

    x = center_x
    y = center_y

    for i in range(num_circles):
        prev_x = x
        prev_y = y
        n = i * 2 + 1
        radius = 75 * (4 / (n * math.pi))
        x += radius * math.cos(n * time)
        y += radius * math.sin(n * time)

        pygame.draw.circle(screen, (100,100,100), (int(prev_x), int(prev_y)), int(radius), 1)
        pygame.draw.line(screen, (255,255,255), (int(prev_x), int(prev_y)), (int(x), int(y)), 1)


    wave.insert(0,y)
    if len(wave) > 350:
        wave.pop()

    pygame.draw.circle(screen, (255,50,50), (int(x), int(y)), 5)
    pygame.draw.line(screen, (100,200,255),(x,y),(450,wave[0]),1)

    for i in range(len(wave) -1):
        pygame.draw.line(screen, (100,200,255), (450 + i + 1, wave[i]), (450 + i + 1, wave[i+1]), 1)


    time += .03
    text = font.render(f"Circles: {num_circles}", True, (255, 255, 255))
    screen.blit(text, (20,20))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()