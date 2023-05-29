class Type:
    class Unicode:
        class Border:
            vertical = u""
            horizontal = u""
            top_left = u""
            top_right = u""
            bottom_left = u""
            bottom_right = u""


class Bold(Type):
    def __init__(self):
        self.Unicode.Border.vertical = u"\u2503"
        self.Unicode.Border.horizontal = u"\u2501"
        self.Unicode.Border.top_left = u"\u250F"
        self.Unicode.Border.top_right = u"\u2513"
        self.Unicode.Border.bottom_left = u"\u2517"
        self.Unicode.Border.bottom_right = u"\u251B"


class Thin(Type):
    def __init__(self):
        self.Unicode.Border.vertical = u"\u2502"
        self.Unicode.Border.horizontal = u"\u2500"
        self.Unicode.Border.top_left = u"\u250C"
        self.Unicode.Border.top_right = u"\u2510"
        self.Unicode.Border.bottom_left = u"\u2514"
        self.Unicode.Border.bottom_right = u"\u2518"




class Console(object):
    def reset() -> int:
        print("\x1bc", end="")
        return 1


    def clear() -> int:
        print("\x1b[3J", end="")
        return 1




class Cursor(object):   
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
    

    def hide() -> int:
        print("\x1b[?25l", end="")
        return 1
    
    
    def show() -> int:
        print("\x1b[?25h", end="")
        return 1




class Box(object):
    def __init__(self, x:int, y:int, w:int, h:int, type:Type, esccolor="\x1b[0m") -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.type = type
        self.esccolor = esccolor




class ThinBox(Box):
    def __init__(self, x:int, y:int, w:int, h:int, esccolor="\x1b[0m") -> None:
        super().__init__(x, y, w, h, Thin, esccolor)




class BoldBox(Box):
    def __init__(self, x:int, y:int, w:int, h:int, esccolor="\x1b[0m") -> None:
        super().__init__(x, y, w, h, Bold, esccolor)