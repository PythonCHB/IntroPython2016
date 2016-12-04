#!/Users/jhefner/python_dev/uw_python/bin/python

class TextWrapper: #lifted this code directly from solution, explanation at line 20
    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind=""):
        file_out.write(current_ind + self.text)

class Element():

    html_tag = 'html'
    indent = '    '

    def __init__(self, content=None):
        self.content = []
        if content:
            self.append(content)
            # i dont understand this portion and why we put "content" there

    def append(self,content):
        # taking this append code from the solution.
        # the lab text says to reference duck typing and whatnot.
        # after reading the solution code and using it here I get why we are
        # doing it this way but im not quite sure how i was supposed to
        # know to arrive at this solution or something similar.
        # OO stuff is still very new to me so maybe its just a pattern
        # that im not used to here.
        if hasattr(content, 'render'):
            self.content.append(content)
        else:
            self.content.append(TextWrapper(str(content)))

    def render(self, out_file, ind=""):
        out_file.write(ind+"<"+self.html_tag+">"+"\n")
        for i in self.content:
            i.render(out_file, ind+self.indent)
            out_file.write("\n")
        out_file.write(ind+"</"+self.html_tag+">"+"\n")

class OneLineTag(Element):
    def render(self, out_file, ind=""):
        out_file.write(ind+"<"+self.html_tag+">")
        for i in self.content:
            i.render(out_file)
        out_file.write("</"+self.html_tag+">")

class Title(OneLineTag):
    tag = 'title'

class Html(Element):
    html_tag = 'html' #isnt this redundant? Shouldn't I leave the base class with an empty string for html_tag?
    indent = ''

class Body(Element):
    html_tag = 'body'
    indent = '    '

class P(Element):
    html_tag = 'p'
    indent = '        '

class Head(Element):
    html_tag = 'head'