#!/Users/jhefner/python_dev/uw_python/bin/python

"""
test html_render.py
"""

from html_render import Element
import io

def test_init():
    # basic test to ensure that class deals with expected attributes correctly.
    e = Element()
    e = Element("test text")


def test_content():
    # tests the actual result of the class is working as currently expected.
    e = Element("this is the first text")
    assert "this is the first text" in e.content

def test_append():
    # test that text passed will be appended
    e = Element("this is appended text")
    e.append("additional text")
    assert "additional text" in e.content
    assert "this is appended text" in e.content

def test_two_instances_of_class():
    e = Element("this is 1st elements text")
    e2 = Element("this is 2nd elements text")
    e.append("additional text for 1st element")
    assert "additional text for 1st element" not in e2.content

def test_render():
    outfile = io.StringIO()
    e = Element("this is some text")
    e.append("some more text")
    e.render(outfile)
    outfile.seek(0)
    file_contents = outfile.read()
    assert("this is some text") in file_contents
    assert("some more text") in file_contents
    assert file_contents.startswith("<html>")
    assert file_contents.strip().endswith("</html>")