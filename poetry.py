import random

poem = """If you are a dreamer, come in,
If you are a dreamer, a wisher, a liar,
A hope-er, a pray-er, a magic bean buyer…
If you’re a pretender, come sit by my fire
For we have some flax-golden tales to spin.
Come in!
Come in!"""

#Split poem into seperate lines
my_poem = poem.split("\n")

#Custom Function (normal numbered lines)
def number_lines(poem):
    for line in enumerate(poem,1):
        print(line)

#Lines printed backwards function, uses enumerate method and starts counting at 1.
def lines_printed_backwards(poem):
    for line_num, line in reversed(list(enumerate(my_poem,1))):
        print(line_num, line)

#Lines printed at random function, uses random index but does not check for duplicates.
def lines_printed_random(poem):
    random_lines = []
    for line in poem:
        random_index = random.randint(0, len(poem)-1)
        random_lines.append(poem[random_index])

    for line in random_lines:
        print(line)


#Function Calls
lines_printed_backwards(my_poem)
print("")
lines_printed_random(my_poem)
