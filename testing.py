from main import *

if __name__ == "__main__":

    colay = Colay()

    main = BoldBox(10, 5, 40, 20, "\x1b[0m")
    header = BoldBox(-2, -1, 20, 10)
    header.override = False
    footer = ThinBox(-2, 6, 10, 5)

    colay.addElement(colay, main)
    main.addElement(colay, header)
    main.addElement(colay, footer)


    Cursor.setPosition(0, 100)
    print()