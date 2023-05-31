from main import *

if __name__ == "__main__":

    layout = Conlay()

    main = BoldBox(10, 5, 40, 20)
    main.padding_x = 5
    main.padding_y = 2
    layout.add(main)

    header = ThinBox(0, 0, 30, 4)
    main.add(header)

    headline = ThinLabel(6, 2, "headline")
    headline.padding_x = 5
    headline.padding_y = 1
    headline.background = True
    header.add(headline)


    layout.print()




    Cursor.setPosition(0, 40)
    print()
