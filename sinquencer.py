import math
import pygame
import pygame.gfxdraw

screen = pygame.display.set_mode((1280, 960))  # (1024, 768))  #
clock = pygame.time.Clock()
running = True
dt = 0
tau = math.pi * 2

# WINDOW DATA/OFFSETS #
x_offset = screen.get_width() * 0.0625
y_offset = screen.get_height() * 0.0833
main_window_width = int(screen.get_width() - x_offset * 2.0)
main_window_height = screen.get_height() * 0.625 - y_offset
main_window = pygame.Rect(x_offset, y_offset, main_window_width, main_window_height)

# WAVE DATA #
# frequency = 4.0
sample_rate = 44000

wave_data = []
color_list = [
    "grey",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "indigo",
    "violet",
    "pink",
]

waves = [
    {
        "frequency": 1,
        "amplitude": 172,
    },
    {
        "frequency": 1,
        "amplitude": 23,
    },
    {
        "frequency": 2,
        "amplitude": 23,
    },
    {
        "frequency": 3,
        "amplitude": 23,
    },
    {
        "frequency": 4,
        "amplitude": 23,
    },
    {
        "frequency": 5,
        "amplitude": 23,
    },
    {
        "frequency": 6,
        "amplitude": 23,
    },
    {
        "frequency": 7,
        "amplitude": 23,
    },
    {
        "frequency": 8,
        "amplitude": 23,
    },
]

windows = [
    {
        "rect": main_window,
        "amplitude": 172,
    },
    {
        "rect": pygame.Rect(main_window.x, main_window.bottom + 20, 128, 70),
        "amplitude": 23,  # 70 * .33,
    },
    {
        "rect": pygame.Rect(main_window.x + 142, main_window.bottom + 20, 128, 70),
        "amplitude": 23,
    },
    {
        "rect": pygame.Rect(main_window.x + 142 * 2, main_window.bottom + 20, 128, 70),
        "amplitude": 23,
    },
    {
        "rect": pygame.Rect(main_window.x + 142 * 3, main_window.bottom + 20, 128, 70),
        "amplitude": 23,
    },
    {
        "rect": pygame.Rect(main_window.x + 142 * 4, main_window.bottom + 20, 128, 70),
        "amplitude": 23,
    },
    {
        "rect": pygame.Rect(main_window.x + 142 * 5, main_window.bottom + 20, 128, 70),
        "amplitude": 23,
    },
    {
        "rect": pygame.Rect(main_window.x + 142 * 6, main_window.bottom + 20, 128, 70),
        "amplitude": 23,
    },
    {
        "rect": pygame.Rect(main_window.x + 142 * 7, main_window.bottom + 20, 128, 70),
        "amplitude": 23,
    },
]


def draw_windows():
    for i in range(9):
        pygame.gfxdraw.rectangle(
            screen,
            windows[i]["rect"],
            pygame.Color(color_list[i]),
        )


def gen_waves():
    for i in range(9):
        wave = []
        for x in range(windows[i]["rect"].width):
            time_scale = sample_rate / windows[i]["rect"].width
            current_y = -(
                math.sin(tau * waves[i]["frequency"] * x / sample_rate * time_scale)
            )
            print(f"i: {i}, x: {x}, y: {current_y}")
            wave.append(current_y)
    wave_data.append(wave)


def draw_waves():
    for i, wave in enumerate(wave_data):
        num_samples = windows[i]["rect"].width
        for x in range(num_samples):
            print(f"sample: {x}")
            pygame.draw.line(
                screen,
                color_list[i],
                (
                    windows[i]["rect"].x + x,
                    wave_data[i][abs(x - 1)]
                    + windows[i]["rect"].centery * waves[i]["amplitude"],
                ),
                (
                    windows[i]["rect"].x + x + 1,
                    wave_data[i][abs(x)]
                    + windows[i]["rect"].centery * waves[i]["amplitude"],
                ),
            )


def print_wave_data():
    for wave in wave_data:
        print(wave)


gen_waves()
print_wave_data()
while running:
    # for event in pygame.event.get():
    screen.fill("black")
    draw_windows()

    draw_waves()
    pygame.display.flip()
