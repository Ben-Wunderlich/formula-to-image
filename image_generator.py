from num_inp import numeric_ensure
from PIL import Image
import numpy
import math

def the_equation(root_formula, x):  # I might make a thing so that you can turn a string into a formula
    return eval(root_formula)


def add_pixel(the_formula, pix, line_to_print_on, pixel_states, the_array):
    curr_pix = the_equation(the_formula, pix) % pixel_states
    the_array = numpy.insert(the_array,[line_to_print_on], curr_pix, axis=0)
    return curr_pix, the_array


def make_image(formula, zero_works, y_height, x_width):
    PIXEL_STATES = 255
    pic_array = numpy.empty(shape=(0, x_width))
    if zero_works:
        for i in range(y_height):
            curr_line = pic_array.size // x_width
            current_pix, pic_array = add_pixel(formula, i, curr_line, PIXEL_STATES, pic_array)
    else:
        for i in range(1, y_height+1):
            curr_line = pic_array.size // x_width
            current_pix, pic_array = add_pixel(formula, i, curr_line, PIXEL_STATES, pic_array)

    print("the shape of the array is:", pic_array.shape)
    print("the size of the array is:", pic_array.size)

    le_image = Image.fromarray(pic_array, mode="L")
    le_image.show()
    return le_image


def error_message():
    print("that does not work, "
          "remember it must be structured like 2*x not 2x")


def test_eval():
    while True:
        try:
            thing_to_test = input("formula?")
            x = 0
            eval(thing_to_test)
        except SyntaxError:
            error_message()
        except NameError:
            error_message()
        except ZeroDivisionError:
            return thing_to_test, False
        else:
            return thing_to_test, True


def help_commands():
    print("""commands:
  return -- makes the image
'resize' -- change the dimensions of the image
   'new' -- change the formula used to create the image
  'quit' -- quits the program
  'save' -- saves the last image
    """)


def save_image(image):
    if image is None:
        print("you need to make an image first")
        return
    file_name = ""
    while file_name == "":
        file_name = input("name of file?")
    file_name += ".PNG"
    image.save(file_name)
    print(file_name, "has been saved")


def main():
    pic_height = 113
    pic_width = 200
    usr_choice = image = None
    formula, zero_works = test_eval()
    while usr_choice != "quit":
        usr_choice = input("What do you want to do?"
                           " Type 'help' to see the commands")
        if usr_choice == "resize":
            pic_width = numeric_ensure("what do you want the width to be?")
            pic_height = numeric_ensure("what do you want the height to be?")
        elif usr_choice == "":
            image = make_image(formula, zero_works, pic_width, pic_height)
        elif usr_choice == "new":
            formula, zero_works = test_eval()
        elif usr_choice == "help":
            help_commands()
            continue
        elif usr_choice == "save":
            save_image(image)
            continue
        elif usr_choice == "quit":
            continue
        else:
            print("that is not a command I am familiar with, type 'help' to"
                  " see a list of valid commands")


if __name__ == "__main__":
    main()
    