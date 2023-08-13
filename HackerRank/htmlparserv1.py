from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f'Start : {tag}')
        for attr in attrs:
            print(f'-> {attr[0]} > {attr[1]}')
    def handle_endtag(self, tag):
        print(f'End   : {tag}')
    def handle_startendtag(self, tag, attrs):
        print(f'Empty : {tag}')
        for attr in attrs:
            print(f'-> {attr[0]} > {attr[1]}')

n = int(input())
html_list = []
for _ in range(n):
    html_list.append(input())

html_doc = '\n'.join(html_list)

parser = MyHTMLParser()
parser.feed(html_doc)