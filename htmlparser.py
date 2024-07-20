
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f'Start : {tag}')
        for att in attrs:
            print(f'-> {att[0]} > {att[1]}')
        
    def handle_endtag(self, tag):
        print(f'End   : {tag}')
        
    def handle_startendtag(self, tag, attrs):
        print(f'Empty : {tag}')
        for att in attrs:
            print(f'-> {att[0]} > {att[1]}')


if __name__ == '__main__':
    n = int(input().rstrip())
    html_text = ''
    for i in range(n):
        html_text += input()
    praser = MyHTMLParser()
    praser.feed(html_text)
