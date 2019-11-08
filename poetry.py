poem = """If you are a dreamer, come in,
If you are a dreamer, a wisher, a liar,
A hope-er, a pray-er, a magic bean buyer…
If you’re a pretender, come sit by my fire
For we have some flax-golden tales to spin.
Come in!
Come in!"""

lines = poem.split("\n")

def number_lines(poem):
    for line in enumerate(poem,1):
        print(line)

def lines_printed_backwards(poem):
    for line_num, line in reversed(list(enumerate(lines,1))):
        print(line_num, line)

    # new_poem = poem[::-1]
    # for line in new_poem:
    #     print(line)

# number_lines(lines)
lines_printed_backwards(lines)
