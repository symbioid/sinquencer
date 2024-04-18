import math

import pygame
import pygame.gfxdraw

pygame.init()

screen = pygame.display.set_mode((1280, 960))  # (1024, 768))  #
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() * 0.5, screen.get_height() * 0.5)
x_offset = screen.get_width() * 0.0625
y_offset = screen.get_height() * 0.0833
window_width = int(screen.get_width() - x_offset * 2.0)
window_height = screen.get_height() * 0.625 - y_offset
sample_rate = 44000
num_samples = 44000
wave = []
waves_frequency = 2.0
wave_data_array = []


color_array = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "white"]
waves_array = [
    {"frequency": 9, "amplitude": 100},
    {"frequency": 1, "amplitude": 22},
    {"frequency": 2, "amplitude": 22},
    {"frequency": 3, "amplitude": 22},
    {"frequency": 4, "amplitude": 22},
    {"frequency": 5, "amplitude": 22},
    {"frequency": 6, "amplitude": 22},
    {"frequency": 7, "amplitude": 22},
    {"frequency": 8, "amplitude": 22},
]
windows_array = [
    {
        "x_off": x_offset,
        "y_off": y_offset,
        "width": window_width,
        "height": window_height,
        "color": "darkgrey",
    },
    {
        "x_off": x_offset + (window_width / 8) * 0,
        "y_off": y_offset + window_height + 20,
        "width": window_width / 8,
        "height": window_height / 8,
        "color": "red",
    },
    {
        "x_off": x_offset + (window_width / 8) * 1,
        "y_off": y_offset + window_height + 20,
        "width": window_width / 8,
        "height": window_height / 8,
        "color": "orange",
    },
    {
        "x_off": x_offset + (window_width / 8) * 2,
        "y_off": y_offset + window_height + 20,
        "width": window_width / 8,
        "height": window_height / 8,
        "color": "yellow",
    },
    {
        "x_off": x_offset + (window_width / 8) * 3,
        "y_off": y_offset + window_height + 20,
        "width": window_width / 8,
        "height": window_height / 8,
        "color": "green",
    },
    {
        "x_off": x_offset + (window_width / 8) * 4,
        "y_off": y_offset + window_height + 20,
        "width": window_width / 8,
        "height": window_height / 8,
        "color": "blue",
    },
    {
        "x_off": x_offset + (window_width / 8) * 5,
        "y_off": y_offset + window_height + 20,
        "width": window_width / 8,
        "height": window_height / 8,
        "color": "indigo",
    },
    {
        "x_off": x_offset + (window_width / 8) * 6,
        "y_off": y_offset + window_height + 20,
        "width": window_width / 8,
        "height": window_height / 8,
        "color": "violet",
    },
    {
        "x_off": x_offset + (window_width / 8) * 7,
        "y_off": y_offset + window_height + 20,
        "width": window_width / 8,
        "height": window_height / 8,
        "color": "white",
    },
]


def gen_wave():
    for x in range(window_width):
        time_scale = sample_rate / window_width
        current_y = (
            -math.sin(
                math.tau * waves_array[0]["frequency"] * x / sample_rate * time_scale
            )
            * waves_array[0]["amplitude"]
        )
        wave.append(current_y)


def gen_waves():
    for i, w in enumerate(waves_array):
        for x in range(int(windows_array[i]["width"])):
            time_scale = sample_rate / windows_array[i]["width"]
            current_y = (
                -math.sin(math.tau * w["frequency"] * x / sample_rate * time_scale)
                * w["amplitude"]
            )
            wave.append(current_y)
        wave_data_array.append(wave)

    print(list(enumerate(wave_data_array)), end="\n")


def draw_waves(waves_array):  # noqa: ANN001
    for wave in waves_array:
        for i, x in enumerate(wave):
            if i == 0:
                pass
            if i > 1:
                pygame.draw.line(
                    screen,
                    "grey",
                    (
                        (i - 1 + x_offset),
                        (wave[i - 1] + y_offset + (window_height / 2)),
                    ),
                    ((i + x_offset), (wave[i] + y_offset + (window_height / 2))),
                    1,
                )
            # print(list(enumerate(wave)), end="\n")


# def draw_window(x, y, w, h):
#    pygame.draw.rect(screen, "darkgrey", (x - 3, y - 3, w + 6, h + 6), 1)
#    draw_center_line(
#        x_offset,
#        y_offset + window_height / 2,
#        x_offset + window_width,
#        y_offset + window_height / 2,
#    )


def draw_windows():
    for i, waves in enumerate(windows_array):
        pygame.draw.rect(
            screen,
            waves["color"],
            (
                waves["x_off"],
                waves["y_off"],
                waves["width"],
                waves["height"],
            ),
            1,
        )
        draw_center_line(
            waves["x_off"],
            waves["y_off"] + waves["height"] / 2,
            waves["x_off"] + waves["width"],
            waves["y_off"] + waves["height"] / 2,
            waves["color"],
        )


def draw_center_line(x, y, x2, y2, c="grey"):
    pygame.draw.line(screen, c, (x, y), (x2, y2), 1)


## ----------------------------------------------------------------------------------- ##
## ----------------------------------------------------------------------------------- ##

gen_waves()
while running:
    for event in pygame.event.get():
        screen.fill("black")
        draw_windows()
        draw_waves(wave_data_array)
        # flip() buffers
        pygame.display.flip()
        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000
        # pygame.quit()
