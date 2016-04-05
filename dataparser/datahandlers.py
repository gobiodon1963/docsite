# -*- coding: utf-8 -*-

from xml.sax.handler import ContentHandler


class DocumentHandler(ContentHandler):
    def startElement(elf, name, attrs):
        print ("Start element:", name)

if __name__ == '__main__':
    import sys
    from xml.sax import make_parser

    ch = DocumentHandler()
    saxparser = make_parser()
    saxparser.setContentHandler(ch)
    saxparser.parse(sys.stdin)
