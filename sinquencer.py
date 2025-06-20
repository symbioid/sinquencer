# Copyright (c) 2025 2025 by Dave Elliot is licensed under
# Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
import math
import sys
import pygame
import windows


def gen_wave(freq: float) -> list[float]:
    wave_list = []
    for x in range(windows.sample_rate):
        current_y = (
            math.sin(windows.tau * x * freq / windows.sample_rate) * windows.amplitude
        )
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
    for x in range(0, windows.sample_rate):
        pygame.draw.circle(  # dot to plot the wave
            windows.screen,
            color,
            (
                window.left + x * scale_rate,
                wave_list[x] * windows.amplitude * vert_scale + window.centery,
            ),
            1.0,
        )


def draw_all_waves(every_wave: list):
    # draw on sub_windows
    for i, wave_list in enumerate(every_wave):
        draw_wave(
            windows.sub_windows[i],
            wave_list,
            windows.sub_window_scale_rate,
            windows.sub_window_height,
            windows.colors[i],
        )
        # draw on main_window
        draw_wave(
            windows.main_window,
            wave_list,
            windows.main_window_scale_rate,
            120,
            windows.colors[i],
        )


def draw_sub_windows() -> None:
    for i, window in enumerate(windows.sub_windows):
        """Drawing the sub-windows"""
        pygame.draw.rect(
            windows.screen,
            windows.colors[i],
            window,
            1,
        )

        """Drawing center lines"""
        _ = pygame.draw.lines(
            windows.screen,
            windows.colors[i],
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
        windows.screen,
        pygame.Color("grey"),
        (windows.main_window.left - 1, windows.main_window.centery),
        (windows.main_window.right - 1, windows.main_window.centery),
        1,
    )
    pygame.draw.rect(windows.screen, pygame.Color("grey"), windows.main_window, 1)


def draw_steps(num_steps):
    temp_x = 0
    for i in range(1, windows.main_window_width):
        if i % (windows.main_window_width / num_steps) == 0:
            temp_x = windows.main_x_offset + i
            pygame.draw.line(
                windows.screen,
                pygame.Color("grey"),
                (temp_x, windows.main_y_offset),
                (temp_x, windows.main_y_offset + windows.main_window_height),
                1,
            )


waves = all_waves()

while windows.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    windows.screen.fill("black")
    draw_main_window()
    draw_sub_windows()
    draw_all_waves(waves)
    draw_steps(16)
    pygame.display.flip()
