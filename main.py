

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
        def __init__(self, w:int, h:int, charset:object):
            self.w = w
            self.h = h
            self.charset = charset