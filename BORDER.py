def spaced(s):
    text = "ABOOBA"
    textLength = len(text)
    lineLength = textLength + 2 * (2 + 1)
    height = 5

    # at this point we know the first and fifth lines are the same and
    # we know the first and fourth are the same.  (reflected against the x-axis)

    hBorder = ""
    for c in range(lineLength):
        if c % 2:
            hBorder = hBorder + '.'
        else:
            hBorder = hBorder + '-'
    spacer = "." + " " * (lineLength - 2) + "."
    fancyText = "-  " + text + "  -"
    return (hBorder, spacer, fancyText, spacer, hBorder)

textTuple = spaced("ABOOBA")
for line in textTuple:
    print(line)


print('\n')


def border_msg(msg):

    count = len(msg) + 2 # dash will need +2 too

    dash = "-"*count 

    print("+{}+".format(dash))

    print("| {} |".format(msg))

    print("+{}+".format(dash))


border_msg('D')     # without print
border_msg("HELLP") # without print


print('\n')


def border_msg(msg):

    count = len(msg) + 2 # dash will need +2 too

    dash = "-"*count 

    print("+{}+".format(dash))

    print("| {} |".format(msg))

    print("+{}+".format(dash))


border_msg('F')     # without print
border_msg("DEMURE") # without print


print('\n')


def box_lines(lines, width):
    topBottomRow = "+" + "-" * width + "+"
    middle = "\n".join("|" + x.ljust(width) + "|" for x in lines)
    return "{0}\n{1}\n{0}".format(topBottomRow, middle)

def split_line(line, width):
    return [line[i:i+width] for i in range(0, len(line), width)]

def split_msg(msg, width):
    lines = msg.split("\n")
    split_lines = [split_line(line, width) for line in lines]
    return [item for sublist in split_lines for item in sublist] # flatten

def border_msg(msg, width):
    return(box_lines(split_msg(msg, width), width))

print(border_msg("""I'll always remember
The chill of November
The news of the fall
The sounds in the hall
The clock on the wall
Ticking away""", 22))


print('\n')


def big_frame(word_list):
    box_char = '+'
    for words in word_list:
        print(box_char*(len(words)+4))
        print(box_char, words, box_char)
        print(box_char*(len(words)+4))

big_frame(["Welcome", "to", "Brno"])