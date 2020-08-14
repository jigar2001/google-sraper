import urllib,xlwt,bs4,xlsxwriter
import requests
from xlwt import Workbook
from bs4 import BeautifulSoup

def get_data(query):
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

    MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

    query = query.replace(' ', '+')
    URL = f"https://google.com/search?q={query}&num=100"

    headers = {"user-agent": USER_AGENT}
    resp = requests.get(URL, headers=headers)

    if resp.status_code == 200:
        soup = bs4.BeautifulSoup(resp.content, "html.parser")
        
        count = 0
        for g in soup.find_all('div', class_='r'):
            anchors = g.find_all('a')
            if anchors:
                link = anchors[0]['href']
                title = g.find('h3').text
                
                
                item = {
                    "title": title,
                    "link": link
                }
                
                results.append(item)
                print(g.text)
                sheet.write(count,0,g.text,style)
                count+=1
        
        
            
        return results


workbook = xlwt.Workbook()  
sheet = workbook.add_sheet("Sheet 1", cell_overwrite_ok=True) 
style = xlwt.easyxf('font: bold 1')
results = []                
query=input('serch:')
print(get_data(query))


workbook.save("sample.xls")
