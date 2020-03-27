import urllib.request
from bs4 import BeautifulSoup



def req(url):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    r = resp.read()
    soup = BeautifulSoup(r, 'lxml')
    return soup

def get_ip():
    soup = req('https://www.google.com/search?q=what+is+my+ip&oq=what+is+my+ip')
    
    for data in soup.find_all('div', {'class':'MUxGbd u31kKd gsrt lyLwlc lEBKkf'}):
        
        return data.text

def get_info():
    ip = get_ip()
    soup = req("https://whatismyipaddress.com/ip/" + ip)
    for fin in soup.find_all('div', {'id':'section_left_3rd'}):
    
        for ta in fin.find_all('tr'):
            
            print(ta.text)
            return ta.text

get_info()
