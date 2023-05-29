class Type:
    vertical = u""
    horizontal = u""
    top_left = u""
    top_right = u""
    bottom_left = u""
    bottom_right = u""

    tjoint_to_n_bold = u""
    tjoint_to_e_bold = u""
    tjoint_to_s_bold = u""
    tjoint_to_w_bold = u""
    xjoint_horizontal_bold = u""
    xjoint_vertical_bold = u""

    tjoint_to_n_thin = u""
    tjoint_to_e_thin = u""
    tjoint_to_s_thin = u""
    tjoint_to_w_thin = u""
    xjoint_horizontal_thin = u""
    xjoint_vertical_thin = u""


class Bold(Type):
    def __init__(self):
        self.vertical = u"\u2503"
        self.horizontal = u"\u2501"
        self.top_left = u"\u250F"
        self.top_right = u"\u2513"
        self.bottom_left = u"\u2517"
        self.bottom_right = u"\u251B"

        self.tjoint_to_n_bold = u"\u253B"
        self.tjoint_to_e_bold = u"\u2523"
        self.tjoint_to_s_bold = u"\u2533"
        self.tjoint_to_w_bold = u"\u252B"
        self.xjoint_horizontal_bold = u"\u254B"
        self.xjoint_vertical_bold = u"\u254B"

        self.tjoint_to_n_thin = u"\u2537"
        self.tjoint_to_e_thin = u"\u2520"
        self.tjoint_to_s_thin = u"\u252F"
        self.tjoint_to_w_thin = u"\u2528"
        self.xjoint_horizontal_thin = u"\u2542"
        self.xjoint_vertical_thin = u"\u253F"


class Thin(Type):
    def __init__(self):
        self.vertical = u"\u2502"
        self.horizontal = u"\u2500"
        self.top_left = u"\u256D"
        self.top_right = u"\u256E"
        self.bottom_left = u"\u2570"
        self.bottom_right = u"\u256F"

        self.tjoint_to_n_bold = u"\u2538"
        self.tjoint_to_e_bold = u"\u251D"
        self.tjoint_to_s_bold = u"\u2530"
        self.tjoint_to_w_bold = u"\u2525"
        self.xjoint_horizontal_bold = u"\u253F"
        self.xjoint_vertical_bold = u"\u2542"

        self.tjoint_to_n_thin = u"\u2534"
        self.tjoint_to_e_thin = u"\u251C"
        self.tjoint_to_s_thin = u"\u252C"
        self.tjoint_to_w_thin = u"\u2524"
        self.xjoint_horizontal_thin = u"\u253C"
        self.xjoint_vertical_thin = u"\u253C"




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
        self.absx = 0
        self.absy = 0
        self.relx = 0
        self.rely = 0
        self.w = 0
        self.h = 0

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

                for element in struct:
                    if element != self and (
                        (self.absy+y == element.absy and (self.absx+x >= element.absx and self.absx+x < element.absx+element.w)) or
                        (self.absx+x == element.absx and (self.absy+y >= element.absy and self.absy+y < element.absy+element.h)) or
                        (self.absy+y == element.absy+element.h-1 and (self.absx+x >= element.absx and self.absx+x < element.absx+element.w)) or
                        (self.absx+x == element.absx+element.w-1 and (self.absy+y >= element.absy and self.absy+y < element.absy+element.h))
                    ):
                        
                        if self.absy+y == self.absy:
                            Cursor.setPosition(self.absx+x, self.absy+y)
                            if not self.override:
                                if type(element.type) == Thin:
                                    print(self.color + self.type.xjoint_vertical_thin, end="\x1b[0m")
                                elif type(element.type) == Bold:
                                    print(self.color + self.type.xjoint_vertical_bold, end="\x1b[0m")
                            else:
                                if type(element.type) == Thin:
                                    print(self.color + self.type.tjoint_to_n_thin, end="\x1b[0m")
                                elif type(element.type) == Bold:
                                    print(self.color + self.type.tjoint_to_n_bold, end="\x1b[0m")
                            break

                        elif self.absx+x == self.absx+self.w-1:
                            Cursor.setPosition(self.absx+x, self.absy+y)
                            if not self.override:
                                if type(element.type) == Thin:
                                    print(self.color + self.type.xjoint_horizontal_thin, end="\x1b[0m")
                                elif type(element.type) == Bold:
                                    print(self.color + self.type.xjoint_horizontal_bold, end="\x1b[0m")
                            else:
                                if type(element.type) == Thin:
                                    print(self.color + self.type.tjoint_to_e_thin, end="\x1b[0m")
                                elif type(element.type) == Bold:
                                    print(self.color + self.type.tjoint_to_e_bold, end="\x1b[0m")
                            break

                        elif self.absy+y == self.absy+self.h-1:
                            Cursor.setPosition(self.absx+x, self.absy+y)
                            if not self.override:
                                if type(element.type) == Thin:
                                    print(self.color + self.type.xjoint_vertical_thin, end="\x1b[0m")
                                elif type(element.type) == Bold:
                                    print(self.color + self.type.xjoint_vertical_bold, end="\x1b[0m")
                            else:
                                if type(element.type) == Thin:
                                    print(self.color + self.type.tjoint_to_s_thin, end="\x1b[0m")
                                elif type(element.type) == Bold:
                                    print(self.color + self.type.tjoint_to_s_bold, end="\x1b[0m")
                            break

                        elif self.absx+x == self.absx:
                            Cursor.setPosition(self.absx+x, self.absy+y)
                            if not self.override:
                                if type(element.type) == Thin:
                                    print(self.color + self.type.xjoint_horizontal_thin, end="\x1b[0m")
                                elif type(element.type) == Bold:
                                    print(self.color + self.type.xjoint_horizontal_bold, end="\x1b[0m")
                            else:
                                if type(element.type) == Thin:
                                    print(self.color + self.type.tjoint_to_w_thin, end="\x1b[0m")
                                elif type(element.type) == Bold:
                                    print(self.color + self.type.tjoint_to_w_bold, end="\x1b[0m")
                            break

                        if not self.override:
                            break

                    elif element != self:
                        Cursor.setPosition(self.absx + x, self.absy + y)
                    else:

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