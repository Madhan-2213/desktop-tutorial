from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    @staticmethod
    def print_attrs(attrs):
        for name,value in attrs:
            print(f"-> {name} > {value}")
            
    def handle_starttag(self, tag, attrs):
        print(tag)
        self.print_attrs(attrs)

HTML = ""
for _ in range(int(input())):
    HTML += input().rstrip()
    HTML += '\n'

parser = MyHTMLParser()
parser.feed(HTML)
parser.close()
