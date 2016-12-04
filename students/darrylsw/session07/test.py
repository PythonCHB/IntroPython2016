#!/usr/bin/env python3

import io

from html_render import Element, Html

from html_render import Body
from html_render import P


a=Html()
a.append ("some stuff")
a.append ("other stuff")

b=Body()
b.append ("body stuff")
b.append ("body stuff II")

#print (a.content)
#print (a.tag)

#print (b.content)
#print (b.tag)

#a.append(b)
#print (a.content)

outfile = io.StringIO()	
a.render (outfile, "")
b.render (outfile, "")

a.append(b)
#print (a.__class__.__name__)
a.render (outfile, "")
#print (a.content)

#c = "a string"
#print (c.__class__.__name__)

f = open('test.out', 'w')
f.write (a)
