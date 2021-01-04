from bfi import interpret
from .preference import BFPreference

class BFBuilder:
    """
    Generate Brainf**k source by calling functions.
    """

    def __init__(self):
        self.__text = ""
        self.current = 0

    def generate(self, preference: BFPreference = None) -> None:
        """
        Generate Brainf**k source.

        If you want to generate Brainf**k-like language instead, please give a preference as an argument.
        """
        if preference:
            text = self.__text
            text = text.replace("+", preference.increment)
            text = text.replace("-", preference.decrement)
            text = text.replace(">", preference.move_right)
            text = text.replace("<", preference.move_left)
            text = text.replace(",", preference.input)
            text = text.replace(".", preference.output)
            text = text.replace("[", preference.start_loop)
            text = text.replace("]", preference.end_loop)
            return text
        else:
            return self.__text

    def interpret(self, stdin: str = None, tape_size: int = 30000) -> str:
        """
        Execute Brainf**k source.

        This function uses bfi (https://pypi.org/project/bfi/) internally.
        """
        ret = interpret(self.__text, input_data=stdin, tape_size=tape_size, buffer_output=True)
        return ret

    def input(self) -> None:
        """
        Get user's input and store it to the memory.

        It is equivalent to `,`.
        """
        self.__text += ","

    def output(self) -> None:
        """
        Print a value which is pointed.

        It is equivalent to `.`.
        """
        self.__text += "."

    def move(self, pos) -> None:
        """
        Move to the memory by address.
        """
        if pos - self.current >= 0:
            for _ in range(pos - self.current):
                self.__text += ">"
        else:
            for _ in range(self.current - pos):
                self.__text += "<"
        self.current = pos

    def add(self, num: int) -> None:
        """
        Add a number to the memory.

        You can add a minus number to decrement the value.
        """
        if num > 0:
            for _ in range(num):
                self.__text += "+"
        else:
            for _ in range(-num):
                self.__text += "-"

    def loop(self):
        """
        Generate a loop.

        It is equivalent to `[]`.

        ```
        # Use loop() with `with` statement.
        with builder.loop():
            #
            # Do something here.
            #
        # It will generate `[<expressions>]`.
        ```
        """
        return BFLoop(self)

    def branch(self):
        """
        Generate a branch.

        It looks like the `if` statement in C.

        ```
        # Use branch() with `with` statement.
        with builder.branch():
            #
            # Do something here.
            #
        ```
        """
        return BFBranch(self)

    def init_with_zero(self) -> None:
        """
        Initialize the memory by zero.

        It is equivalent to `[-]`.
        """
        self.__text += "[-]"

    def init_with_num(self, num: int) -> None:
        """
        Initialize the memory by a number given.
        """
        self.init_with_zero()
        self.add(num)

    def init_with_letter(self, letter: str) -> None:
        """
        Initialize the memory by a letter given.
        """
        self.init_with_num(ord(letter))

    def copy(self, dist, tmp) -> None:
        """
        Copy a value to the destination given.

        It requires to use a temporary memory.
        """
        first_pos = self.current
        with self.loop():
            self.add(-1)
            self.move(tmp)
            self.add(1)
        self.move(tmp)
        with self.loop():
            self.add(-1)
            self.move(first_pos)
            self.add(1)
            self.move(dist)
            self.add(1)
        self.move(first_pos)

    def custom(self, text: str) -> None:
        """
        Add custom commands.
        """
        self.__text += text

class BFLoop:
    """
    Express a loop statement on Brainf**k.
    """
    def __init__(self, builder: BFBuilder) -> None:
        self.builder = builder
        self.first_pos = builder.current

    def __enter__(self):
        self.builder.custom("[")
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.builder.move(self.first_pos)
        self.builder.custom("]")

class BFBranch:
    """
    Express a if statement on Brainf**k.
    """
    def __init__(self, builder: BFBuilder) -> None:
        self.builder = builder
        self.first_pos = builder.current

    def __enter__(self):
        self.builder.custom("[[-]")
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.builder.move(self.first_pos)
        self.builder.custom("]")
