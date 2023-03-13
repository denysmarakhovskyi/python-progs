def spaced(s):
    text = s.upper()
    textLength = len(text)
    lineLength = textLength + 2 * (2 + 1)

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

text = spaced("ABOOBA")
for line in text:
    print(line)