poem = """
this is poem
line 1
line2
"""

lines = poem.split("\n")

print(lines)

def lines_printed_backwards(poem):
    new_poem = poem[::-1]
    return new_poem


print(lines_printed_backwards(lines))
