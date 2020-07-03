from bs4 import BeautifulSoup
import re

list = []
data = open('canadian_writers.html','r')
soup = BeautifulSoup(data, 'html.parser')
details = soup.findAll('tr')
novelists = soup.find_all("td", string="novelist")
#novelists =  soup.body.findAll(text=re.compile('novelist'), limit=1)
#print(novelists)
tr_tags = soup.findAll('tr')
for tr_tag in tr_tags:
    soup = BeautifulSoup(str(tr_tag), 'html.parser')
    td_tags = soup.findAll('td')
    for td_tag in td_tags:
        author = soup.find('a').text
        if "novelist" in str(td_tag):
            #print(author)
            list.append(author)

save_authors = open('can_writers.txt', 'w')
for author in list:
    try:
        save_authors.write(author + "\n")
    except:
        pass
