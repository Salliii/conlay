class Type:
    vertical = u""
    horizontal = u""
    top_left = u""
    top_right = u""
    bottom_left = u""
    bottom_right = u""


class Bold(Type):
    def __init__(self):
        self.vertical = u"\u2503"
        self.horizontal = u"\u2501"
        self.top_left = u"\u250F"
        self.top_right = u"\u2513"
        self.bottom_left = u"\u2517"
        self.bottom_right = u"\u251B"


class Thin(Type):
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
            print("\x1b[{sh}D".format(sh=sh), end="")
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




class Element(object):
    def __init__(self) -> None:
        self.absx = int()
        self.absy = int()
        self.relx = int()
        self.rely = int()
        self.w = int()
        self.h = int()

        self.absolute = False
        self.override = False


    def addElement(self, main:object, child:object):
        main.struct.append(child)

        if not child.absolute:
            child.absx = child.relx + self.absx
            child.absy = child.rely + self.absy
        child.__set__(main.struct)




class Colay(Element):
    def __init__(self) -> None:
        super().__init__()
        Console.reset()
        Cursor.setPosition(0, 0)

        self.struct = []




class Box(Element):
    def __init__(self, x:int, y:int, w:int, h:int, type:Type, color="\x1b[0m") -> None:
        super().__init__()
        self.absx = x
        self.absy = y
        self.relx = x
        self.rely = y
        self.w = w
        self.h = h
        self.type = type
        self.color = color


    def __set__(self, struct) -> int:
        for y in range(self.h):
            Cursor.setPosition(self.absx, self.absy + y)

            for x in range(self.w):
                if x == 0 and y == 0:
                    print(self.color + self.type.top_left, end="\x1b[0m")
                elif x == 0 and y == self.h - 1:
                    print(self.color + self.type.bottom_left, end="\x1b[0m")
                elif x == self.w - 1 and y == 0:
                    print(self.color + self.type.top_right, end="\x1b[0m")
                elif x == self.w - 1 and y == self.h - 1:
                    print(self.color + self.type.bottom_right, end="\x1b[0m")

                elif x == 0 or x == self.w - 1:
                    print(self.color + self.type.vertical, end="\x1b[0m")
                elif y == 0 or y == self.h - 1:
                    print(self.color + self.type.horizontal, end="\x1b[0m")

                else:
                    print(self.color + " ", end="\x1b[0m")

        return 1


class ThinBox(Box):
    def __init__(self, x:int, y:int, w:int, h:int, color="\x1b[0m") -> None:
        super().__init__(x, y, w, h, Thin(), color)


class BoldBox(Box):
    def __init__(self, x:int, y:int, w:int, h:int, color="\x1b[0m") -> None:
        super().__init__(x, y, w, h, Bold(), color)