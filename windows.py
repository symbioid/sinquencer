import pygame
import math
import logging

pygame.init()

logger = logging.getLogger(__name__)
pygame.init()
screen = pygame.display.set_mode((1280, 960))
clock = pygame.time.Clock()
running = True

tau = math.pi * 2
frequency = 1.0
amplitude = 1.0
phase = 0
sample_rate = 2400
sub_num_samples = 150
main_x_offset = 80
main_y_offset = 80
main_window_width = screen.get_width() - 160
main_window_height = int(screen.get_height() * 0.625 - main_y_offset)
main_window_scale_rate = main_window_width / sample_rate

main_window_scale_rate = main_window_width / sample_rate
sub_window_scale_rate = sub_num_samples / sample_rate

sub_window_scale_rate = sub_num_samples / sample_rate
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
