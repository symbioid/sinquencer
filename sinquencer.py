# Copyright (c) 2025 2025 by Dave Elliot is licensed under
# Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
import logging
import math
import sys
import pygame

logger = logging.getLogger(__name__)
pygame.init()
screen = pygame.display.set_mode((1280, 960))
clock = pygame.time.Clock()
running = True
main_x_offset = 80
main_y_offset = 80
main_window_width = screen.get_width() - 160
main_window_height = int(screen.get_height() * 0.625 - main_y_offset)

sub_window_width = 70
sub_window_height = 20
colors = [
    pygame.Color("red3"),
    pygame.Color("orange3"),
    pygame.Color("yellow3"),
    pygame.Color("green3"),
    pygame.Color("dodgerblue2"),
    pygame.Color("slateblue3"),
    pygame.Color("violetred3"),
]

main_window = pygame.Rect(
    main_x_offset,
    main_y_offset,
    main_window_width,
    main_window_height,
)
sub_windows = [
    # RED 0
    pygame.Rect(
        int(main_x_offset),
        int(main_y_offset + main_window_height + 50),
        int(main_x_offset + sub_window_width),
        int(main_y_offset + sub_window_height),
    ),
    # ORANGE 1
    pygame.Rect(
        int(main_x_offset + sub_window_width * 2 + 22),
        int(main_y_offset + main_window_height + 50),
        int(main_x_offset + sub_window_width),
        int(main_y_offset + sub_window_height),
    ),
    # YELLOW 2
    pygame.Rect(
        int(main_x_offset + sub_window_width * 4 + 44),
        int(main_y_offset + main_window_height + 50),
        int(main_x_offset + sub_window_width),
        int(main_y_offset + sub_window_height),
    ),
    # GREEN 3
    pygame.Rect(
        int(main_x_offset + sub_window_width * 6 + 66),
        int(main_y_offset + main_window_height + 50),
        int(main_x_offset + sub_window_width),
        int(main_y_offset + sub_window_height),
    ),
    # BLUE 4
    pygame.Rect(
        int(main_x_offset + sub_window_width * 8 + 88),
        int(main_y_offset + main_window_height + 50),
        int(main_x_offset + sub_window_width),
        int(main_y_offset + sub_window_height),
    ),
    # INDIGO 5
    pygame.Rect(
        int(main_x_offset + sub_window_width * 10 + 110),
        int(main_y_offset + main_window_height + 50),
        int(main_x_offset + sub_window_width),
        int(main_y_offset + sub_window_height),
    ),
    # VIOLET 6
    pygame.Rect(
        int(main_x_offset + sub_window_width * 12 + 132),
        int(main_y_offset + main_window_height + 50),
        int(main_x_offset + sub_window_width),
        int(main_y_offset + sub_window_height),
    ),
]

tau = math.pi * 2
frequency = 1.0
amplitude = 1.0
phase = 0
sample_rate = 2400
sub_num_samples = 150
main_window_scale_rate = main_window_width / sample_rate
sub_window_scale_rate = sub_num_samples / sample_rate


def gen_wave(freq: float) -> list[float]:
    wave_list = []
    for x in range(sample_rate):
        current_y = math.sin(tau * x * freq / sample_rate) * amplitude
        wave_list.append(current_y)

    return wave_list


def all_waves() -> list:
    g = []
    for i in range(7):
        g.append(gen_wave(i + 1))
    return g


def draw_wave(
    window: pygame.Rect, wave_list: list, scale_rate, vert_scale, color: pygame.Color
):
    for x in range(0, sample_rate):
        pygame.draw.circle(  # dot to plot the wave
            screen,
            color,
            (
                window.left + x * scale_rate,
                wave_list[x] * amplitude * vert_scale + window.centery,
            ),
            1.0,
        )


def draw_all_waves(every_wave: list):
    # draw on sub_windows
    for i, wave_list in enumerate(every_wave):
        draw_wave(
            sub_windows[i],
            wave_list,
            sub_window_scale_rate,
            sub_window_height,
            colors[i],
        )
        # draw on main_window
        draw_wave(
            main_window,
            wave_list,
            main_window_scale_rate,
            120,
            colors[i],
        )


def draw_sub_windows() -> None:
    for i, window in enumerate(sub_windows):
        """Drawing the sub-windows"""
        pygame.draw.rect(
            screen,
            colors[i],
            window,
            1,
        )

        """Drawing center lines"""
        _ = pygame.draw.lines(
            screen,
            colors[i],
            # pygame.Color("grey"),  # colors[i],
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


def draw_steps(num_steps):
    temp_x = 0
    for i in range(1, main_window_width):
        if i % (main_window_width / num_steps) == 0:
            temp_x = main_x_offset + i
            pygame.draw.line(
                screen,
                pygame.Color("grey"),
                (temp_x, main_y_offset),
                (temp_x, main_y_offset + main_window_height),
                1,
            )


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
    draw_steps(64)
    pygame.display.flip()
