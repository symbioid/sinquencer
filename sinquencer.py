import sys
import math
import pygame
import pygame.gfxdraw

pygame.init()

screen = pygame.display.set_mode((1280, 960))  # (1024, 768))  #
clock = pygame.time.Clock()
running = True
dt = 0
x_offset = screen.get_width() * 0.0625
y_offset = screen.get_height() * 0.0833
window_width = int(screen.get_width() - x_offset * 2.0)
window_height = screen.get_height() * 0.625 - y_offset
sample_rate = screen.get_width()
num_samples = sample_rate
wave = []
tau = math.pi * 2
frequency = 10.0
vcenter = screen.get_width() / 2
ycenter = screen.get_height() / 2


def gen_wave():
    for x in range(num_samples):
        time_scale = screen.get_width() / sample_rate
        current_y = -math.sin(tau * frequency * x / sample_rate * time_scale) * 100
        print(current_y)
        wave.append(current_y)


def draw_waves(wave):  # noqa: ANN001
    for x in range(screen.get_width() - 1):
        pygame.draw.line(
            screen,
            pygame.Color("red"),
            (x, wave[x] + ycenter),
            (x + 1, wave[x + 1] + ycenter),
        )


print(list(enumerate(wave)), end="\n")


# if __name__ == "__Main__":
gen_wave()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        screen.fill("black")
        pygame.draw.line(
            screen, pygame.Color("grey"), (0, ycenter), (screen.get_width(), ycenter)
        )
        draw_waves(wave)
        pygame.display.flip()
