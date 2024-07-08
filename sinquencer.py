import math
import sys

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
sample_rate = 1
num_samples = screen.get_width()  # sample_rate
wave = []
tau = math.pi * 2
frequency = 5.5
main_window = pygame.Rect(x_offset, y_offset, window_width, window_height)
amplitude = 100
phase = 0


def gen_wave(window):
    for x in range(num_samples):
        # time_scale = rec.width
        current_y = -math.sin(tau * x * frequency / window.width + phase) * amplitude
        print(current_y)
        wave.append(current_y)


def draw_wave(wave, window):
    for x in range(1, window.width):
        pygame.draw.circle(
            screen,
            pygame.Color("red"),
            (window.left + x, wave[x] + window.centery),
            1.0,
        )


print(list(enumerate(wave)), end="\n")

# if __name__ == "__Main__":
gen_wave(main_window)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        screen.fill("black")
        pygame.draw.line(
            screen,
            pygame.Color("grey"),
            (main_window.left - 1, main_window.centery),
            (main_window.right - 1, main_window.centery),
            1,
        )
        pygame.draw.rect(screen, pygame.Color("grey"), main_window, 1)
        draw_wave(wave, main_window)
        pygame.display.flip()
