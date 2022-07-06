import asyncio
import random
import curses


async def blink(canvas, row, column, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        canvas.refresh()
        tic_amount = random.randint(5, 20)
        for i in range(tic_amount):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        canvas.refresh()
        tic_amount = random.randint(2, 5)
        for i in range(tic_amount):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        canvas.refresh()
        tic_amount = random.randint(2, 5)
        for i in range(tic_amount):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        canvas.refresh()
        tic_amount = random.randint(2, 5)
        for i in range(tic_amount):
            await asyncio.sleep(0)


def generate_stars_coordinate(window_height, window_width, stars_coordinates):
    while True:
        row = random.randint(2, window_height-3)
        column = random.randint(2, window_width-3)
        coordinate = [row, column]
        if coordinate in stars_coordinates:
            continue
        break
    return row, column
