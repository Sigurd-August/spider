import urllib.request
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    html = html.decode('UTF-8')
    return html

file_01 = open('1.html')
file_01_text = file_01.read()
#print(file_01_text)
pattern_symbol = re.compile(r'<th align="left" valign="top" class="colnorm" scope="row">(.*)</th>')
pattern_sname = re.compile(r'<td><a href="profile[?]symbol=.*" target="_top"><em>(.*?)</em> <em>(.*?)</em></a></td>')
pattern_cname = re.compile(r'<td>([\w\s]*?)</td>')
match_symbol = pattern_symbol.findall(file_01_text)
match_sname = pattern_sname.findall(file_01_text)
match_cname = pattern_cname.findall(file_01_text)
print(len(match_symbol))

if match_symbol:
    print(match_symbol)
if match_sname:
    for i in range(0, 1046):
        print(match_sname[i][0] +" "+ match_sname[i][1])
if match_cname:
    print(match_cname)
file_01.close()