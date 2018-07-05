from num_inp import numeric_ensure
from PIL import Image
import numpy
import math

def the_equation(x):  # I might make a thing so that you can turn a string into a formula
    return 1/(x+1)


def add_pixel(pix, line_to_print_on):
    global pic_array
    curr_pix = the_equation(pix) % PIXEL_STATES
    pic_array = numpy.insert(pic_array,[line_to_print_on], curr_pix, axis=0)


HOW_MANY_PIXELS = 400
PIXEL_STATES = 255
PIXELS_PER_LINE = 400
pic_array = numpy.empty(shape=(0, PIXELS_PER_LINE))

for i in range(HOW_MANY_PIXELS):
    curr_line = pic_array.size // PIXELS_PER_LINE
    print("current line is", curr_line)
    add_pixel(i, curr_line)

print("the array contains:", pic_array)
print("the shape of the array is:", pic_array.shape)
print("the size of the array is:", pic_array.size)

le_image = Image.fromarray(pic_array, mode="L")
#le_image.save("1 over x.PNG")
le_image.show()



#for _ in range(100):
#    for _ in range(100):

