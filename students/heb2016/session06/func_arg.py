




def color(fore_color="black", back_color="yellow", link_color="blue", visited_color="red"):
    print( "fore_color: ", fore_color)
    print("back_color: ",  back_color)
    print("link_color: ",  link_color)
    print("visited_color: ", visited_color  )
    print("\n")

print("default: ") 
color() 
print("positional: ")
color("red", "blue", "yellow", "chartreuse") 

print("keyword: ")
color(link_color ='red', back_color ='blue')

print("combination of position & keyword: ")
color("purple", link_color='red', back_color ='blue')


print("tuple & dict: ")
links={'link_color': 'chartreuse'}
regular=('red', 'blue')
color(*regular, **links)

 


