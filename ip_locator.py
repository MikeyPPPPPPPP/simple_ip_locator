#size 10
import urllib.request
from bs4 import BeautifulSoup



ip = '68.189.65.252'

html = ("https://whatismyipaddress.com/ip/" + ip)

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
req = urllib.request.Request(html, headers = headers)
resp = urllib.request.urlopen(req)
r = resp.read()
soup = BeautifulSoup(r, 'lxml')



#table = soup.table

for fin in soup.find_all('div', {'id':'section_left_3rd'}):
    
    for ta in fin.find_all('tr'):
        print(ta.text)
        
        
