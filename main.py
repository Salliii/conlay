class Unicode(object):
    class Border(object):
        class Thick(object):
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




class PromptLayout(object):
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
    

    class Box(object):
        def __init__(self, w:int, h:int, charset:Unicode.Border, esccolor=str) -> None:
            self.w = w
            self.h = h
            self.charset = charset
            self.esccolor = esccolor

            self.posx = 0
            self.posy = 0


    class ThinBox(Box):
        def __init__(self, w:int, h:int, esccolor=str) -> None:
            super().__init__(w, h, Unicode.Border.Thin, esccolor)
            self.w = w
            self.h = h
            self.esccolor = esccolor