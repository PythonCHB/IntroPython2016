#!/usr/bin/env python3

import io

from html_render import Element, Html, Body, P

def test_init():
	e = Element()

	e = Element("this is some text")

def test_content():
	# fixme: this tests internals!!!!
	e = Element("this is some text")

	assert "this is some text" in e.content 

def test_append():
	e = Element("this is some text")
	e.append ("and more text")

	assert "and more text" in e.content
	assert e.content == ["this is some text", "and more text"]	

	e.append ("and even more text")
	assert e.content == ["this is some text", "and more text", "and even more text"]

def test_render():
	outfile = io.StringIO()		
	e = Element ("this is some text")
	e.append ("and some more text")
	#with open("test1.html", 'w') as outfile:
	#	e.render(outfile)
	e.render(outfile, "")

	outfile.seek(0)
	file_contents = outfile.read()

	assert ("this is some text") in file_contents
	assert ("and some more text") in file_contents
	
	#assert file_contents.startswith ("<html>\n")
	#assert file_contents.strip().endswith ("</html>")

def test_html():
	outfile = io.StringIO()
	h = Html("this is some text")
	h.append ("and some more text")

	assert "and some more text" in h.content
	assert h.content == ["this is some text", "and some more text"]

	h.render(outfile, "")
	outfile.seek(0)
	file_contents = outfile.read()

	assert ("this is some text") in file_contents
	assert ("and some more text") in file_contents

	assert file_contents.startswith ("<html>\n")
	assert file_contents.strip().endswith ("</html>")


def test_body():
	outfile = io.StringIO()
	b = Body("this is some text")
	b.append ("and some more text")

	assert "and some more text" in b.content
	assert b.content == ["this is some text", "and some more text"]

	b.render(outfile, "")
	outfile.seek(0)
	file_contents = outfile.read()

	assert ("this is some text") in file_contents
	assert ("and some more text") in file_contents

	assert file_contents.startswith ("<body>\n")
	assert file_contents.strip().endswith ("</body>")


def test_p():
	outfile = io.StringIO()
	p = P("this is some text")
	p.append ("and some more text")

	assert "and some more text" in p.content
	assert p.content == ["this is some text", "and some more text"]

	p.render(outfile, "")
	outfile.seek(0)
	file_contents = outfile.read()

	assert ("this is some text") in file_contents
	assert ("and some more text") in file_contents

	assert file_contents.startswith ("<p>\n")
	assert file_contents.strip().endswith ("</p>")

def test_page():
	outfile = io.StringIO()
	a = Html()
	b = Body("Body Text")
	c = P("Paragraph text 1")
	c.append("Paragraph text 2")
	b.append(c)
	a.append(b)

	a.render(outfile, "")
	outfile.seek(0)
	file_contents = outfile.read()

	assert file_contents.startswith ("<html>\n")
	assert file_contents.strip().endswith ("</html>")

	assert ("<body>") in file_contents
	assert ("</body>") in file_contents

	assert ("<p>") in file_contents
	assert ("</p>") in file_contents

	assert ("Body Text") in file_contents
	assert ("Paragraph text 1") in file_contents
	assert ("Paragraph text 2") in file_contents



