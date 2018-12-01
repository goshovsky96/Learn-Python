import requests
from datetime import date
sdate = "01.09.2018"
edate = "30.11.2018"
teacher = "Савка (п) Іван Ярославович" 
url = "http://asu.pnu.edu.ua/cgi-bin/timetable.cgi"
headers = {'Content-Type': 'text/html; charset=windows-1251'}
data = {'teacher': teacher.encode('cp1251'), 'sdate': sdate, 'edate': edate}
r = requests.post(url, headers=headers, data = data )
r.encoding = 'cp1251'
soup = BeautifulSoup(r.text, "html.parser")
rows = soup.find_all('tr')
dict_line = {}
if rows:
    for row in rows:
        cols = row.find_all('td')
        if (cols[2].text != '') and (len(cols[2].text.split()) != 0):
            key = cols[2].text.split()[-1]
            if (key in dict_line.keys()):
                dict_line[key]+=1
            else:
                dict_line[key] = 1
print(dict_line)
