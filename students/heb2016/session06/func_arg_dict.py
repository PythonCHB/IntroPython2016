




def color(*color_args, **color_kwags):
    print("position arguments *color_args: ", color_args)
    print("keyword arguments **color_kwags: ", color_kwags)
    print("\n")

print("default: ")
color() 

print("generic parameters keyword: ")
color_args= ('green', 'black')
color_kwags = {"link_color": "red", "visited_color": "blue"}
color(*color_args, **color_kwags)





 


