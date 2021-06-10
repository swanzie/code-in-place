"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage
import random

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter.
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
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    patches = [] #list of patches

    patches.append(make_recolored_patch(1.5, 0, 1.5)) #pink patch
    patches.append(make_recolored_patch(0, 1, 0.25)) #green patch
    patches.append(make_recolored_patch(1.5, 1.5, 1.5)) #brighter patch
    patches.append(make_recolored_patch(1.5, 1.5, 0)) #yellow patch
    patches.append(make_recolored_patch(1, 1, 1)) #normal patch
    patches.append(make_recolored_patch(0.25, 0.5, 1.25)) #blue patch

    for i in range(N_COLS * N_ROWS):
        # red_scale = random.uniform(0.0, 1.5)
        # green_scale = random.uniform(0.0, 1.5)
        # blue_scale = random.uniform(0.0, 1.5)
        # patches.append(make_recolored_patch(red_scale, green_scale, blue_scale))
        for x in range(PATCH_SIZE):
            for y in range(PATCH_SIZE):
                pixel = patches[i].get_pixel(x, y)
                x_offset = (i % N_COLS) * PATCH_SIZE
                y_offset = (i // N_COLS) * PATCH_SIZE
                final_image.set_pixel((x + x_offset), (y + y_offset), pixel)

    final_image.show()

if __name__ == '__main__':
    main()