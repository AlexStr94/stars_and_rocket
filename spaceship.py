from curses_tools import draw_frame, read_controls, get_frame_size
import asyncio


with open("animations/rocket_frame_1.txt", "r") as my_file:
    rocket_frame_1 = my_file.read()
with open("animations/rocket_frame_2.txt", "r") as my_file:
    rocket_frame_2 = my_file.read()


async def animate_spaceship(canvas, start_row, start_column, speed=1):
    window_height, window_width = canvas.getmaxyx()
    row = start_row
    column = start_column
    rocket_height, rocket_width = get_frame_size(rocket_frame_1)
    min_row = 1
    max_row = window_height - (rocket_height + 1)
    min_column = 1
    max_column = window_width - (rocket_width + 1)

    def _coordinate_counting(row, column, rows_direction, columns_direction):
        new_row = row + rows_direction
        if new_row >= min_row and new_row <= max_row:
            row = new_row
        if new_row < min_row:
            row = min_row
        if new_row > max_row:
            row = max_row
        new_column = column + columns_direction
        if new_column >= min_column and new_column <= max_column:
            column = new_column
        if new_column < min_column:
            column = min_column
        if new_column > max_column:
            column = max_column

        return row, column

    while True:
        for i in range(10):
            draw_frame(canvas, row, column, rocket_frame_1)
            rows_direction, columns_direction, space_pressed = read_controls(canvas)
            rows_direction = rows_direction * speed
            columns_direction = columns_direction * speed
            if rows_direction != 0 or columns_direction != 0:
                draw_frame(canvas, row, column, rocket_frame_1, negative=True)
                row, column = _coordinate_counting(
                    row,
                    column,
                    rows_direction,
                    columns_direction
                )
                draw_frame(canvas, row, column, rocket_frame_1)
            await asyncio.sleep(0)

        draw_frame(canvas, row, column, rocket_frame_1, negative=True)

        for i in range(10):
            draw_frame(canvas, row, column, rocket_frame_2)
            rows_direction, columns_direction, space_pressed = read_controls(canvas)
            rows_direction = rows_direction * speed
            columns_direction = columns_direction * speed
            if rows_direction != 0 or columns_direction != 0:
                draw_frame(canvas, row, column, rocket_frame_2, negative=True)
                row, column = _coordinate_counting(
                    row,
                    column,
                    rows_direction,
                    columns_direction
                )
                draw_frame(canvas, row, column, rocket_frame_2)
            await asyncio.sleep(0)

        draw_frame(canvas, row, column, rocket_frame_2, negative=True)
