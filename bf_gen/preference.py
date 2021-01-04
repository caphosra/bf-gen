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

    def blub(self):
        """
        Have BFBuilder use Blub.

        What is Blub : https://esolangs.org/wiki/Blub
        """
        self.increment = "Blub.Blub."
        self.decrement = "Blub!Blub!"
        self.move_right = "Blub.Blub?"
        self.move_left = "Blub?Blub."
        self.input = "Blub.Blub!"
        self.output = "Blub!Blub."
        self.start_loop = "Blub!Blub?"
        self.end_loop = "Blub?Blub!"
