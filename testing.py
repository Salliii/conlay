from conlay import *


"""
    this file is used for testing the layout and its elements

    run 'python testing.py'
"""


if __name__ == "__main__":

    # add main layout
    layout = Conlay()

    # add main box at position (0, 0) with size of (60, 20)
    main = BoldBox(0, 0, 60, 20)

    # add padding to main box
    main.padding_x = 5
    main.padding_y = 2

    # add border color to main box
    main.border_color = Color.Fg.red

    # add main box to main layout
    layout.add(main)




    # add header box at relative position (0, 0) with size of (30, 4)
    header = ThinBox(0, 0, 30, 6)

    # add header box to main box layout
    main.add(header)




    # add headline label at relative position (2, 1) with text content "test"
    headline = ThinLabel(2, 1, "test")

    # add padding to headline label
    headline.padding_x = 5
    headline.padding_y = 1

    # add background for headline box
    headline.background = True

    # add border color to headline label
    headline.border_color = Color.Fg.green

    # add headline label to header box layout
    header.add(headline)




    # add input element at relative position (2, 8)
    input_element = ThinInput(2, 8, "input:", 15)

    # set placeholder text
    input_element.placeholder = "text"

    # add input element to header box layout
    header.add(input_element)




    # print layout
    layout.print()


    # print out the content you entered in the input element
    print(input_element.content)