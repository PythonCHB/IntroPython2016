#!/usr/bin/env python3


class Element:
    tag = 'html'
    def __init__(self, content=None):
        self.content = []
        if content:
            self.content.append(content)

    def append(self, content):
        self.content.append(content)

    def render(self, out_file, ind=''):
        out_file.write("<{}>\n".format(self.tag))
        for stuff in self.content:
            out_file.write(stuff+"\n")
        out_file.write("</{}>\n".format(self.tag))


class Html(Element):
    tag = 'html'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'







# class Element:
    
#     tag = 'aaa'

#     def __init__(self, content=None):
#         self.content = []
#         if content:
#             self.content.append(content)

#     def append(self, content):
#         self.content.append(content)

#     def render(self, out_file, ind=''):
#         if self.tag == 'html':
#             out_file.write('<html>\n')
#         for stuff in self.content:
#             out_file.write(stuff + '\n')
        
#         # if self.tag == 'body':
#         #     out_file.write('<body>\n')
#         # for stuff in self.content:
#         #     out_file.write(stuff + '\n')
#         # if self.tag == 'body':
#         #     out_file.write('</body>\n')

#         if self.tag == 'html':
#             out_file.write('</html>\n')
