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




class Colay(object):
    def __init__(self) -> None:
        pass


    def __reset_prompt__(self) -> int:
        print("\x1bc", end="")
        return 1
    

    def __clear_prompt__(self) -> int:
        print("\x1b[3J", end="")
        return 1
    
    
    def __set_cursor_position__(self, x:int, y:int) -> int:
        print("\x1b[{y};{x}H".format(y=y+1, x=x+1), end="")
        return 1
    

    def __shift_cursor_horizontal__(self, sh) -> int:
        if sh < 0:
            print("\x1b[{sh}D".format(sh=sh*-1), end="")
            return 1
        elif sh > 0:
            print("\x1b[{sh}D".format(sh=sh), end="")
            return 1
        return 0
    

    def __shift_cursor_vertikal__(self, sh) -> int:
        if sh < 0:
            print("\x1b[{sh}A".format(sh=sh*-1), end="")
            return 1
        elif sh > 0:
            print("\x1b[{sh}B".format(sh=sh), end="")
            return 1
        return 0
    


    
class Console(object):
    def __init__(self) -> None:
        pass



    
class Cursor(object):
    def init(self) -> None:
        pass
    



class Box(object):
    def __init__(self, x:int, y:int, w:int, h:int, charset:Unicode, esccolor=str) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.charset = charset
        self.esccolor = esccolor


class ThinBox(Box):
    def __init__(self, x:int, y:int, w:int, h:int, esccolor=str) -> None:
        super().__init__(x, y, w, h, Unicode.Border.Thin, esccolor)
    

class BoldBox(Box):
    def __init__(self, x:int, y:int, w:int, h:int, esccolor=str) -> None:
        super().__init__(x, y, w, h, Unicode.Border.Bold, esccolor)