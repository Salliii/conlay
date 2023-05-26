

class PromptLayout(object):
    def __init__(self) -> None:
        pass


    def __reset_prompt__(self) -> int:
        print("\x1bc", end="")
        return 1
    

    def __clear_screen__(self) -> int:
        print("\x1b[3J", end="")
        return 1