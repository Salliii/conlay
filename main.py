class Border:
    vertical = u""
    horizontal = u""
    top_left = u""
    top_right = u""
    bottom_left = u""
    bottom_right = u""


class Bold(Border):
    def __init__(self) -> None:
        self.vertical = u"\u2503"
        self.horizontal = u"\u2501"
        self.top_left = u"\u250F"
        self.top_right = u"\u2513"
        self.bottom_left = u"\u2517"
        self.bottom_right = u"\u251B"


class Thin(Border):
    def __init__(self) -> None:
        self.vertical = u"\u2502"
        self.horizontal = u"\u2500"
        self.top_left = u"\u256D"
        self.top_right = u"\u256E"
        self.bottom_left = u"\u2570"
        self.bottom_right = u"\u256F"




class Color:
    
    clear = "\x1b[0m"

    class Bg:

        clear = "\x1b[49m"

        def rgb(r:int, g:int, b:int) -> str:
            return "\x1b[48;2;{r};{g};{b}m".format(r=r, g=g, b=b)
        
        black = rgb(0, 0, 0)
        white = rgb(255, 255, 255)
        red = rgb(205, 49, 49)
        green = rgb(13, 188, 121)
        blue = rgb(36, 114, 200)
        yellow = rgb(229, 229, 16)
        purple = rgb(188, 63, 188)
        cyan = rgb(17, 168, 205)
    
    class Fg:

        clear = "\x1b[49m"

        def rgb(r:int, g:int, b:int) -> str:
            return "\x1b[38;2;{r};{g};{b}m".format(r=r, g=g, b=b)
        
        black = rgb(0, 0, 0)
        white = rgb(255, 255, 255)
        red = rgb(205, 49, 49)
        green = rgb(13, 188, 121)
        blue = rgb(36, 114, 200)
        yellow = rgb(229, 229, 16)
        purple = rgb(188, 63, 188)
        cyan = rgb(17, 168, 205)




class Console:
    def reset() -> int:
        print("\x1bc", end="")
        return 1


    def clear() -> int:
        print("\x1b[3J", end="")
        return 1
    

    def eraseLineToEnd() -> int:
        print("\x1b[0K", end="")
        return 1
    

    def eraseLinefromStart() -> int:
        print("\x1b[1K", end="")
        return 1
    

    def eraseLine() -> int:
        print("\x1b[2K", end="")
        return 1




class Cursor:   
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




class Conlay:

    childs = []

    Console.reset()
    Cursor.setPosition(0, 0)

    def __init__(self) -> None:
        self.relative_x = int()
        self.relative_y = int()
        self.absolute_x = int()
        self.absolute_y = int()
        self.width = int()
        self.min_width = int()
        self.max_width = int()
        self.height = int()
        self.min_height = int()
        self.max_height = int()
        self.zindex = int()
        self.padding_x = int()
        self.padding_y = int()
        self.text = str()
        self.background = bool()
        self.bg_color = Color.clear
        self.fg_color = Color.clear


    def __sort_childs_by_zindex__(self, reverse=False) -> dict:
        return list(sorted(self.childs, key=lambda child: child.zindex, reverse=reverse))


    def add(self, element:None) -> int: #Element
        element.zindex = self.zindex + 1
        
        element.absolute_x = self.absolute_x + self.padding_x + element.relative_x
        element.absolute_y = self.absolute_y + self.padding_y + element.relative_y

        if self.min_width != self.max_width and self.min_width < self.max_width and self.min_width >= 0:
            element.width = min(max(element.min_width, element.width), element.max_width)
            element.height = min(max(element.min_height, element.height), element.max_height)

        self.childs.append(element)
        
        return 1
    

    def print(self) -> int:
        for element in self.__sort_childs_by_zindex__():

            try:
                element.__preprint__()
            except AttributeError:
                pass

            for y in range(element.height):
                Cursor.setPosition(element.absolute_x, element.absolute_y + y)

                for x in range(element.width):
                    if x == 0 and y == 0:
                        print(element.bg_color + element.fg_color + element.border.top_left, end=Color.clear)
                    elif x == 0 and y == element.height - 1:
                        print(element.bg_color + element.fg_color + element.border.bottom_left, end=Color.clear)
                    elif x == element.width - 1 and y == 0:
                        print(element.bg_color + element.fg_color + element.border.top_right, end=Color.clear)
                    elif x == element.width - 1 and y == element.height - 1:
                        print(element.bg_color + element.fg_color + element.border.bottom_right, end=Color.clear)

                    elif x == 0 or x == element.width - 1:
                        print(element.bg_color + element.fg_color + element.border.vertical, end=Color.clear)
                    elif y == 0 or y == element.height - 1:
                        print(element.bg_color + element.fg_color + element.border.horizontal, end=Color.clear)

                    else:
                        if element.background:
                            print(element.bg_color + element.fg_color + " ", end=Color.clear)
                        else:
                            Cursor.shiftHorizontal(1)
            
            try:
                element.__pastprint__()
            except AttributeError:
                pass




class LayoutElement(Conlay):
    def __init__(self, x:int, y:int, w:int, h:int, border:Border) -> None:
        super().__init__()

        self.relative_x = x
        self.relative_y = y
        self.width = w + 2
        self.height = h + 2
        self.border = border




class Box(LayoutElement):
    def __init__(self, x:int, y:int, w:int, h:int, border:Border) -> None:
        super().__init__(x, y, w, h, border)

    
    def __preprint__(self) -> int:
        return 1
    

    def __pastprint__(self) -> int:
        return 1


class ThinBox(Box):
    def __init__(self, x:int, y:int, w:int, h:int) -> None:
        super().__init__(x, y, w, h, Thin())


class BoldBox(Box):
    def __init__(self, x:int, y:int, w:int, h:int) -> None:
        super().__init__(x, y, w, h, Bold())




class Label(LayoutElement):
    def __init__(self, x:int, y:int, text:str, border:Border) -> None:
        w = len(max(text.split("\n"), key=len))
        h = len(text.split("\n"))

        super().__init__(x, y, w, h, border)

        self.text = text


    def __preprint__(self) -> int:
        self.width = self.width + self.padding_x * 2
        self.height = self.height + self.padding_y * 2

        return 1


    def __pastprint__(self) -> int:
        Cursor.setPosition(self.absolute_x + 1 + self.padding_x, self.absolute_y + 1 + self.padding_y)
        print(self.text, end="")

        return 1


class ThinLabel(Label):
    def __init__(self, x:int, y:int, text:str) -> None:
        super().__init__(x, y, text, Thin())


class BoldLabel(Label):
    def __init__(self, x:int, y:int, text:str) -> None:
        super().__init__(x, y, text, Bold())