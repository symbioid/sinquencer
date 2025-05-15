# Copyright (c) 2025 2025 by Dave Elliot is licensed under
# Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International

from dataclasses import dataclass
import logging
import math
import sys
import pygame

logger = logging.getLogger(__name__)
pygame.init()

screen = pygame.display.set_mode((1280, 960))  # (1024, 768))  #
clock = pygame.time.Clock()
running = True
main_x_offset = 80
main_y_offset = 80
main_window_width = screen.get_width() - 160
main_window_height = screen.get_height() * 0.625 - main_y_offset

small_window_width = 70
small_window_height = 20
colors = [
    pygame.Color("red"),
    pygame.Color("orange"),
    pygame.Color("yellow"),
    pygame.Color("green"),
    pygame.Color("blue"),
    pygame.Color("indigo"),
    pygame.Color("violet"),
]

main_window = pygame.Rect(
    main_x_offset,
    main_y_offset,
    main_window_width,
    main_window_height,
)
small_windows = [
    # RED 1
    pygame.Rect(
        int(main_x_offset),
        int(main_y_offset + main_window_height + 50),
        int(main_x_offset + small_window_width),
        int(main_y_offset + small_window_height),
    ),
    # ORANGE 2
    pygame.Rect(
        int(main_x_offset + small_window_width * 2 + 22),
        int(main_y_offset + main_window_height + 50),
        int(main_x_offset + small_window_width),
        int(main_y_offset + small_window_height),
    ),
    # YELLOW 3
    pygame.Rect(
        int(main_x_offset + small_window_width * 4 + 44),
        int(main_y_offset + main_window_height + 50),
        int(main_x_offset + small_window_width),
        int(main_y_offset + small_window_height),
    ),
    # GREEN 4
    pygame.Rect(
        int(main_x_offset + small_window_width * 6 + 66),
        int(main_y_offset + main_window_height + 50),
        int(main_x_offset + small_window_width),
        int(main_y_offset + small_window_height),
    ),
    # BLUE 5
    pygame.Rect(
        int(main_x_offset + small_window_width * 8 + 88),
        int(main_y_offset + main_window_height + 50),
        int(main_x_offset + small_window_width),
        int(main_y_offset + small_window_height),
    ),
    # INDIGO 6
    pygame.Rect(
        int(main_x_offset + small_window_width * 10 + 110),
        int(main_y_offset + main_window_height + 50),
        int(main_x_offset + small_window_width),
        int(main_y_offset + small_window_height),
    ),
    # VIOLET 7
    pygame.Rect(
        int(main_x_offset + small_window_width * 12 + 132),
        int(main_y_offset + main_window_height + 50),
        int(main_x_offset + small_window_width),
        int(main_y_offset + small_window_height),
    ),
]

tau = math.pi * 2
frequency = 1.0
amplitude = 150
phase = 0
sample_rate = main_window.width
num_samples = sample_rate


@dataclass
class wave():
    wave_data: list
    freq: float = 0.0
    amp: float = small_window_height * .289
    phase: float = 0.0

def gen_wave(window: pygame.Rect, frequency: float, phase: float) -> list:
    wave = []
    for x in range(num_samples):
        current_y = math.sin(tau * x * frequency /
                             sample_rate + phase) * amplitude
        logger.info(current_y)
        wave.append(current_y)
    return wave

def all_waves() -> list:
    g = []
    for i in range(6):
        g.append(gen_wave(main_window, 1, i))
    return g

def draw_wave(wave: list, color: pygame.Color):
    # (instead scale wave to window, dont chop off) !!!
    # for x in range(1, num_samples):
    for x in range(2, num_samples):
        pygame.draw.circle(  # dot to plot the wave
            screen,
            color,
            (main_window.left + x, -wave[x] + main_window.centery),
            1.0,
        )

def draw_all_waves(all_waves: list):
    # draw on main screen
    for i, wave in enumerate(all_waves):
        draw_wave(wave, colors[i])

def draw_sub_windows() -> None:
    for i, window in enumerate(small_windows):
        pygame.draw.rect(
            screen,
            colors[i],
            window,
            1,
        )
        pygame.draw.lines(
            screen,
            pygame.Color("grey"),  # colors[i],
            False,
            (
                (window.left - 1, window.centery),
                (window.right - 1, window.centery),
            ),
            1,
        )

def draw_main_window() -> None:
    pygame.draw.line(
        screen,
        pygame.Color("grey"),
        (main_window.left - 1, main_window.centery),
        (main_window.right - 1, main_window.centery),
        1,
    )
    pygame.draw.rect(screen, pygame.Color("grey"), main_window, 1)


waves = all_waves()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        screen.fill("black")
        draw_main_window()
        draw_sub_windows()
        draw_all_waves(waves)
        pygame.display.flip()
