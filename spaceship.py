from curses_tools import draw_frame, read_controls
import asyncio


with open("animations/rocket_frame_1.txt", "r") as my_file:
  rocket_frame_1 = my_file.read()
with open("animations/rocket_frame_2.txt", "r") as my_file:
  rocket_frame_2 = my_file.read()

async def animate_spaceship(canvas, start_row, start_column):
    row = start_row
    column = start_column
    while True:
        for i in range(10):
            draw_frame(canvas, row, column, rocket_frame_1)
            rows_direction, columns_direction, space_pressed = read_controls(canvas)
            if rows_direction != 0 or columns_direction != 0:
                draw_frame(canvas, row, column, rocket_frame_1, negative=True)
                row += rows_direction
                column += columns_direction
                draw_frame(canvas, row, column, rocket_frame_1)
            await asyncio.sleep(0)
        
        draw_frame(canvas, row, column, rocket_frame_1, negative=True)
      
        
        for i in range(10):
            draw_frame(canvas, row, column, rocket_frame_2)
            rows_direction, columns_direction, space_pressed = read_controls(canvas)
            if rows_direction != 0 or columns_direction != 0:
                draw_frame(canvas, row, column, rocket_frame_2, negative=True)
                row += rows_direction
                column += columns_direction
                draw_frame(canvas, row, column, rocket_frame_2)
            await asyncio.sleep(0)

        draw_frame(canvas, row, column, rocket_frame_2, negative=True)