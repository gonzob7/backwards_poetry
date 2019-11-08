import random

poem = """If you are a dreamer, come in,
If you are a dreamer, a wisher, a liar,
A hope-er, a pray-er, a magic bean buyer…
If you’re a pretender, come sit by my fire
For we have some flax-golden tales to spin.
Come in!
Come in!"""

my_poem = poem.split("\n")

def number_lines(poem):
    for line in enumerate(poem,1):
        print(line)

def lines_printed_backwards(poem):
    for line_num, line in reversed(list(enumerate(my_poem,1))):
        print(line_num, line)

def lines_printed_random(poem):
    random_lines = []
    for line in poem:
        random_index = random.randint(0, len(poem)-1)
        random_lines.append(poem[random_index])

    for line in random_lines:
        print(line)


lines_printed_backwards(my_poem)
print("")
lines_printed_random(my_poem)
