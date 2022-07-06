import random
import time
import curses

from spaceship import animate_spaceship
from stars import blink, generate_stars_coordinate


TIC_TIMEOUT = 0.1


def draw(canvas):
    window_height, window_width = canvas.getmaxyx()
    coroutines = []

    stars = '+*.:'
    stars_coordinates = []
    for i in range(100):
        row, column = generate_stars_coordinate(
            window_height,
            window_width,
            stars_coordinates
        )
        stars_coordinates.append([row, column])
        star = random.choice(stars)
        coroutines.append(blink(canvas, row, column, star))

    spaceship_position = [window_height/2, window_width/2]
    spaceship = animate_spaceship(
        canvas,
        spaceship_position[0],
        spaceship_position[1],
        speed=4
    )
    coroutines.append(spaceship)

    canvas.border()
    canvas.nodelay(True)
    curses.curs_set(False)
    while True:
        for coroutine in coroutines:
            try:
                coroutine.send(None)
            except StopIteration:
                coroutines.remove(coroutine)
                canvas.border()
        canvas.refresh()
        time.sleep(TIC_TIMEOUT)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
