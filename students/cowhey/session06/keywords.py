def print_colors(fore_color="purple", back_color="maroon", link_color="mauve", visited_color="violeta"):
    print(fore_color, back_color, link_color, visited_color)


print_colors()

print_colors("blue", "teal")

print_colors("green", link_color="emerald")

reds = ("ruby", "scarlet")

grays = {"link_color": "smoke", "visited_color": "charcoal"}

print_colors(*reds, **grays)
