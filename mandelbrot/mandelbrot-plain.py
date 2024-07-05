import os
import time

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    aspect_ratio = width / height
    pixel_width = (xmax - xmin) / (width - 1)
    pixel_height = (ymax - ymin) / (height - 1)

    # Characters used to represent different iteration counts
    gradient = ' .:-=+*#%@'

    for y in range(height):
        for x in range(width):
            real = xmin + x * pixel_width
            imag = ymin + y * pixel_height
            c = complex(real, imag)
            m = mandelbrot(c, max_iter)
	    #grad_idx = m%len(gradie
            while m < 1: 
                m = m*10
            grad_idx = m%len(gradient)
            char = gradient[grad_idx]
            print(char, end='')
        print()

def clear_terminal():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    os.environ["TERM"]="linux"
    # Initial parameters for the Mandelbrot set
    xmin, xmax = -2.0, 1.0
    ymin, ymax = -1.5, 1.5
    width, height = 80, 40  # Adjust the size for your terminal
    max_iter = 1000

    while True:
        clear_terminal()
        mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
        time.sleep(1)
        
        # Zoom in by adjusting the coordinates
        zoom_factor = 0.9
        x_center = (xmin + xmax) / 2
        y_center = (ymin + ymax) / 2
        x_range = (xmax - xmin) * zoom_factor
        y_range = (ymax - ymin) * zoom_factor
        xmin = x_center - x_range / 2
        xmax = x_center + x_range / 2
        ymin = y_center - y_range / 2
        ymax = y_center + y_range / 2

