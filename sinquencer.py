import math

import pygame
import pygame.gfxdraw

# pygame setup
# pygame.init()

screen = pygame.display.set_mode((1280, 960))  # (1024, 768))  #
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() * 0.5, screen.get_height() * 0.5)
x_offset = screen.get_width() * 0.0625
y_offset = screen.get_height() * 0.0833
window_width = int(screen.get_width() - x_offset * 2.0)
window_height = screen.get_height() * 0.625 - y_offset
num_samples = window_width
sample_rate = num_samples
wave = [num_samples]
waves_frequency = 2.0
amplitude = 100


def gen_wave():
    for x in range(window_width):
        time_scale = window_width / num_samples
        current_y = (
            -math.sin(math.tau * waves_frequency * x / sample_rate * time_scale)
            * amplitude
        )
        wave.append(current_y)


def draw_wave():
    # pygame.draw.line(screen, "green", (0, 400), (1024, 400), 3)
    for i, x in enumerate(wave):
        # if i == 0:
        #    pass
        if i > 1:
            pygame.draw.line(
                screen,
                "orange",
                ((i - 1 + x_offset), (wave[i - 1] + y_offset + (window_height / 2))),
                ((i + x_offset), (wave[i] + y_offset + (window_height / 2))),
                10,
            )

        # print(list(enumerate(wave)), end="\n")


def draw_window(x, y, w, h):
    pygame.draw.rect(screen, "grey", (x, y, w, h), 3)


def draw_center_line(x, y, x2, y2):
    pygame.draw.line(screen, "grey", (x, y), (x2, y2), 1)


gen_wave()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    screen.fill("black")
    draw_wave()
    draw_window(x_offset, y_offset, window_width, window_height)
    draw_center_line(
        x_offset,
        y_offset + window_height / 2,
        x_offset + window_width,
        y_offset + window_height / 2,
    )

    # flip() buffers
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    # pygame.quit()
