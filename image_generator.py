from num_inp import numeric_ensure
from PIL import Image
import numpy
import math
import re

def the_equation(root_formula, x):  # I might make a thing so that you can turn a string into a formula
    return eval(root_formula)


def add_pixel(the_formula, pix, line_to_print_on, pixel_states, the_array):
    curr_pix = the_equation(the_formula, pix) % pixel_states
    the_array = numpy.insert(the_array,[line_to_print_on], curr_pix, axis=0)
    return curr_pix, the_array


def make_image(formula, zero_works, y_height, x_width):
    print("\nmaking an image for the equation:", formula, "\n")

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

    '''print("the shape of the array is:", pic_array.shape)
    print("the size of the array is:", pic_array.size)'''

    the_image = Image.fromarray(pic_array, mode="L")
    the_image.show()
    return the_image


def error_message():
    print("that does not work")


def make_executable(formula):
    formula = formula.replace(" ", "") # removes spaces

    end_mult_pattern = r"[0-9]x"
    end_match = re.search(end_mult_pattern, formula)
    while end_match:
        if end_match:
            split = end_match.end()-1
            formula = formula[:split] + "*" + formula[split:]
        end_match = re.search(end_mult_pattern, formula)

    strt_mult_patt = r"x[0-9]"
    strt_match = re.search(strt_mult_patt, formula)
    while strt_match:
        if strt_match:
            split = strt_match.start()+1
            formula = "{}*{}".format(formula[:split], formula[split:])
        strt_match = re.search(strt_mult_patt, formula)
    formula = formula.replace("^", "**")
    formula = formula.replace("", "")
    return formula


def test_eval():
    while True:
        try:
            thing_to_test = input("formula?")
            thing_to_test = make_executable(thing_to_test)
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
  'save' -- saves the last image created
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
    print("\n{} has been saved\n".format(file_name))


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
            print("\nthat is not a command I am familiar with, type 'help' to"
                  " see a list of valid commands\n")


if __name__ == "__main__":
    main()
