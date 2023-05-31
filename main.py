class Border:
    vertical = u""
    horizontal = u""
    top_left = u""
    top_right = u""
    bottom_left = u""
    bottom_right = u""


class Bold(Border):
    def __init__(self):
        self.vertical = u"\u2503"
        self.horizontal = u"\u2501"
        self.top_left = u"\u250F"
        self.top_right = u"\u2513"
        self.bottom_left = u"\u2517"
        self.bottom_right = u"\u251B"


class Thin(Border):
    def __init__(self):
        self.vertical = u"\u2502"
        self.horizontal = u"\u2500"
        self.top_left = u"\u256D"
        self.top_right = u"\u256E"
        self.bottom_left = u"\u2570"
        self.bottom_right = u"\u256F"




class Console(object):
    def reset() -> int:
        print("\x1bc", end="")
        return 1


    def clear() -> int:
        print("\x1b[3J", end="")
        return 1




class Cursor(object):   
    def setPosition(x:int, y:int) -> int:
        print("\x1b[{y};{x}H".format(y=y, x=x), end="")
        return 1


    def shiftHorizontal(sh: int) -> int:
        if sh < 0:
            print("\x1b[{sh}D".format(sh=sh*-1), end="")
            return 1
        elif sh > 0:
            print("\x1b[{sh}C".format(sh=sh), end="")
            return 1
        return 0


    def shiftVertikal(sh:int) -> int:
        if sh < 0:
            print("\x1b[{sh}A".format(sh=sh*-1), end="")
            return 1
        elif sh > 0:
            print("\x1b[{sh}B".format(sh=sh), end="")
            return 1
        return 0
    

    def hide() -> int:
        print("\x1b[?25l", end="")
        return 1
    
    
    def show() -> int:
        print("\x1b[?25h", end="")
        return 1




class Conlay(object):

    struct = {}

    Console.reset()
    Cursor.setPosition(0, 0)

    def __init__(self) -> None:
        self.relative_x = int()
        self.relative_y = int()
        self.absolute_x = int()
        self.absolute_y = int()
        self.width = int()
        self.height = int()
        self.zindex = int()
        self.padding_x = int()
        self.padding_y = int()


    def __sort_struct_by_x__(self, x, reverse=False) -> dict:
        return dict(sorted(self.struct.items(), key=lambda elem: elem[1][x], reverse=reverse))


    def add(self, child:None) -> int: #LayoutElement
        child.absolute_x = self.absolute_x + self.padding_x + child.relative_x
        child.absolute_y = self.absolute_y + self.padding_y + child.relative_y

        self.struct[child] = {
            "absolute_x": child.absolute_x,
            "absolute_y": child.absolute_y,
            "width": child.width,
            "height": child.height,
            "zindex": child.zindex,
            "parent": self
            }
        return 1
    

    def print(self) -> int:
        for element, attr in self.__sort_struct_by_x__("zindex").items():

            for y in range(element.height):
                Cursor.setPosition(element.absolute_x, element.absolute_y + y)

                for x in range(element.width):
                    if x == 0 and y == 0:
                        print(element.border.top_left, end="")
                    elif x == 0 and y == element.height - 1:
                        print(element.border.bottom_left, end="")
                    elif x == element.width - 1 and y == 0:
                        print(element.border.top_right, end="")
                    elif x == element.width - 1 and y == element.height - 1:
                        print(element.border.bottom_right, end="")

                    elif x == 0 or x == element.width - 1:
                        print(element.border.vertical, end="")
                    elif y == 0 or y == element.height - 1:
                        print(element.border.horizontal, end="")

                    else:
                        Cursor.shiftHorizontal(1)




class LayoutElement(Conlay):
    def __init__(self, x:int, y:int, w:int, h:int, border:Border) -> None:
        super().__init__()

        self.relative_x = x
        self.relative_y = y
        self.width = w
        self.height = h
        self.border = border


class ThinBox(LayoutElement):
    def __init__(self, x:int, y:int, w:int, h:int) -> None:
        super().__init__(x, y, w, h, Thin())


class BoldBox(LayoutElement):
    def __init__(self, x:int, y:int, w:int, h:int) -> None:
        super().__init__(x, y, w, h, Bold())