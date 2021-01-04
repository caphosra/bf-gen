from bf_gen import BFBuilder

def test_builder1():
    builder = BFBuilder()

    for letter in "Hello World":
        builder.init_with_letter(letter)
        builder.output()

    assert builder.interpret() == "Hello World"

def test_builder2():
    builder = BFBuilder()
    triangle_size = 5

    DESCENDING = 0
    ASCENDING = 1
    SYMBOL = 2
    TEMP = 3

    builder.move(DESCENDING)
    builder.init_with_num(triangle_size)

    with builder.loop():
        builder.add(-1)

        builder.move(TEMP)
        builder.init_with_zero()

        builder.move(ASCENDING)
        builder.add(1)
        builder.copy(SYMBOL, TEMP)

        builder.move(SYMBOL)

        with builder.loop():
            builder.add(-1)

            builder.move(TEMP)
            builder.init_with_letter("#")
            builder.output()

            builder.move(SYMBOL)

        builder.move(TEMP)
        builder.init_with_letter("\n")
        builder.output()

        builder.move(DESCENDING)

    assert builder.interpret() == "#\n##\n###\n####\n#####\n"
