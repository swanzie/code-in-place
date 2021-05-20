"""
This program generates random color filters to the different patches 
based on user inputted row and column numbers
"""

from simpleimage import SimpleImage
import random

PATCH_SIZE = 222
PATCH_NAME = 'simba-sq.jpg'

def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    It loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixel's red component by
    :param green_scale: A number to multiply each pixel's green component by
    :param blue_scale: A number to multiply each pixel's blue component by
    Returns the newly generated patch.
    '''
    patch = SimpleImage(PATCH_NAME)
    width = patch.width
    height = patch.height
    for x in range(width):
        for y in range(height):
            pixel = patch.get_pixel(x, y)
            pixel.red *= red_scale
            pixel.green *= green_scale
            pixel.blue *= blue_scale
            patch.set_pixel(x, y, pixel)
    return patch

def main():
    n_cols = int(input("Columns: "))
    n_rows = int(input("Rows: "))
    width = n_cols * PATCH_SIZE
    height = n_rows * PATCH_SIZE 

    final_image = SimpleImage.blank(width, height)
    patches = [] #list of patches

    for i in range(n_cols * n_rows):
        red_scale = random.uniform(0.0, 2.0)
        green_scale = random.uniform(0.0, 2.0)
        blue_scale = random.uniform(0.0, 2.0)
        patches.append(make_recolored_patch(red_scale, green_scale, blue_scale))
        for x in range(PATCH_SIZE):
            for y in range(PATCH_SIZE):
                pixel = patches[i].get_pixel(x, y)
                x_offset = (i % n_cols) * PATCH_SIZE
                y_offset = (i // n_cols) * PATCH_SIZE
                final_image.set_pixel((x + x_offset), (y + y_offset), pixel)

    final_image.show()

if __name__ == '__main__':
    main()