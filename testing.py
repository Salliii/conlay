from main import *

if __name__ == "__main__":

    layout = Conlay()

    main = BoldBox(0, 0, 60, 20)
    main.padding_x = 5
    main.padding_y = 2
    main.fg_color = Color.Fg.red
    main.bg_color = Color.Bg.rgb(60, 0, 0)
    main.background = True
    layout.add(main)

    header = ThinBox(0, 0, 30, 4)
    main.add(header)

    headline = ThinLabel(6, 2, "test")
    headline.padding_x = 5
    headline.padding_y = 1
    headline.background = True
    headline.fg_color = Color.Fg.green
    header.add(headline)


    layout.print()


    Cursor.show()