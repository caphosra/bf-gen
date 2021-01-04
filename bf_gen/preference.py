class BFPreference:
    """
    Stores language preference
    """
    def __init__(self):
        self.increment = "+"
        self.decrement = "-"
        self.move_right = ">"
        self.move_left = "<"
        self.input = ","
        self.output = "."
        self.start_loop = "["
        self.end_loop = "]"

    def brainf__k(self):
        """
        Have BFBuilder use Brainf**k.

        What is Brainf**k : https://esolangs.org/wiki/Brainfuck
        """
        self.increment = "+"
        self.decrement = "-"
        self.move_right = ">"
        self.move_left = "<"
        self.input = ","
        self.output = "."
        self.start_loop = "["
        self.end_loop = "]"

    def ook(self):
        """
        Have BFBuilder use Ook!

        What is Ook! : https://esolangs.org/wiki/Ook!
        """
        self.increment = "Ook.Ook."
        self.decrement = "Ook!Ook!"
        self.move_right = "Ook.Ook?"
        self.move_left = "Ook?Ook."
        self.input = "Ook.Ook!"
        self.output = "Ook!Ook."
        self.start_loop = "Ook!Ook?"
        self.end_loop = "Ook?Ook!"
