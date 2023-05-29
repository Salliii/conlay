class Unicode(object):
    class Border(object):
        class Bold(object):
            horizontal = u"\u2501"
            vertical = u"\u2503"
            top_left = u"\u250F"
            top_right = u"\u2513"
            bottom_left = u"\u2517"
            bottom_right = u"\u251B"


        class Thin(object):
            horizontal = u"\u2500"
            vertical = u"\u2502"
            top_left = u"\u256D"
            top_right = u"\u256E"
            bottom_left = u"\u256F"
            bottom_right = u"\u2570"




class Console(object):
    def __init__(self) -> None:
        pass


    def reset() -> int:
        print("\x1bc", end="")
        return 1


    def clear() -> int:
        print("\x1b[3J", end="")
        return 1




class Cursor(object):
    def init(self) -> None:
        pass


    def setPosition(x:int, y:int) -> int:
        print("\x1b[{y};{x}H".format(y=y+1, x=x+1), end="")
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




class Box(Cursor, Console):
    def __init__(self, x:int, y:int, w:int, h:int, charset:Unicode, esccolor=str) -> None:
        self.relx = x
        self.rely = y
        self.absx = x
        self.absy = y
        self.w = w
        self.h = h
        self.charset = charset
        self.esccolor = esccolor

        self.setPosition(self.x, self.y)




class ThinBox(Box):
    def __init__(self, x:int, y:int, w:int, h:int, esccolor=str) -> None:
        super().__init__(x, y, w, h, Unicode.Border.Thin, esccolor)
 



class BoldBox(Box):
    def __init__(self, x:int, y:int, w:int, h:int, esccolor=str) -> None:
        super().__init__(x, y, w, h, Unicode.Border.Bold, esccolor)