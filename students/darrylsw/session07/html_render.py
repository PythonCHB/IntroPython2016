#!/usr/bin/env python3

class Element:

	tag = ""

	def __init__(self, content=None):
		self.content = []
		if content:
			self.content.append(content)

	def append(self, content):
		self.content.append(content)

	def render(self, out_file, indent):
		tag_out = indent + "<" + self.tag + ">\n"
		out_file.write (tag_out)
		for i in self.content:
			if isinstance(i, Element):
				indent2 = indent + indent
				i.render(out_file, indent2)
			else:
				out_file.write(indent + i + "\n")
		tag_out = indent + "</" + self.tag + ">\n"
		out_file.write (tag_out)	

class Html(Element):
	tag = "html"

	def render(self, out_file, indent):
		tag_out = "<" + self.tag + ">\n"
		out_file.write (tag_out)
		for i in self.content:
			if isinstance(i, Element):
				i.render(out_file, indent)
			else:
				out_file.write(indent + i + "\n")
		tag_out = "</" + self.tag + ">\n"
		out_file.write (tag_out)

class Head(Element):
	tag = "head"

class Title(Element):
	tag = "title"

class Body(Element):
	tag = "body"

class P(Element):
	tag = "p"