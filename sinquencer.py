import math

import pygame

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


# (Math.sin ( Tau * waves_frequency * x /
#  sampleRate * timeScale) *
#  waves[w].amplitude)
#


for x in range(window_width):
    # timeScale = ( window_width/numSamples );
    # currentY = ( Math.asin(math.tau * waves_frequency * x / sampleRate * timeScale* waves[w].amplitude)
    current_y = math.asin(((math.radians(2.0) * x / num_samples) * 1000) / 1000)
    wave.append(current_y)

print(list(enumerate(wave)))

# for x in wave
#    print(wave[x])


def draw_window(x, y, w, h):
    pygame.draw.rect(screen, "grey", (x, y, w, h), 3)


def draw_center_line(x, y, x2, y2):
    pygame.draw.line(screen, "grey", (x, y), (x2, y2), 1)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    screen.fill("black")
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
