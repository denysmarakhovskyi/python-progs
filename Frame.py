def border_msg(msg):
    count = len(msg) + 2 # dash will need +2 too
    dash = "-"*count 
    return "+{}+\n| {} |\n+{}+".format(dash, msg, dash)

print(border_msg('F'))     # without print
print(border_msg("DEMURE")) # without print