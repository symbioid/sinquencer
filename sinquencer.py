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
num_samples = 1024
wave = []
tau = math.pi * 2


def gen_wave():
    for x in range(sample_rate):
        time_scale = sample_rate / sample_rate
        current_y = math.sin(tau * 1 * x / sample_rate * time_scale) * 100
        print(current_y)
        wave.append(current_y)


def draw_waves(wave):  # noqa: ANN001
    for x in range(sample_rate - 1):
        pygame.draw.line(
            screen,
            pygame.Color("grey"),
            (x, wave[x] * 2 + screen.get_height() / 2),
            (x + 1, wave[x + 1] * 2 + screen.get_height() / 2),
        )


print(list(enumerate(wave)), end="\n")


gen_wave()

while running:
    for event in pygame.event.get():
        screen.fill("black")
        draw_waves(wave)
        pygame.display.flip()
        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        dt = clock.tick(60) / 1000
        # pygame.quit()
