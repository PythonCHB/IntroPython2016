"""
test code for html_render.py
"""

from html_render import Body, Element, Head, Html, P, OneLineTag, Title, Hr, Br, Img, A, H, Meta
import io


def get_output(element, ind=""):
    outfile = io.StringIO()
    element.render(outfile, ind)
    return outfile.getvalue()

def get_output_lines(element, ind=""):
    outfile = get_output(element, ind)
    return outfile.split("\n")


def test_init():
    e = Element("some string")
    e = Element()


def test_content():
    # todo: this tests an internal--fix!
    e = Element("some text")
    assert e.content == ["some text"]
    assert "some text" in e.content


def test_append():
    e = Element("some text")
    e.append("some more text")
    assert e.content[-1] == "some more text"


def test_header():
    attr = {"class": "tiny-header"}
    h = H(4, "a header", **attr)
    output = get_output(h)
    print(output)
    assert output == "<h4 class=\"tiny-header\">a header</h4>"


def test_element_with_attributes():
    p = P("a paragraph", id="TheList", style="line-height:200%")
    outfile_lines = get_output_lines(p)
    assert "id=\"TheList\"" in outfile_lines[0]
    assert "style=\"line-height:200%\"" in outfile_lines[0]


def test_single_line_element_with_attributes():
    attr = {"id": "myTitle", "class": "red"}
    e = Title("a title", **attr)
    outfile_lines = get_output_lines(e)
    print(outfile_lines[0])
    assert "<title " in outfile_lines[0]
    assert "id=\"myTitle\"" in outfile_lines[0]
    assert "class=\"red\"" in outfile_lines[0]


def test_self_closing_tag():
    e = Hr()
    output = get_output(e)
    print(output)
    assert output == "<hr />"


def test_img_tag():
    img = Img(src="/assets/an_image.jpg")
    output = get_output(img)
    print(output)
    assert "src=\"/assets/an_image.jpg\"" in output


def test_link():
    a = A("http://google.com", "link to google")
    output = get_output(a)
    print(output)
    assert output == "<a href=\"http://google.com\">link to google</a>"

def test_link_with_attributes():
    attr = {"class": "external-link", "target": "_blank"}
    a = A("http://google.com", "link to google", **attr)
    output = get_output(a)
    print(output)
    assert "class=\"external-link\"" in output
    assert "target=\"_blank\"" in output


def test_two_instances():
    e = Element("some text")
    e2 = Element("some more text")
    e.append("more text")
    assert "more text" not in e2.content


def test_doctype_and_meta():
    h = Html()
    b = Body()
    p = P("a paragraph")
    b.append(p)
    h.append(b)
    output = get_output(h)
    output_lines = get_output_lines(h)
    print(output)
    assert output_lines[0] == "<!DOCTYPE html>"
    assert output_lines[1] == "<meta charset=\"UTF-8\" />"


def test_indentation_render():
    e = P("some text")
    output = get_output(e, ind="    ")
    print(output)
    assert output.startswith("    <")


def test_html_indentation():
    e = Html("a test")
    output = get_output(e)
    print(output)
    assert "<html>\n" in output
    assert output.endswith("\n</html>")
    output_lines = output.split("\n")
    assert "    a test" in output_lines


def test_multiple_element_indentation():
    e1 = Html("")
    e2 = Body("")
    e3 = P("some random text")
    e2.append(e3)
    e1.append(e2)
    output = get_output(e1)
    output_lines = output.split("\n")
    assert "        <p>" in output_lines
    assert "            some random text" in output_lines
    print(output)


def test_one_line_tag():
    e1 = Html("")
    e2 = Head("")
    e3 = Title("Hark! A Title!")
    e2.append(e3)
    e1.append(e2)
    output = get_output(e1)
    print(output)
    output_lines = get_output_lines(e1)
    assert "        <title>Hark! A Title!</title>" in output_lines


def test_render():
    outfile = io.StringIO()
    e = Element("this is some text")
    e.append("and this is some more text")
    e.render(outfile, "")
    print(outfile.seek(0))

    file_contents = outfile.read()

    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents

    assert file_contents.startswith("<html>")
    assert file_contents.strip().endswith("</html>")
